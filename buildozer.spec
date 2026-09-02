[app]
title = AI Jinu
package.name = aijinu
package.domain = org.aijinu
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,requests,urllib3,certifi,chardet,idna
orientation = portrait
osx.kivy_version = 2.2.1
fullscreen = 0
android.permissions = INTERNET,RECORD_AUDIO,CAMERA,ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
