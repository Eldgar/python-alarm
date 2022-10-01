from sub_programs import music_list, data_entry_google
#from sub_programs import music_list, play_song
import schedule
import time
import random
import datetime
from tkinter import *

#async to allow adding workout numbers to gui
import asyncio

 

async def alarm(set_alarm_timer):
    while True:
        
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            music_list.play_song(music_list.music_list[random.randint(0, len(music_list.music_list)-1)])
            break
        print('while loop')
        time.sleep(60)
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}"
    print('test')
    asyncio.run(alarm(set_alarm_timer))


gui = Tk()
gui.title("Morning Workout Alarm Clock")
gui.geometry("600x300")
time_format=Label(gui, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=70,y=120)
addTime = Label(gui,text = "Hour     Min",font=60).place(x = 130)
setYourAlarm = Label(gui,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
#Time required to set the alarm clock
hourTime= Entry(gui,textvariable = hour,bg = "pink",width = 15).place(x=130,y=30)
minTime= Entry(gui,textvariable = min,bg = "pink",width = 15).place(x=200,y=30)
#To take the time input by user:
submit_time = Button(gui,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)


#labels to describe program in gui
workout_format=Label(gui,text = "Pushups    Squats",font=60).place(x = 120, y=190)


#function for adding numbers to google sheets
def submit_data(pushups, squats):
    print(squats)
    print(pushups)
    data_entry_google.update_workout(pushups, squats)



#workout numbers
push_ups = StringVar()
squats = StringVar()
#inputs for the workouts
number_push_ups= Entry(gui,textvariable = push_ups,bg = "pink",width = 15).place(x=110,y=230)
number_push_ups= Entry(gui,textvariable = squats,bg = "pink",width = 15).place(x=170,y=230)
# submit workout numbers
# .get() is used to retrieve values from Entry, lambda function used to fix issue with command triggering on startup
submit_workout = Button(gui,text = "Submit Numbers for workout",fg="black",width = 25,command=lambda :submit_data(push_ups.get(), squats.get())).place(x =110,y=260)


#Execution of the window.
gui.mainloop()




#play_song(music_list[random.randint(0, len(music_list)-1)]) f"{hour.get()}:{min.get()}:{sec.get()}"

