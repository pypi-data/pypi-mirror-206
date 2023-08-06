from watchdog.observers import Observer
from core.tools.file_handler import EnvFileHandler

def run_observer_and_spinner():
    observer = Observer()
    observer.schedule(EnvFileHandler(), '.', recursive=True)
    observer.start()

    stop_spinner = threading.Event()
    spinner_thread = threading.Thread(target=spinner, args=(stop_spinner,))
    spinner_thread.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        stop_spinner.set()

    observer.join()
    spinner_thread.join()
