
import threading
from utils import Utils
from config import Config
class Simulator(Config):
    
    def __init__(self):
        self.thread = threading.Thread(target=self.runtime)
        self.thread.daemon = True  # Set the thread as a daemon so it exits when the main program ends
        
        

    def start(self):
        self.thread.start()  # Start the background thread

    def Runtime(self):
        # Your background task logic goes here
        while True:
            # Do some work in the background
            print("Background thread is running...")
            print(Config.MAP)
