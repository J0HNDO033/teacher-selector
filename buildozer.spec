[app]

# (str) Title of your application
title = Teacher Selector

# (str) Package name
package.name = teacherselector

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where the main.py lives
source.dir = .

# (str) Application version
version = 1.0.0

# (str) Requirements
requirements = python3,kivy,pyjnius

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported architectures
android.archs = armeabi-v7a, arm64-v8a

# (str) Android SDK API level
android.api = 33

# (str) Minimum Android API level
android.minapi = 21

# (str) Android NDK version (you can leave this default or update)
android.ndk = 27b

# (bool) Copy library instead of making a symlink
android.copy_libs = 1

# (str) Android SDK directory, auto-detected if SDK installed
# android.sdk_path = /path/to/android/sdk

# (str) Android NDK directory, auto-detected if NDK installed
# android.ndk_path = /path/to/android/ndk

# (str) Path to ant, optional if using ant
# android.ant_path = /path/to/apache-ant

# (bool) Enable android logcat debug info (set to True to help debugging)
android.logcat = True

# (str) Application icon
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash image
# presplash.filename = %(source.dir)s/presplash.png

# (bool) Use Cython to speed up pyjnius build (should be True)
cython = True
