def chat_interface():
    print("Welcome to the Python file runner setup!")
    file = input("Enter the path to the Python file you want to run: ")
    dev_mode = input("Do you want to run in development mode? (y/n): ").lower() == 'y'

    return file, dev_mode
