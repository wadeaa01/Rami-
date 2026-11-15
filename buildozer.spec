[app]

# (str) Title of your application
title = Ramid3bol

# (str) Package name
package.name = ramid3bol

# (str) Package domain (needed for android packaging)
package.domain = org.ramid3bol

# (str) Source files where the include_exts is located
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# (comma separated)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
# android.api = 33

# (int) Minimum API your APK will support.
# android.minapi = 21

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET
