
from termcolor import colored

def display_result(agent_name, result, warning):
    if warning:
        print(colored(warning, 'yellow'))
    else:
        print(f"{colored(agent_name, 'magenta')}: {result}")
