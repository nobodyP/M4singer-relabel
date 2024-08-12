import os
import sys

def rename_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Split the file name and extension
            file_name, file_extension = os.path.splitext(file_name)

            # Get the name of the current folder
            folder_name = os.path.basename(root)

            # Construct the new file name
            new_file_name = f"{file_name}{folder_name}{file_extension}"

            # Build the full paths for the old and new file names
            old_file_path = os.path.join(root, file_name + file_extension)
            new_file_path = os.path.join(root, new_file_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)

if __name__ == "__main__":
    # Check if the command-line argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <main_folder_path>")
        sys.exit(1)

    main_folder_path = sys.argv[1]

    # Check if the provided path is a valid directory
    if not os.path.isdir(main_folder_path):
        print(f"Error: {main_folder_path} is not a valid directory.")
        sys.exit(1)

    # Perform the renaming operation
    rename_files_in_folder(main_folder_path)

    print("File renaming completed.")
