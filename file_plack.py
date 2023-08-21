import pickle
import os
import tkinter as tk
from tkinter import filedialog


def create_database(database_file_path):
    if not os.path.exists(database_file_path):
        with open(database_file_path, 'wb') as f:
            pickle.dump([], f)

def get_files(database_file):
    with open(database_file, 'rb') as f:
        return pickle.load(f)


def save_file(database_file, filename):
    files = get_files(database_file)
    files.append(filename)
    with open(database_file, 'wb') as f:
        pickle.dump(files, f)


def upload_file(database_file, upload_folder):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Choose a file")
    if file_path:
        filename = os.path.basename(file_path)
        target_path = os.path.join(upload_folder, filename)
        os.makedirs(upload_folder, exist_ok=True)
        os.rename(file_path, target_path)
        save_file(database_file, filename)
        print("File uploaded successfully!")
    else:
        print("No file selected.")


def list_files(database_file):
    files = get_files(database_file)
    if files:
        print("Uploaded Images:")
        for image in files:
            print(image)
    else:
        print("No images found.")


def main():
    database_file = "image_database.pickle"
    upload_folder = "uploads"

    # create_database(database_file)

    while True:
        print("\nMenu:")
        print("1. Upload an image")
        print("2. List uploaded images")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            upload_file(database_file, upload_folder)
        elif choice == '2':
            list_files(database_file)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
    
