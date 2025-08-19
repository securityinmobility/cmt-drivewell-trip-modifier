# Transferring modified trip data to the smartphone's SD card
adb push modified_app_fil/ /sdcard/
adb push cmtelematics.db /sdcard/

# Copying modified trip data from the smartphone's SD card to the data directory of the \textit{HUK Mein Auto} application
adb shell "su \
    && cp /sdcard/modified_app_fil/* /data/data/de.hdd.telematik/app_fil/ \
    && cp /sdcard/cmtelematics.db /data/data/de.hdd.telematik/databases/"

 # Modifying file system permissions for the altered files
adb shell "su \
    && chown -R 10195 /data/data/de.hdd.telematik/app_fil/ \
    && chgrp -R 10195 /data/data/de.hdd.telematik/app_fil/ \
    && chown 10195 /data/data/de.hdd.telematik/databases/cmtelematics.db \
    && chgrp 10195 /data/data/de.hdd.telematik/databases/cmtelematics.db"

# Retrieving the user ID of the installed \textit{HUK Mein Auto
adb shell dumpsys package de.hdd.telematik | grep userId

# Restoring SELinux permissions for the modified files
adb shell "su \
    && restorecon /data/data/de.hdd.telematik/databases/ \
    && restorecon /data/data/de.hdd.telematik/app_fil/"