[app]
title = Teacher Selector
package.name = teacherselector
package.domain = org.example
source.dir = .
source.main = main.py
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Android settings
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 33.0.2         # match what we install
# android.sdk_build_tools = 33.0.2           # alternative key in older Buildozer
android.sdk = 33
android.ndk = 25b

version = 1.0.0
