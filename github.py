import sublime, sublime_plugin
from xml.dom.minidom import parseString
import re, os
from functools import wraps

class NotAGitRepositoryError(Exception):
  pass

class NotAGithubRepositoryError(Exception):
  pass

class NoFileOpenError(Exception):
  pass

class GitRepo:
  def __init__(self, path):
    self.path = path
    if not self.is_git():
      raise NotAGitRepositoryError

    self.repository_path = self.repository_path()

  def git(self, command):
    os.chdir(self.path)
    return os.popen("git %s" % command).read().strip()

  def repository_path(self):
    repository_path = self.parse_repository(self.git("remote -v"))
    if not repository_path:
      raise NotAGithubRepositoryError
    return repository_path

  def path_from_rootdir(self, filename):
    rootdir = self.git("rev-parse --show-toplevel")
    if self.path != rootdir:
      _, _, path_from_rootdir = self.path.partition(rootdir)
      return path_from_rootdir + '/' + filename
    return filename

  def branch(self):
    return self.parse_branch(self.git("branch"))

  def revision(self):
    return self.git("rev-parse HEAD")

  def browse_file_url(self, filename):
    return git_browse_file_url(self.repository_path, self.path_from_rootdir(filename), self.branch())

  def blame_file_url(self, filename):
    return git_blame_file_url(self.repository_path, self.path_from_rootdir(filename), self.branch())

  def parse_repository(self, remotes):
    remotes = list(set(map(lambda l: re.split("\s", l)[1], remotes.splitlines())))
    return self.make_repository_url(remotes)

  def parse_branch(self, branches):
    p = re.compile("\* (.+)")
    m = p.findall(branches)
    return m[0] if m else None

  def is_git(self):
    os.chdir(self.path)
    code = os.system('git rev-parse')
    return not code

  def make_repository_url(self, remotes):
    for r in remotes:
      if r.startswith('git@'):
        return r[4:-4].replace(":", "/")
      elif r.startswith('https://'):
        return r[8:-4].split("@")[-1]

class GithubWindowCommand(sublime_plugin.WindowCommand):
  def rootdir(self):
    folders = self.window.folders()
    return [i for i in folders if self.filename().startswith(i + os.sep)][0]

  def relative_filename(self):
    _, _, filename = self.filename().partition(self.rootdir())
    return filename

  def filename(self):
    if not self.window.active_view():
      raise NoFileOpenError
    return self.window.active_view().file_name()

  @property
  def repository(self):
    return GitRepo(self.rootdir())

def with_repo(func):
  @wraps(func)
  def wrapper(self):
    try:
      return func(self, self.repository)
    except (NotAGitRepositoryError, NotAGithubRepositoryError):
      sublime.message_dialog("Github repository not found.")
    except (NoFileOpenError):
      sublime.message_dialog("Please open a file first.")
  return wrapper

def git_browse_file_url(repository, filepath, branch='master'):
  return "https://%s/blob/%s%s" % (repository, branch, filepath)

def git_blame_file_url(repository, filepath, branch='master'):
  return "https://%s/blame/%s%s" % (repository, branch, filepath)
