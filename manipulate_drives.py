import time
import os
import re
import uuid 

ts10_regex = r"(\d{10})[.,]"                                                                        # RegEx for matching 10-character timestamps 
ts13_regex = r"(\d{13})[.,]"                                                                        # RegEx for matching 13-character timestamps 
drive_id_regex = r"drive_id\":\"(.+?)\""                                                            # RegEx for matching UUIDs (Drive_IDs)
label_regex = r"label\":\"(.+?)\""                                                                  # RegEx for matching Labels (Drive_IDs without Hyphens)

files = os.listdir('in/')
if ".DS_Store" in files:
    os.remove("in/.DS_Store")                                                                       # Only relevant in MacOS Systems: Delete System File .DS_Store
    files.remove('.DS_Store')

sorted_files = sorted(files, key=lambda x: int(x))                                                  # File sorting by name
last_timestamp = int(re.findall(ts10_regex, open(f"in/{sorted_files[-1]}").read())[-1])             # Saving the last file timestamp
timestamp_s_now = int(time.strftime("%s"))                                                          # Saving the current unix timestamp
time_difference = timestamp_s_now - last_timestamp                                                  # Calculation of the time difference between now (script execution) and the last file timestamp
new_drive_id = str(uuid.uuid4()).upper()                                                            # Generation of a new UUID (Drive_ID)

for file in sorted_files:
    with open(f"in/{file}", 'r') as f:
        lines = f.readlines()
   
    new_filename = file
    with open(f"out/{new_filename}", 'w') as f:
        for line in lines:
            for match in re.findall(ts10_regex, line):
                line = line.replace(match, str(int(match) + time_difference))                       # Modification of all 10-character timestamps
               
            for match in re.findall(ts13_regex, line):
                line = line.replace(match, str(int(match[:-3]) + time_difference) + match[-3:])     # Modification of all 13-character timestamps
               
            for match in re.findall(drive_id_regex, line):
                line = line.replace(match, new_drive_id)                                            # Replacement of all old Drive_IDs with the newly generated one
               
            for match in re.findall(label_regex, line):                                             # Replacement of all old Labels with the newly generated one
                line = line.replace(match, new_drive_id.replace("-", ""))
               
            f.write(line)
        f.close()

print(f"Done. New Drive_ID: {new_drive_id}")

