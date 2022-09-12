import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/Satyam/Downloads"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"Hey,{event.src.path}has been created!")

    def on_deleted(self,event):
        print(f"Oops!Someone has deleted {event.src.path} ! ")

    def on_modified(self,event):
        print(f"It looks like someone has modified {event.src.path} file")

    def on_moved(self,event):
        print(f"Oh! You have moved ur {event.src.path} file ")

# Initialize Event Handler Class
event_handler = FileEventHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
 while True :
     time.sleep(2)
     print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()

   
