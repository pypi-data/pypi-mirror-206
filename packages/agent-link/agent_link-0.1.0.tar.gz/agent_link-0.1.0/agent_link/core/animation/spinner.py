from alive_progress import alive_bar
import time

def spinner(stop_spinner):
    with alive_bar(title='Monitoring for .env, node_modules, __pycahce__ and dist...', spinner='classic') as bar:
        while not stop_spinner.is_set():
            bar()
            time.sleep(0.1)

def spinner_task(stop_spinner, task):
    with alive_bar(title={task}, spinner='classic') as bar:
        while not stop_spinner.is_set():
            bar()
            time.sleep(0.1)

