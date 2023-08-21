import os
import shutil
import time
import file_plack


class plack:
    
    def __init__(self):
        self.current_path = os.getcwd()
    
    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
    def create_empty_file(self, filename):
        try:
            os.open(filename, os.O_CREAT)
            print(f"Empty file '{filename}' created successfully using os directly.")
            time.sleep(1.5)
        except Exception as e:
            print(f"Error creating the file: {e}")
            time.sleep(1.5)
                
    def switch_directory(self, new_path):
        if os.path.exists(new_path) and os.path.isdir(new_path):
            self.current_path = new_path
            print(f"Switched to directory: {self.current_path}")
            time.sleep(1.5)
        else:
            print(f"Invalid directory: {new_path}")
            time.sleep(1.5)

    def create_directory(self, target_dir):
        # Create a target directory if it doesn't exit 
        try:
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)
                time.sleep(1.5)
                print(f"Directory {target_dir} created.")
        except Exception as e:
            print(f"Error creating directory {target_dir}: {e}")
            time.sleep(1.5)
            
    def move_file(self, source_file, destination_directory):
        try:
            os.makedirs(destination_directory, exist_ok=True)
            filename = os.path.basename(source_file)
            destination_file = os.path.join(destination_directory, filename)
            shutil.move(source_file, destination_file)
            print(f"Moved {source_file} to {destination_file}.")
            time.sleep(1.5)
            
        except Exception as e:
            print(f"Error moving file {source_file} to {destination_directory}: {e}")
            time.sleep(1.5)
    def delete_file(self, file_path):
        
        try:
            os.remove(file_path)
            print(f"File {file_path} deleted.")
            time.sleep(1.5)
            
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
            time.sleep(1.5)
            
            
    def delete_directory(self, dir_path):
        try:
            shutil.rmtree(dir_path)
            print(f"Directory {dir_path} deleted.")
            time.sleep(1.5)
        except Exception as e:
            print(f"Error deleting directory {dir_path}: {e}")
            time.sleep(1.5)
            
            
    
    
    def list_contents(self):
        print(f"Current path: {self.current_path}")
        files = os.listdir(self.current_path)
        print("\n")
        print("Contents in current directory:")
        for file in files:
            icon = "\uf07b" if os.path.isdir(os.path.join(self.current_path, file)) else "\uf15b"  # Folder and file icons from Nerd Font
            print(f"{icon} {file}")

    
    def switch_directory(self, new_path):
        if os.path.exists(new_path) and os.path.isdir(new_path):
            self.current_path = new_path
            print(f"Switched to directory: {self.current_path}")
            time.sleep(1.5)
        else:
            print(f"Invalid directory: {new_path}")
            time.sleep(1.5)
            
    def display_help(self):
        print("Available commands:")
        print("1. Create file")
        print("2. Create directory")
        print("3. Move file")
        print("4. Delete file")
        print("5. Delete directory")
        print("6. Switch Directory")
        print("10. Exit")
        print("\nPress 'q' to return to the main menu.")

    def start(self):
        database = "plack_database.pickle"
        upload_folder = "uploads"
        self.list_contents()
        print("\n")
        while True:
                
                choice = input("Enter your choice: ")

                if choice == 'q':
                    self.display_help()
                    user_input = input()
                    if user_input == 'q':
                        continue
                
                if choice == '1':
                    file_name = input("Enter file path: ")
                    self.create_empty_file(file_name)
                    self.clear_console()
                    self.list_contents()
                elif choice == '2':
                    target_direc = input("Enter target directory: ")
                    self.create_directory(target_direc)
                    self.clear_console()
                    self.list_contents()
                elif choice == '3':
                    source_file = input("Enter source file: ")
                    destination_directory = input("Enter destination directory: ")
                    self.move_file(source_file, destination_directory)
                    self.clear_console()
                    self.list_contents()
                elif choice == '4':
                    file_path = input("Enter file path: ")
                    self.delete_file(file_path)
                    self.clear_console()
                    self.list_contents()
                elif choice == '5':
                    dir_path = input("Enter directory path: ")
                    self.delete_directory(dir_path)
                    self.clear_console()
                    self.list_contents()
                elif choice == '6':
                    new_directory = input("Enter new directory path: ")
                    self.switch_directory(new_directory)
                    self.clear_console()
                    self.list_contents()
                    print("\n")
                elif choice == '7':
                    print("Exiting...")
                    break
                else:
                    print("Invalid choice. Please select a valid option.")
            
    
if __name__ == "__main__":
    file_manager = plack()
    file_manager.start()