def read_specifications():
    with open("specifications.txt", "r") as spec_file:
        specifications = spec_file.read()
    return specifications