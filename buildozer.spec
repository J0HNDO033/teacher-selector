[app]

# (str) Title of your application
title = Teacher Selector

# (str) Package name
package.name = teacherselector

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py is located
source.dir = .

# (str) Application entry point
source.main = main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash image (optional)
#presplash.filename =

# (list) Permissions
android.permissions = INTERNET

# (str) Android API level
android.api = 33

# (int) Minimum API level your APK will support
android.minapi = 21

# (int) Android SDK build tools version
android.build_tools_version = 33.0.2

# (str) Android NDK version (recommended matching with SDK)
android.ndk = 25b

# (int) Target Android SDK version
android.sdk = 33

# (str) Application versioning
version = 1.0.0

# (str) Application icon (optional)
#icon.filename = %(source.dir)s/icon.png

# (str) Presplash screen animation (optional)
#presplash.filename =

# (list) Source include patterns
#source.include_exts = py,png,jpg,kv,atlas

# (list) Exclude patterns
#source.exclude_exts =

# (bool) Copy all files from source.dir except those ignored by .gitignore
# (default is True)
#copy_without_render = False

# (bool) Enable Android logcat debug output
android.logcat_filters = *:S python:D

# (bool) Enable debug build
debug = 0

# (str) Additional command line arguments for buildozer
#buildozer.args =

# (str) Android manifest additions (optional)
#android.manifest_xml =

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (int) Android entrypoint (default is python3)
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android presplash background color
#android.presplash_color = #FFFFFF

# (str) Android application theme, default is "import android"
#android.theme = '@android:style/Theme.NoTitleBar'

# (bool) Enable or disable OpenGL ES 2.0 support (True by default)
#android.opengl_es = True

# (int) Android icon density (default 160)
#android.icon_density = 160

