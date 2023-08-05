import os

def create_directory_and_file(directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        pass

    return file_path
