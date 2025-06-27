[app]

# (str) Title of your application
title = Teacher Selector

# (str) Package name
package.name = teacherselector

# (str) Package domain (reverse DNS style)
package.domain = org.example

# (str) Source code where main.py lives
source.dir = .

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Android entry point, default is ok
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme
android.theme = '@android:style/Theme.NoTitleBar'

# (int) Target Android API, should match what you install
android.api = 33

# (int) Minimum Android API your app supports
android.minapi = 21

# (str) Android SDK build tools version to use, must match installed SDK
android.build_tools_version = 33.0.2

# (list) Permissions your app needs
android.permissions = INTERNET

# (bool) Whether to copy the .pyo files
#android.pyo = False

# (str) Path to presplash image
#presplash.filename = %(source.dir)s/data/presplash.png
