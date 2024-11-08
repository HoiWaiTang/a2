## Table of contents
* [General Information](#general-information)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Status](#status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## General info
This Python script with a Graphical User Interface (GUI) calculates and displays a small list of alarm durations so that you can wake up without feeling tired or needing to set a lot of alarms by showing you times which you will likely be in light sleep.
An Internet connection is required for the script to function.

## Features
Uses the current time to begin calculating the times you should set your alarm to
Calculates when's the next sunrise and sunset if you wake up before said times
Input custom time when you plan on napping/sleeping at another time
Keybinds for efficiency (Did you know that using keyboard shortcuts is estimated to save you 64 hours a year?)

## Setup
To use the .exe:
Downloaded the .exe
The .exe can be used when your device is connected to the Internet

To use the .pyw:
pip install datetime
pip install geocoder
pip install suntime
pip install tkinter
The .pyw can be used when your device is connected to the Internet

Optionally, to convert the .pyw into .exe:
pip install pyinstaller
Open Git Bash or type in "cmd" in the file directory of where the .pyw is located
Input "pyinstaller --onefile Alarm_Calculator.pyw" and press Enter
The .exe is generated in the "dist" folder for use when your device is connected to the Internet and you may delete the newly generated unecessary assets

## Usage
Choose your own start time by typing in the time in HH:MM format into the entry field and click the button
Refresh/reset the calculated times by clicking the "Refresh/Reset" button at the bottom or press F5, R, or the space bar
Use X or the Escape key to terminate the GUI

## Status
The project ceases development with the submission for A2 in the UTS course 52685 Working with Data and Code.

## Room for Improvement
.apk support
.app support
.ipa support
Offline usage
Optimizations

## Acknowledgements
I acknowledge the use of ChatGPT (https://chat.openai.com/) to generate parts of the script that were beyond my experience and skill level.

Prompt 1:
Can you make it so that users can input the custom time and the code will take the input to perform time calculations?

#datetime import retrieved from https://stackoverflow.com/questions/68632685/alarm-clock-in-python
from datetime import datetime, timedelta
#tkinter GUI toolkit import retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
import tkinter as tk
from tkinter import *   

#Function to update & show times retrieved from https://www.programiz.com/python-programming/datetime/current-time
def update_times():
    timeNow = datetime.now()
    currentTime = timeNow.strftime('%H:%M')

#Math retrieved from https://www.geeksforgeeks.org/how-to-add-time-onto-a-datetime-object-in-python/
    time_change1 = timedelta(minutes=6)
    time_change2 = timedelta(minutes=11)
    time_change3 = timedelta(minutes=21)
    time_change4 = timedelta(minutes=61)
    time_change5 = timedelta(minutes=91)
    time_change6 = timedelta(minutes=185)
    time_change7 = timedelta(minutes=302)
    time_change8 = timedelta(minutes=392)
    time_change9 = timedelta(minutes=470)
    new_time1 = timeNow + time_change1
    new_time2 = timeNow + time_change2
    new_time3 = timeNow + time_change3
    new_time4 = timeNow + time_change4
    new_time5 = timeNow + time_change5
    new_time6 = timeNow + time_change6
    new_time7 = timeNow + time_change7
    new_time8 = timeNow + time_change8
    new_time9 = timeNow + time_change9

#Update labels w/ new times
    current_time_label.config(text=f"Current Time: {currentTime}")
    us_nap_label.config(text=f"Ultra short nap alarm time (+6m): {new_time1.strftime('%H:%M')}")
    short_nap_label.config(text=f"Short nap alarm time (+11m): {new_time2.strftime('%H:%M')}")
    power_nap_label.config(text=f"Power nap alarm time (+21m): {new_time3.strftime('%H:%M')}")
    longer_nap_label.config(text=f"Longer nap alarm time (+61m): {new_time4.strftime('%H:%M')}")
    cycle1_label.config(text=f"1 cycle alarm time (+91m): {new_time5.strftime('%H:%M')}")
    cycle2_label.config(text=f"2 cycle alarm time (+185m): {new_time6.strftime('%H:%M')}")
    cycle3_label.config(text=f"3 cycle alarm time (+302m): {new_time7.strftime('%H:%M')}")
    cycle4_label.config(text=f"4 cycle alarm time (+392m): {new_time8.strftime('%H:%M')}")
    cycle5_label.config(text=f"5 cycle alarm time (+470m): {new_time9.strftime('%H:%M')}")

#Window creation retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Background color retrieved from https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python
#Winow geometry retrieved from https://stackoverflow.com/questions/68240695/how-to-change-the-window-size-after-the-program-starts
root = tk.Tk()
root.title("(:")
root.configure(background='#CFE8CC')
root.geometry("230x310")
root.minsize(230, 310)
root.maxsize(1920, 1080)

#Custom time input label retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Entry field retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Vertical center aligning text retrieved from https://stackoverflow.com/questions/68148478/how-to-vertically-center-a-text-label-in-tkinter
#Label background color configuration retrieved from https://www.reddit.com/r/learnpython/comments/11dh1t0/comment/ja8n62f/
#Button retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
custom_entry_label = tk.Label(root, text="Set Custom Time:")
custom_entry_label.pack(expand=True)
custom_entry_label.configure(bg="#CFE8CC")
entry_field = tk.Entry(root)
entry_field.pack(expand=True)
def use_custom_time():
    custom_time=entry_field.get()
    update_times(custom_time)
custom_button = tk.Button(root, text="Use Custom Time", command=use_custom_time)
custom_button.pack(expand=True)

#Labels to show times retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Vertical center aligning text retrieved from https://stackoverflow.com/questions/68148478/how-to-vertically-center-a-text-label-in-tkinter
#Label background color configuration retrieved from https://www.reddit.com/r/learnpython/comments/11dh1t0/comment/ja8n62f/
current_time_label = tk.Label(root, text="Current Time: ")
current_time_label.pack(expand=True)
current_time_label.configure(bg="#CFE8CC")

us_nap_label = tk.Label(root, text="Ultra short nap alarm time (+6m): ")
us_nap_label.pack(expand=True)
us_nap_label.configure(bg="#CFE8CC")

short_nap_label = tk.Label(root, text="Short nap alarm time (+11m): ")
short_nap_label.pack(expand=True)
short_nap_label.configure(bg="#CFE8CC")

power_nap_label = tk.Label(root, text="Power nap alarm time (+21m): ")
power_nap_label.pack(expand=True)
power_nap_label.configure(bg="#CFE8CC")

longer_nap_label = tk.Label(root, text="Longer nap alarm time (+61m): ")
longer_nap_label.pack(expand=True)
longer_nap_label.configure(bg="#CFE8CC")

cycle1_label = tk.Label(root, text="1 cycle alarm time  (+91m): ")
cycle1_label.pack(expand=True)
cycle1_label.configure(bg="#CFE8CC")

cycle2_label = tk.Label(root, text="2 cycle alarm time (+185m): ")
cycle2_label.pack(expand=True)
cycle2_label.configure(bg="#CFE8CC")

cycle3_label = tk.Label(root, text="3 cycle alarm time (+302m): ")
cycle3_label.pack(expand=True)
cycle3_label.configure(bg="#CFE8CC")

cycle4_label = tk.Label(root, text="4 cycle alarm time (+392m): ")
cycle4_label.pack(expand=True)
cycle4_label.configure(bg="#CFE8CC")

cycle5_label = tk.Label(root, text="5 cycle alarm time (+470m): ")
cycle5_label.pack(expand=True)
cycle5_label.configure(bg="#CFE8CC")

#Refresh button & keybinds
#Button retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Keybinds retrieved from https://www.geeksforgeeks.org/python-binding-function-in-tkinter/
def close_ui(event=None):
    root.quit()
refresh_button = tk.Button(root, text="Refresh/Reset", command=update_times)
refresh_button.pack()
root.bind("<F5>", lambda event: update_times())
root.bind("<r>", lambda event: update_times())
root.bind("<Escape>", close_ui)
root.bind("<x>", close_ui)

#Start UI & show times retrieved from https://www.programiz.com/python-programming/datetime/current-time
update_times()

#Setting tkinter loop retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
root.mainloop()

Output 1:
To allow users to input a custom time and perform time calculations based on it, we can modify the update_times function to accept an optional custom time. If a user provides input, the program will use the custom time instead of the current time for calculations.

Here is the updated version of your code that allows custom time input:

from datetime import datetime, timedelta
import tkinter as tk
from tkinter import *

# Function to update & show times, now accepting custom time input
def update_times(custom_time=None):
    if custom_time:
        # Parse the custom time provided by the user (assumes HH:MM format)
        timeNow = datetime.strptime(custom_time, '%H:%M')
    else:
        timeNow = datetime.now()

    currentTime = timeNow.strftime('%H:%M')

    # Time increments
    time_change1 = timedelta(minutes=6)
    time_change2 = timedelta(minutes=11)
    time_change3 = timedelta(minutes=21)
    time_change4 = timedelta(minutes=61)
    time_change5 = timedelta(minutes=91)
    time_change6 = timedelta(minutes=185)
    time_change7 = timedelta(minutes=302)
    time_change8 = timedelta(minutes=392)
    time_change9 = timedelta(minutes=470)

    # New times after applying the changes
    new_time1 = timeNow + time_change1
    new_time2 = timeNow + time_change2
    new_time3 = timeNow + time_change3
    new_time4 = timeNow + time_change4
    new_time5 = timeNow + time_change5
    new_time6 = timeNow + time_change6
    new_time7 = timeNow + time_change7
    new_time8 = timeNow + time_change8
    new_time9 = timeNow + time_change9

    # Update labels with new times
    current_time_label.config(text=f"Current Time: {currentTime}")
    us_nap_label.config(text=f"Ultra short nap alarm time (+6m): {new_time1.strftime('%H:%M')}")
    short_nap_label.config(text=f"Short nap alarm time (+11m): {new_time2.strftime('%H:%M')}")
    power_nap_label.config(text=f"Power nap alarm time (+21m): {new_time3.strftime('%H:%M')}")
    longer_nap_label.config(text=f"Longer nap alarm time (+61m): {new_time4.strftime('%H:%M')}")
    cycle1_label.config(text=f"1 cycle alarm time (+91m): {new_time5.strftime('%H:%M')}")
    cycle2_label.config(text=f"2 cycle alarm time (+185m): {new_time6.strftime('%H:%M')}")
    cycle3_label.config(text=f"3 cycle alarm time (+302m): {new_time7.strftime('%H:%M')}")
    cycle4_label.config(text=f"4 cycle alarm time (+392m): {new_time8.strftime('%H:%M')}")
    cycle5_label.config(text=f"5 cycle alarm time (+470m): {new_time9.strftime('%H:%M')}")

# Function to handle custom time input and trigger updates
def use_custom_time():
    custom_time = entry_field.get()
    try:
        # Validate and update times based on custom input
        update_times(custom_time)
    except ValueError:
        # Handle invalid input (e.g., incorrect time format)
        current_time_label.config(text="Invalid time format! Use HH:MM.")

# Window setup
root = tk.Tk()
root.title("Nap Alarm Clock")
root.configure(background='#CFE8CC')
root.geometry("230x310")
root.minsize(230, 310)
root.maxsize(1920, 1080)

# Custom time input label and entry field
custom_entry_label = tk.Label(root, text="Set Custom Time (HH:MM):")
custom_entry_label.pack(expand=True)
custom_entry_label.configure(bg="#CFE8CC")
entry_field = tk.Entry(root)
entry_field.pack(expand=True)

# Button to use custom time
custom_button = tk.Button(root, text="Use Custom Time", command=use_custom_time)
custom_button.pack(expand=True)

# Labels to display times
current_time_label = tk.Label(root, text="Current Time: ")
current_time_label.pack(expand=True)
current_time_label.configure(bg="#CFE8CC")

us_nap_label = tk.Label(root, text="Ultra short nap alarm time (+6m): ")
us_nap_label.pack(expand=True)
us_nap_label.configure(bg="#CFE8CC")

short_nap_label = tk.Label(root, text="Short nap alarm time (+11m): ")
short_nap_label.pack(expand=True)
short_nap_label.configure(bg="#CFE8CC")

power_nap_label = tk.Label(root, text="Power nap alarm time (+21m): ")
power_nap_label.pack(expand=True)
power_nap_label.configure(bg="#CFE8CC")

longer_nap_label = tk.Label(root, text="Longer nap alarm time (+61m): ")
longer_nap_label.pack(expand=True)
longer_nap_label.configure(bg="#CFE8CC")

cycle1_label = tk.Label(root, text="1 cycle alarm time  (+91m): ")
cycle1_label.pack(expand=True)
cycle1_label.configure(bg="#CFE8CC")

cycle2_label = tk.Label(root, text="2 cycle alarm time (+185m): ")
cycle2_label.pack(expand=True)
cycle2_label.configure(bg="#CFE8CC")

cycle3_label = tk.Label(root, text="3 cycle alarm time (+302m): ")
cycle3_label.pack(expand=True)
cycle3_label.configure(bg="#CFE8CC")

cycle4_label = tk.Label(root, text="4 cycle alarm time (+392m): ")
cycle4_label.pack(expand=True)
cycle4_label.configure(bg="#CFE8CC")

cycle5_label = tk.Label(root, text="5 cycle alarm time (+470m): ")
cycle5_label.pack(expand=True)
cycle5_label.configure(bg="#CFE8CC")

# Refresh button & keybinds
def close_ui(event=None):
    root.quit()

refresh_button = tk.Button(root, text="Refresh/Reset", command=update_times)
refresh_button.pack()
root.bind("<F5>", lambda event: update_times())
root.bind("<r>", lambda event: update_times())
root.bind("<Escape>", close_ui)
root.bind("<x>", close_ui)

# Start UI and show current times
update_times()

# Setting tkinter loop
root.mainloop()

Key changes:

    The update_times function now accepts an optional custom_time argument.
    The custom time is parsed using datetime.strptime() to validate the format.
    If the input is invalid, an error message is displayed on the current time label.
    The user can input custom times in the format HH:MM, and the system will calculate based on that.

Prompt 2:
#datetime import retrieved from 
from datetime import date, datetime, timedelta
#tkinter GUI toolkit import retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
import tkinter as tk
from tkinter import *
#Coordinates retrieval retrieved from https://medium.com/@omraghuvanshi1010/unveiling-your-location-a-python-guide-to-retrieve-current-gps-coordinates-d1ba282b44fd
import geocoder
#SunTime retrieved from https://stackoverflow.com/a/57963943
from suntime import Sun, SunTimeException

#Defining function for coordinates retrieval retrieved from https://medium.com/@omraghuvanshi1010/unveiling-your-location-a-python-guide-to-retrieve-current-gps-coordinates-d1ba282b44fd
def get_current_gps_coordinates():
    g = geocoder.ip('me')
    if g.latlng is not None:
        return g.latlng
    else:
        return None
if __name__ == "__main__":
    coordinates = get_current_gps_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates

#SunTime calculation retrieved from https://stackoverflow.com/a/57963943
sun = Sun(latitude, longitude)

#
today = date.today()
tomorrow = today + timedelta(days=1)

#Defining function to update & show times retrieved from https://www.programiz.com/python-programming/datetime/current-time
#Custom time feature retrieved from ChatGPT
def update_times(custom_time=None):
    if custom_time:
        timeNow = datetime.strptime(custom_time,'%H:%M')
    else:
        timeNow = datetime.now()
    
    currentTime = timeNow.strftime('%H:%M')

#Math retrieved from https://www.geeksforgeeks.org/how-to-add-time-onto-a-datetime-object-in-python/
    time_change1 = timedelta(minutes=6)
    time_change2 = timedelta(minutes=11)
    time_change3 = timedelta(minutes=21)
    time_change4 = timedelta(minutes=61)
    time_change5 = timedelta(minutes=91)
    time_change6 = timedelta(minutes=185)
    time_change7 = timedelta(minutes=302)
    time_change8 = timedelta(minutes=392)
    time_change9 = timedelta(minutes=470)
    new_time1 = timeNow + time_change1
    new_time2 = timeNow + time_change2
    new_time3 = timeNow + time_change3
    new_time4 = timeNow + time_change4
    new_time5 = timeNow + time_change5
    new_time6 = timeNow + time_change6
    new_time7 = timeNow + time_change7
    new_time8 = timeNow + time_change8
    new_time9 = timeNow + time_change9

#Update labels w/ (new) times
    current_time_label.config(text=f"Current Time: {currentTime}")
    us_nap_label.config(text=f"Ultra short nap alarm time (+6m): {new_time1.strftime('%H:%M')}")
    short_nap_label.config(text=f"Short nap alarm time (+11m): {new_time2.strftime('%H:%M')}")
    power_nap_label.config(text=f"Power nap alarm time (+21m): {new_time3.strftime('%H:%M')}")
    longer_nap_label.config(text=f"Longer nap alarm time (+61m): {new_time4.strftime('%H:%M')}")
    ss_label.config(text=f"Next sunset time: {today_ss.strftime('%H:%M')}")
    sr_label.config(text=f"Next sunrise time: {today_sr.strftime('%H:%M')}")
    cycle1_label.config(text=f"1 cycle alarm time (+91m): {new_time5.strftime('%H:%M')}")
    cycle2_label.config(text=f"2 cycle alarm time (+185m): {new_time6.strftime('%H:%M')}")
    cycle3_label.config(text=f"3 cycle alarm time (+302m): {new_time7.strftime('%H:%M')}")
    cycle4_label.config(text=f"4 cycle alarm time (+392m): {new_time8.strftime('%H:%M')}")
    cycle5_label.config(text=f"5 cycle alarm time (+470m): {new_time9.strftime('%H:%M')}")

#
try:
    sr_today = sun.get_local_sunrise_time(today)
    ss_today = sun.get_local_sunset_time(today)
    if now < sr_today:
        next_event = f"Next event is Sunrise today at {sunrise_today}"
    elif now < ss_today:
        next_event = f"Next event is Sunset today at {sunset_today}"
    else:
        sr_tomorrow = sun.get_local_sunrise_time(tomorrow)
        next_event = f"Next event is Sunrise tomorrow at {sunrise_tomorrow}"

#Window creation retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Background color retrieved from https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python
#Winow geometry retrieved from https://stackoverflow.com/questions/68240695/how-to-change-the-window-size-after-the-program-starts
root = tk.Tk()
root.title("(:")
root.configure(background='#CFE8CC')
root.geometry("230x348")
root.minsize(230, 348)
root.maxsize(1920, 1080)

#Custom time input label retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Entry field retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Vertical center aligning text retrieved from https://stackoverflow.com/questions/68148478/how-to-vertically-center-a-text-label-in-tkinter
#Label background color configuration retrieved from https://www.reddit.com/r/learnpython/comments/11dh1t0/comment/ja8n62f/
#Custom time definition retrieved from ChatGPT
#Button retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
custom_entry_label = tk.Label(root, text="Set Custom Time (HH:MM):")
custom_entry_label.pack(expand=True)
custom_entry_label.configure(bg="#CFE8CC")
entry_field = tk.Entry(root)
entry_field.pack(expand=True)
def use_custom_time():
    custom_time=entry_field.get()
    try:
        update_times(custom_time)
    except ValueError:
        current_time_label.config(text="Invalid time format! Use HH:MM.")
custom_button = tk.Button(root, text="Use Custom Time", command=use_custom_time)
custom_button.pack(expand=True)

#Labels to show times retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Vertical center aligning text retrieved from https://stackoverflow.com/questions/68148478/how-to-vertically-center-a-text-label-in-tkinter
#Label background color configuration retrieved from https://www.reddit.com/r/learnpython/comments/11dh1t0/comment/ja8n62f/
current_time_label = tk.Label(root, text="Current Time: ")
current_time_label.pack(expand=True)
current_time_label.configure(bg="#CFE8CC")

us_nap_label = tk.Label(root, text="Ultra short nap alarm time (+6m): ")
us_nap_label.pack(expand=True)
us_nap_label.configure(bg="#CFE8CC")

short_nap_label = tk.Label(root, text="Short nap alarm time (+11m): ")
short_nap_label.pack(expand=True)
short_nap_label.configure(bg="#CFE8CC")

power_nap_label = tk.Label(root, text="Power nap alarm time (+21m): ")
power_nap_label.pack(expand=True)
power_nap_label.configure(bg="#CFE8CC")

longer_nap_label = tk.Label(root, text="Longer nap alarm time (+61m): ")
longer_nap_label.pack(expand=True)
longer_nap_label.configure(bg="#CFE8CC")

ss_label = tk.Label(root, text="Next sunset time: ")
ss_label.pack(expand=True)
ss_label.configure(bg="#CFE8CC")

sr_label = tk.Label(root, text="Next sunrise time: ")
sr_label.pack(expand=True)
sr_label.configure(bg="#CFE8CC")

cycle1_label = tk.Label(root, text="1 cycle alarm time  (+91m): ")
cycle1_label.pack(expand=True)
cycle1_label.configure(bg="#CFE8CC")

cycle2_label = tk.Label(root, text="2 cycle alarm time (+185m): ")
cycle2_label.pack(expand=True)
cycle2_label.configure(bg="#CFE8CC")

cycle3_label = tk.Label(root, text="3 cycle alarm time (+302m): ")
cycle3_label.pack(expand=True)
cycle3_label.configure(bg="#CFE8CC")

cycle4_label = tk.Label(root, text="4 cycle alarm time (+392m): ")
cycle4_label.pack(expand=True)
cycle4_label.configure(bg="#CFE8CC")

cycle5_label = tk.Label(root, text="5 cycle alarm time (+470m): ")
cycle5_label.pack(expand=True)
cycle5_label.configure(bg="#CFE8CC")

#Refresh button & keybinds
#Button retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
#Keybinds retrieved from https://www.geeksforgeeks.org/python-binding-function-in-tkinter/
def close_ui(event=None):
    root.quit()
refresh_button = tk.Button(root, text="Refresh/Reset", command=update_times)
refresh_button.pack()
root.bind("<F5>", lambda event: update_times())
root.bind("<r>", lambda event: update_times())
root.bind("<Escape>", close_ui)
root.bind("<x>", close_ui)

#Start UI & show times retrieved from https://www.programiz.com/python-programming/datetime/current-time
update_times()

#Setting tkinter loop retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
root.mainloop()

What's the issue here?

Output 2:
The main issue in the provided code is related to how the sunrise_today, sunset_today, sr_today, and ss_today variables are being used and updated within the update_times function and the try block. Specifically:

    sunrise_today and sunset_today are not defined: These variables (sunrise_today, sunset_today) are used in the try block, but they are not declared or assigned values anywhere in your code. You likely meant to use sr_today and ss_today instead.

    Accessing current time outside update_times(): The now variable, which holds the current time, is missing in the try block. You need to get the current time inside the update_times() function (or outside it, if reused).

    Next sunrise/sunset calculation needs adjustment: The try block logic for calculating the next sunrise/sunset appears outside of the update_times() function but is dependent on the now variable, which is only defined in update_times().

Here’s how you can fix these issues:

    Move the sunrise/sunset logic into update_times().
    Replace sunrise_today and sunset_today with sr_today and ss_today.
    Ensure now is defined when calculating the next event.

Corrected code:

from datetime import date, datetime, timedelta
import tkinter as tk
from tkinter import *
import geocoder
from suntime import Sun, SunTimeException

# Function to get current GPS coordinates
def get_current_gps_coordinates():
    g = geocoder.ip('me')
    if g.latlng is not None:
        return g.latlng
    else:
        return None

if __name__ == "__main__":
    coordinates = get_current_gps_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates

# Initialize Sun object with latitude and longitude
sun = Sun(latitude, longitude)

# Today's and tomorrow's date
today = date.today()
tomorrow = today + timedelta(days=1)

# Function to update times and show the results
def update_times(custom_time=None):
    if custom_time:
        timeNow = datetime.strptime(custom_time, '%H:%M')
    else:
        timeNow = datetime.now()

    currentTime = timeNow.strftime('%H:%M')

    # Calculate sunrise and sunset times
    sr_today = sun.get_local_sunrise_time(today)
    ss_today = sun.get_local_sunset_time(today)

    # Determine next sunrise/sunset
    if timeNow < sr_today:
        next_sr_time = sr_today
    else:
        next_sr_time = sun.get_local_sunrise_time(tomorrow)

    if timeNow < ss_today:
        next_ss_time = ss_today
    else:
        next_ss_time = sun.get_local_sunset_time(tomorrow)

    # Math to add time for nap and cycle alarms
    time_change1 = timedelta(minutes=6)
    time_change2 = timedelta(minutes=11)
    time_change3 = timedelta(minutes=21)
    time_change4 = timedelta(minutes=61)
    time_change5 = timedelta(minutes=91)
    time_change6 = timedelta(minutes=185)
    time_change7 = timedelta(minutes=302)
    time_change8 = timedelta(minutes=392)
    time_change9 = timedelta(minutes=470)
    
    new_time1 = timeNow + time_change1
    new_time2 = timeNow + time_change2
    new_time3 = timeNow + time_change3
    new_time4 = timeNow + time_change4
    new_time5 = timeNow + time_change5
    new_time6 = timeNow + time_change6
    new_time7 = timeNow + time_change7
    new_time8 = timeNow + time_change8
    new_time9 = timeNow + time_change9

    # Update labels with current times
    current_time_label.config(text=f"Current Time: {currentTime}")
    us_nap_label.config(text=f"Ultra short nap alarm time (+6m): {new_time1.strftime('%H:%M')}")
    short_nap_label.config(text=f"Short nap alarm time (+11m): {new_time2.strftime('%H:%M')}")
    power_nap_label.config(text=f"Power nap alarm time (+21m): {new_time3.strftime('%H:%M')}")
    longer_nap_label.config(text=f"Longer nap alarm time (+61m): {new_time4.strftime('%H:%M')}")
    ss_label.config(text=f"Next sunset time: {next_ss_time.strftime('%H:%M')}")
    sr_label.config(text=f"Next sunrise time: {next_sr_time.strftime('%H:%M')}")
    cycle1_label.config(text=f"1 cycle alarm time (+91m): {new_time5.strftime('%H:%M')}")
    cycle2_label.config(text=f"2 cycle alarm time (+185m): {new_time6.strftime('%H:%M')}")
    cycle3_label.config(text=f"3 cycle alarm time (+302m): {new_time7.strftime('%H:%M')}")
    cycle4_label.config(text=f"4 cycle alarm time (+392m): {new_time8.strftime('%H:%M')}")
    cycle5_label.config(text=f"5 cycle alarm time (+470m): {new_time9.strftime('%H:%M')}")

# Setup the UI
root = tk.Tk()
root.title("Nap and Sleep Timer")
root.configure(background='#CFE8CC')
root.geometry("230x348")
root.minsize(230, 348)
root.maxsize(1920, 1080)

# Custom time input
custom_entry_label = tk.Label(root, text="Set Custom Time (HH:MM):")
custom_entry_label.pack(expand=True)
custom_entry_label.configure(bg="#CFE8CC")
entry_field = tk.Entry(root)
entry_field.pack(expand=True)

def use_custom_time():
    custom_time = entry_field.get()
    try:
        update_times(custom_time)
    except ValueError:
        current_time_label.config(text="Invalid time format! Use HH:MM.")

custom_button = tk.Button(root, text="Use Custom Time", command=use_custom_time)
custom_button.pack(expand=True)

# Labels to show times
current_time_label = tk.Label(root, text="Current Time: ")
current_time_label.pack(expand=True)
current_time_label.configure(bg="#CFE8CC")

us_nap_label = tk.Label(root, text="Ultra short nap alarm time (+6m): ")
us_nap_label.pack(expand=True)
us_nap_label.configure(bg="#CFE8CC")

short_nap_label = tk.Label(root, text="Short nap alarm time (+11m): ")
short_nap_label.pack(expand=True)
short_nap_label.configure(bg="#CFE8CC")

power_nap_label = tk.Label(root, text="Power nap alarm time (+21m): ")
power_nap_label.pack(expand=True)
power_nap_label.configure(bg="#CFE8CC")

longer_nap_label = tk.Label(root, text="Longer nap alarm time (+61m): ")
longer_nap_label.pack(expand=True)
longer_nap_label.configure(bg="#CFE8CC")

ss_label = tk.Label(root, text="Next sunset time: ")
ss_label.pack(expand=True)
ss_label.configure(bg="#CFE8CC")

sr_label = tk.Label(root, text="Next sunrise time: ")
sr_label.pack(expand=True)
sr_label.configure(bg="#CFE8CC")

cycle1_label = tk.Label(root, text="1 cycle alarm time (+91m): ")
cycle1_label.pack(expand=True)
cycle1_label.configure(bg="#CFE8CC")

cycle2_label = tk.Label(root, text="2 cycle alarm time (+185m): ")
cycle2_label.pack(expand=True)
cycle2_label.configure(bg="#CFE8CC")

cycle3_label = tk.Label(root, text="3 cycle alarm time (+302m): ")
cycle3_label.pack(expand=True)
cycle3_label.configure(bg="#CFE8CC")

cycle4_label = tk.Label(root, text="4 cycle alarm time (+392m): ")
cycle4_label.pack(expand=True)
cycle4_label.configure(bg="#CFE8CC")

cycle5_label = tk.Label(root, text="5 cycle alarm time (+470m): ")
cycle5_label.pack(expand=True)
cycle5_label.configure(bg="#CFE8CC")

# Refresh button & keybinds
def close_ui(event=None):
    root.quit()

refresh_button = tk.Button(root, text="Refresh/Reset", command=update_times)
refresh_button.pack()

root.bind("<F5>", lambda event: update_times())
root.bind("<r>", lambda event: update_times())
root.bind("<Escape>", close_ui)
root.bind("<x>", close_ui)

# Start UI and show times
update_times()
root.mainloop()

Changes:

    sunrise_today and sunset_today: Replaced with sr_today and ss_today.
    now variable: The current time (timeNow) is now consistently defined inside update_times().
    Sunrise and sunset calculation: The code now correctly calculates the next sunrise/sunset based on the current time.

This should fix the issues and allow the GUI to work as intended.

## Contact
Created by Hoi Wai Tang - Hoi.W.Tang@student.uts.edu.au
