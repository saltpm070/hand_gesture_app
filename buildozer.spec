[app]

# (str) Title of your application
title = Hand Gesture App

# (str) Package name
package.name = gestureapp

# (str) Package domain (needed for android packaging)
package.domain = org.saltpm070

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let's keep it simple)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# DO NOT CHANGE THESE: MediaPipe and OpenCV are sensitive to versions.
requirements = python3,kivy,mediapipe,opencv-python,numpy,pillow

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = CAMERA, INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android archs to build for. 
# arm64-v8a is standard for most modern phones.
android.archs = arm64-v8a

# (bool) Allow backup
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk)
android.release_artifact = apk

# (str) The format used to package the app for debug mode (apk or aab)
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 0