import os
import re

folder_path = "file path to clean data"

def clean_file_names(folder_path):
    for filename in os.listdir(folder_path):
        # Regular expression pattern to replace non-alphanumeric characters with underscores
        new_filename = re.sub(r"\W+", "_", filename)

        # Handle potential duplicate names (add an index if needed)
        if new_filename != filename:
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)

def rename_files_sequentially(folder_path, prefix="image"):
    i = 0
    for filename in os.listdir(folder_path):
        base, ext = os.path.splitext(filename)  # Split into filename and extension
        new_filename = f"{prefix}_{i}{ext}"
        old_filepath = os.path.join(folder_path, filename)
        new_filepath = os.path.join(folder_path, new_filename)
        os.rename(old_filepath, new_filepath)
        i += 1

# Call the functions
clean_file_names(folder_path)
rename_files_sequentially(folder_path)
