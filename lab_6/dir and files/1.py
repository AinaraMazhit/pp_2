import os
import shutil

# 1 task
def list_directories_files(path="."):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    print("Directories:", directories if directories else "No directories")
    print("Files:", files if files else "No files")
    print("All contents:", os.listdir(path))


# 2 task
def check_access(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    print(f"Path: {path}")
    print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
    print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
    print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")


# 3 task
def path_info(path):
    if not os.path.exists(path):
        print("Path does not exist.")
        return

    print(f"Directory: {os.path.dirname(path)}")
    print(f"File Name: {os.path.basename(path)}")


# 4 task
def count_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print("File not found.")
        return 0


# 5 task
def write_list_to_file(filename, data_list):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for item in data_list:
                file.write(item + "\n")
        print(f"List written to {filename}")
    except Exception as e:
        print(f"Error: {e}")


# 6 task
def generate_text_files():
    for char in range(65, 91):  # ASCII A-Z
        filename = f"{chr(char)}.txt"
        with open(filename, "w") as file:
            file.write(f"File {filename}")
    print("Files A.txt to Z.txt created.")


# 7 task
def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print(f"Copied {source} to {destination}")
    except FileNotFoundError:
        print("Source file not found.")
    except Exception as e:
        print(f"Error: {e}")


# 8 task
def delete_file(path):
    if not os.path.exists(path):
        print("File does not exist.")
        return

    if not os.access(path, os.W_OK):
        print("No permission to delete the file.")
        return

    os.remove(path)
    print(f"File {path} deleted.")


# Test 
if __name__ == "__main__":
    print("Running tests...\n")

    # 1
    list_directories_files(".")

    # 2
    check_access("file_exercises.py")

    # 3
    path_info("file_exercises.py")

    # 4
    print(f"Lines in file: {count_lines('file_exercises.py')}")

    # 5
    write_list_to_file("test_list.txt", ["Hello", "World", "Python"]) 

    # 6
    generate_text_files()

    # 7
    copy_file("test_list.txt", "copy_test.txt")

    # 8
    delete_file("copy_test.txt")
