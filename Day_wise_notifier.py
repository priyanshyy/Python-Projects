""" import time
import os
from plyer import notification

if __name__ == "__main__":
    while True:
        title = "About Today!"
        path='C:\\Users\\chaud\\OneDrive\\Documents\\vocabulary.txt'
        with open(os.path.join(os.path.dirname(__file__),path),'r') as vc:
            lines = vc.readlines() 
            for vocab in lines:
                notification.notify(title=title, message= vocab.strip(), timeout=10)
        time.sleep(60*60*24) """


import time
import os
from plyer import notification

path="C:\projects\checkToday.txt"

def checkToday():
    file=open(path,'r')
    today=time.strftime("%d-%m-%Y")
    flag = 0
    for i in file:
            
                if today in i:
                    i=i.split(' ')
                    flag=1
                    notification.notify(title="About today", message=i.__str__(), timeout=10)
                    
    if flag == 0:
                    notification.notify(title="About today", message="Normal day", timeout=10)

if __name__ == '__main__':
    checkToday()
