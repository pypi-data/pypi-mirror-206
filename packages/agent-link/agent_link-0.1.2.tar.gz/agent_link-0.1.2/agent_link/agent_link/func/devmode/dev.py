import time
import threading
import curses
from watchdog.observers import Observer
from core.tools.file_handler import EnvFileHandler
from core.animation.spinner import spinner
from core.games.snake.play import main

if __name__ == "__main__":
    # curses.wrapper(main) uncomment for games or cool animation
    path = "." 
    event_handler = EnvFileHandler()
    event_handler = EnvFileHandler()
    event_handler.check_existing_files(path)

    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    stop_spinner = threading.Event()
    spinner_thread = threading.Thread(target=spinner, args=(stop_spinner,))
    spinner_thread.start()

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    spinner_thread.join()
