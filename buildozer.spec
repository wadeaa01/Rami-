[app]

title = Ramid3bol
package.name = ramid3bol
package.domain = org.ramid3bol
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (str) Android arch to build for
android.archs = arm64-v8a

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b
