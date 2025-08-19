# Finding and copying the application package from the smartphone to a computer
# List all installed packages on the Android device. This step is necessary if the name of the package is not known.
# adb shell pm list packages
# Find the installation path of the desired application
adb shell pm path de.hdd.telematikplus
# Copy the APK file to the computer
adb pull /data/app/de.hdd.telematik-.../ /desired/path/

# Copying the application folder from the smartphone to a computer
# Access the device and switch to root privileges
adb shell "su \
    && cp -r /data/data/de.hdd.telematik/ /sdcard/"

# Copy the entire Folder to a desired path on the computer
adb pull /sdcard/de.hdd.telematik-.../ /desired/path/    