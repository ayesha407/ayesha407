import os import shutil from pathlib import Path

Define file type categories

FILE_CATEGORIES = { 'Documents': ['.pdf', '.docx', '.txt', '.xlsx'], 'Images': ['.jpg', '.jpeg', '.png', '.gif'], 'Videos': ['.mp4', '.mov', '.avi'], 'Audio': ['.mp3', '.wav', '.aac'], 'Archives': ['.zip', '.rar', '.7z'], 'Others': [] }

def organize_files(directory): """ Organize files in the specified directory into folders based on their file type. """ for item in os.listdir(directory): item_path = os.path.join(directory, item) if os.path.isfile(item_path): file_extension = Path(item_path).suffix.lower() destination_folder = get_destination_folder(file_extension) if destination_folder: move_file(item_path, os.path.join(directory, destination_folder))

def get_destination_folder(extension): """Determine the destination folder based on file extension.""" for category, extensions in FILE_CATEGORIES.items(): if extension in extensions: return category return 'Others'

def move_file(file_path, destination_folder): """Move the file to the appropriate folder, creating it if necessary.""" os.makedirs(destination_folder, exist_ok=True) try: shutil.move(file_path, destination_folder) print(f"Moved {file_path} to {destination_folder}") except Exception as e: print(f"Error moving {file_path}: {e}")

if name == "main": target_directory = input("Enter the directory to organize: ").strip() if os.path.isdir(target_directory): organize_files(target_directory) print("File organization complete.") else: print("Invalid directory path.")
