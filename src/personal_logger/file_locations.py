import os

LOG_DIRECTORY="var/personal_log_data/"

current_dir = os.path.dirname(os.path.abspath(__file__))
#print(f"Current directory: {current_dir}")

parent_dir = os.path.dirname(current_dir)
#print(f"Parent directory: {parent_dir}")

root_dir = os.path.dirname(parent_dir)
#print(f"Root directory: {root_dir}")


person_log_file_path = os.path.join(root_dir, LOG_DIRECTORY)
