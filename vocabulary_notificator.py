import time
import os
from plyer import notification

if __name__ == "__main__":
    while True:
        title = "Learn this Vocab"
        path='C:\\Users\\chaud\\OneDrive\\Documents\\vocabulary.txt'
        with open(os.path.join(os.path.dirname(__file__),path),'r') as vc:
            lines = vc.readlines() 
            for vocab in lines:
                notification.notify(title= title, message= vocab.strip(), timeout= 10)
                time.sleep(5)