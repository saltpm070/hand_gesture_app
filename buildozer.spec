[app]
title = GesturePro
package.name = gesturepro
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,tflite
# This ensures we don't try to package the "build" folder into the "build" folder
source.exclude_dirs = bin, venv, .git, __pycache__, .buildozer, android

version = 0.1

# Simplified requirements to prevent version clashing
requirements = python3,kivy==2.3.0,mediapipe,opencv-python,numpy,pillow,android,hostpython3

orientation = portrait
android.permissions = CAMERA, INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# The "Big Project" Flags
android.gradle_dependencies = "androidx.multidex:multidex:2.0.1"
android.enable_androidx = True
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 0