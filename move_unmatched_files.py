import os
import sys
import shutil

def move_unmatched_files(folder_path):
    # Create the "not_done" folder if it doesn't exist
    not_done_folder = os.path.join(folder_path, "not_done")
    os.makedirs(not_done_folder, exist_ok=True)

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Skip the "not_done" folder itself
        if file_name == "not_done":
            continue

        # Get the file name and extension
        base_name, file_extension = os.path.splitext(file_name)

        # Check if the file is a .wav or .lab file
        if file_extension == '.wav' or file_extension == '.lab':
            # Construct the counterpart file name
            counterpart_name = f"{base_name}.{'lab' if file_extension == '.wav' else 'wav'}"

            # Construct the full paths for the current file and its counterpart
            current_file_path = os.path.join(folder_path, file_name)
            counterpart_file_path = os.path.join(folder_path, counterpart_name)

            # Check if the counterpart file exists
            if not os.path.exists(counterpart_file_path):
                # Move the file to the "not_done" folder
                destination_path = os.path.join(not_done_folder, file_name)
                print(f"Moving: {current_file_path} to {destination_path}")
                shutil.move(current_file_path, destination_path)

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

    # Perform the file moving operation
    move_unmatched_files(main_folder_path)

    print("File moving completed.")