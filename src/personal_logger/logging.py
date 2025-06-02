import datetime
import time
import os
import re
import file_locations

LOG_EXTENTION = ".txt"

def read_log(y,m,d):
    log_contents = ""
    stripped_line=""
    readable_date=""

    file_name = file_locations.person_log_file_path + y + "_" + m + "_" + d + LOG_EXTENTION
    file_available=False

    try:
        file=open(file_name,"r")
        lines=file.readlines()
        file.close()
        file_available=True
        for i in range(2,len(lines)):
            # remove epoch timestamp
            _, _, stripped_line = lines[i].partition("|")
            #split stripped_line into readable timestamp and text
            readable_date, _, log_text = stripped_line.partition("|")
            log_contents += readable_date + "  " + log_text
    except FileNotFoundError:
        print("Error: File not found")
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print("Error: ", e)
    return file_available,log_contents

def write_log(content):
    log_entry=""
    today = datetime.date.today()
    file_name=file_locations.person_log_file_path + today.strftime("%Y_%m_%d")+LOG_EXTENTION

    utc_timestamp_from_now = str(datetime.datetime.now(datetime.timezone.utc).timestamp())

    datetime_object = datetime.datetime.fromtimestamp(time.time())
    readable_datetime = datetime_object.strftime("%Y-%m-%d %H:%M:%S")

    #remove newline
    cleaned_text = re.sub(r"\n", "   ", content)
    log_entry = utc_timestamp_from_now + "|" + readable_datetime + "|" + cleaned_text + "\n"

    file_available=False

    try:
        file = open(file_name,"r")
        file.close()
        file_available=True
    except FileNotFoundError:
        file = open(file_name,"w")
        file.write(today.strftime("%Y_%m_%d")+LOG_EXTENTION+"\n\n")
        file.close()
        file_available=True
    except PermissionError:
        print("Error: Permission denied")
    except Exception as e:
        print("Error: ", e)

    if file_available:
        write_file = open(file_name,"a")
        write_file.write(log_entry)
        write_file.close()

    return file_available

# test
if __name__ == "__main__":
   print(write_log("TEST2"))




