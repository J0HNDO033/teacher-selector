[app]

# (str) Title of your application
title = TeacherSelector

# (str) Package name
package.name = teacherselector

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.code = 1

# (str) Application versioning (method 3)
# version.regex =

# (str) Application versioning (method 4)
# version.git_commit =

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, must match the SDK platforms installed
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK build tools version to use
android.build_tools_version = 33.0.2

# (str) Android NDK version to use (optional)
# android.ndk = 25b

# (str) Android SDK directory (optional)
# android.sdk_path =

# (str) Android NDK directory (optional)
# android.ndk_path =

# (bool) Indicate if the Android app should be fullscreen or not
fullscreen = 1

# (bool) Hide the statusbar
android.hide_statusbar = 1

# (str) Application icon
# icon.filename = %(source.dir)s/icon.png

# (list) Application requirements
requirements = python3, kivy

# (str) Supported orientations
orientation = portrait

# (bool) Whether to copy assets from source dir to the package
presplash.filename =

# (str) Entry point (default is main.py)
# entrypoint = main.py

[buildozer]

log_level = 2
warn_on_root = 1
