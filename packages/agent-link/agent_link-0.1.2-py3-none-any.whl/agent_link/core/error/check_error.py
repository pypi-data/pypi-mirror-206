import re

def check_errors(process):
    error_pattern = re.compile(r'Error', re.IGNORECASE)

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
            if error_pattern.search(output.strip()):
                process.terminate()
                return True
    return False
