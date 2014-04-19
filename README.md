# Sublime Text 2 Github Tools #

## Introduction ##

A set of handy tools for using Sublime Text 2 editor with [Github](http://github.com). If you're [Beanstalk](http://beanstalkapp.com) user, then check out [Sublime Text 2 Beanstalk Tools](https://github.com/temochka/sublime-text-2-beanstalk).

## Usage ##

Open any directory of your GIT working copy in Sublime Text 2.

* Press `Ctrl + Shift + P` and select `Github: Open File` or just press `Ctrl + Shift + ^` to open currently edited file in Github.
* Press `Ctrl + Shift + P` and select `Github: Blame` to open blame for currently edited file in Github.

Use `Cmd` instead of `Ctrl` on Mac OS X.

## Get it installed ##

### With The Package Control Plugin ###

Press `Ctrl + Shift + P` to open the Command Palette type `pack install`, search for Github Tools and press enter

Use `Cmd` instead of `Ctrl` on Mac OS X.

### On Mac ###

```bash
cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
git clone git://github.com/temochka/sublime-text-2-github.git
```

### On Linux ###

```bash
cd ~/.config/sublime-text-2/Packages/
git clone git://github.com/temochka/sublime-text-2-github.git
```

### On Windows ###

```
cd %APPDATA%/Sublime Text 2/Packages/
git clone git://github.com/temochka/sublime-text-2-github.git
```

Make sure you have included all required binaries (`git`, `svn`) in your PATH.