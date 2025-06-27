[app]
title = Teacher Selector
package.name = teacherselector
package.domain = org.example
source.dir = .
source.main = main.py
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

# Android settings
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True
android.archs = armeabi-v7a, arm64-v8a

# Use SDL2 bootstrap (default & recommended)
android.bootstrap = sdl2

# Optional: improves speed and debugging in CI/CD
android.debug = 1
android.copy_libs = 1

[hostpython]
# Optional for better compatibility in newer P4A
# hostpython = 3.11
