# inspired by https://github.com/weslly/ColorPicker/blob/master/sublimecp.py
import sublime
import os
import shutil

PKGNAME = 'SendTextPlus'


def update_resources(*target):
    targetpath = os.path.join(sublime.packages_path(), 'User', PKGNAME, *target)
    targetdir = os.path.dirname(targetpath)
    respath = 'Packages/%s/' % PKGNAME + "/".join(target)
    pkgpath = os.path.join(sublime.installed_packages_path(), '%s.sublime-package' % PKGNAME)
    unpkgpath = os.path.join(sublime.packages_path(), PKGNAME, *target)

    if os.path.exists(targetpath):
        targetinfo = os.stat(targetpath)
    else:
        if not os.path.exists(targetdir):
            os.makedirs(targetdir, 0o755)
        targetinfo = None

    if os.path.exists(unpkgpath):
        pkginfo = os.stat(unpkgpath)
    elif os.path.exists(pkgpath):
        pkginfo = os.stat(pkgpath)
    else:
        return

    if targetinfo is None or targetinfo.st_mtime < pkginfo.st_mtime:
        print("* Updating " + targetpath)
        if sublime.version() < '3000':
            shutil.copy2(unpkgpath, targetpath)
        else:
            data = sublime.load_binary_resource(respath)
            with open(targetpath, 'wb') as f:
                f.write(data)
                f.close()

    if not os.access(targetpath, os.X_OK):
        os.chmod(targetpath, 0o755)


def plugin_loaded():
    if sublime.platform() == "windows":
        update_resources("bin", "AutoHotkeyU32.exe")
        update_resources("bin", "Cmder.ahk")
        update_resources("bin", "Cygwin.ahk")
        update_resources("bin", "RStudio.ahk")
        update_resources("bin", "Rgui.ahk")
