[app]
title = Hand Gesture App
package.name = gestureapp
package.domain = org.saltpm070
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0,mediapipe,opencv-python,numpy
orientation = portrait
android.permissions = CAMERA
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
