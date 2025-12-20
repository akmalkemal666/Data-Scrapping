import os

def create_directory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def create_new_file(path):
    with open(path, 'w') as f:
        f.write("")

def write_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + "\n")

def clear_file(path):
    with open(path, 'w') as f:
        f.write("")

def does_file(path):
    if os.path.isfile(path):
        print(f"File '{path}' ADA di sistem.")
        return True
    else:
        print(f"File '{path}' TIDAK ditemukan.")
        return False

def read_data(path):
    print("\nIsi file (dibaca baris per baris):")
    with open(path, 'rt') as file:
        for line in file:
            print(line.strip())

def read_data_as_list(path):
    with open(path, 'rt') as file:
        return [line.strip() for line in file]

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
        print(f"File '{path}' berhasil dihapus.")
    else:
        print("File tidak ditemukan")
