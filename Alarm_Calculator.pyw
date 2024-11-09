#datetime import retrieved from https://stackoverflow.com/questions/68632685/alarm-clock-in-python
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

#Next SunTime calculation retrieved from ChatGPT
today = date.today()
tomorrow = today + timedelta(days=1)

#Defining function to update & show times retrieved from https://www.programiz.com/python-programming/datetime/current-time
#Custom time feature retrieved from ChatGPT
#Next SunTime calculation retrieved from ChatGPT
def update_times(custom_time=None):
    if custom_time:
        timeNow = datetime.strptime(custom_time,'%H:%M')
    else:
        timeNow = datetime.now()
    
    currentTime = timeNow.strftime('%H:%M')

    sr_today = sun.get_local_sunrise_time(today)
    ss_today = sun.get_local_sunset_time(today)
    if timeNow < sr_today:
        next_sr_time = sr_today
    else:
        next_sr_time = sun.get_local_sunrise_time(tomorrow)
    if timeNow < ss_today:
        next_ss_time = ss_today
    else:
        next_ss_time = sun.get_local_sunset_time(tomorrow)

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
    ss_label.config(text=f"Next sunset time: {next_ss_time.strftime('%H:%M')}")
    sr_label.config(text=f"Next sunrise time: {next_sr_time.strftime('%H:%M')}")
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
root.geometry("480x350")
root.minsize(480, 350)
root.maxsize(2560, 1440)

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
ss_label.configure(bg="#FFD700")

sr_label = tk.Label(root, text="Next sunrise time: ")
sr_label.pack(expand=True)
sr_label.configure(bg="#FFD700")

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
root.bind("<space>", lambda event: update_times())
root.bind("<Escape>", close_ui)
root.bind("<x>", close_ui)

#Resizing text retrieved from https://www.geeksforgeeks.org/how-to-dynamically-resize-button-text-in-tkinter/
#Resizing entry field retrieved from https://www.tutorialspoint.com/how-to-resize-an-entry-box-by-height-in-tkinter
def resize(e):
    
    size = e.width/10

    if e.height < 1100 and e.height > 1000:
        custom_entry_label.config(font = ("Helvetica", 22))
        entry_field.config(font = ("Helvetica", 22))
        custom_button.config(font = ("Helvetica", 22))
        current_time_label.config(font = ("Helvetica", 22))
        us_nap_label.config(font = ("Helvetica", 22))
        short_nap_label.config(font = ("Helvetica", 22))
        power_nap_label.config(font = ("Helvetica", 22))
        longer_nap_label.config(font = ("Helvetica", 22))
        ss_label.config(font = ("Helvetica", 22))
        sr_label.config(font = ("Helvetica", 22))
        cycle1_label.config(font = ("Helvetica", 22))
        cycle2_label.config(font = ("Helvetica", 22))
        cycle3_label.config(font = ("Helvetica", 22))
        cycle4_label.config(font = ("Helvetica", 22))
        cycle5_label.config(font = ("Helvetica", 22))
        refresh_button.config(font = ("Helvetica", 22))
    if e.height < 1000 and e.height > 900:
        custom_entry_label.config(font = ("Helvetica", 20))
        entry_field.config(font = ("Helvetica", 20))
        custom_button.config(font = ("Helvetica", 20))
        current_time_label.config(font = ("Helvetica", 20))
        us_nap_label.config(font = ("Helvetica", 20))
        short_nap_label.config(font = ("Helvetica", 20))
        power_nap_label.config(font = ("Helvetica", 20))
        longer_nap_label.config(font = ("Helvetica", 20))
        ss_label.config(font = ("Helvetica", 20))
        sr_label.config(font = ("Helvetica", 20))
        cycle1_label.config(font = ("Helvetica", 20))
        cycle2_label.config(font = ("Helvetica", 20))
        cycle3_label.config(font = ("Helvetica", 20))
        cycle4_label.config(font = ("Helvetica", 20))
        cycle5_label.config(font = ("Helvetica", 20))
        refresh_button.config(font = ("Helvetica", 20))
    if e.height < 900 and e.height > 800:
        custom_entry_label.config(font = ("Helvetica", 18))
        entry_field.config(font = ("Helvetica", 18))
        custom_button.config(font = ("Helvetica", 18))
        current_time_label.config(font = ("Helvetica", 18))
        us_nap_label.config(font = ("Helvetica", 18))
        short_nap_label.config(font = ("Helvetica", 18))
        power_nap_label.config(font = ("Helvetica", 18))
        longer_nap_label.config(font = ("Helvetica", 18))
        ss_label.config(font = ("Helvetica", 18))
        sr_label.config(font = ("Helvetica", 18))
        cycle1_label.config(font = ("Helvetica", 18))
        cycle2_label.config(font = ("Helvetica", 18))
        cycle3_label.config(font = ("Helvetica", 18))
        cycle4_label.config(font = ("Helvetica", 18))
        cycle5_label.config(font = ("Helvetica", 18))
        refresh_button.config(font = ("Helvetica", 18))
    if e.height < 800 and e.height > 700:
        custom_entry_label.config(font = ("Helvetica", 16))
        entry_field.config(font = ("Helvetica", 16))
        custom_button.config(font = ("Helvetica", 16))
        current_time_label.config(font = ("Helvetica", 16))
        us_nap_label.config(font = ("Helvetica", 16))
        short_nap_label.config(font = ("Helvetica", 16))
        power_nap_label.config(font = ("Helvetica", 16))
        longer_nap_label.config(font = ("Helvetica", 16))
        ss_label.config(font = ("Helvetica", 16))
        sr_label.config(font = ("Helvetica", 16))
        cycle1_label.config(font = ("Helvetica", 16))
        cycle2_label.config(font = ("Helvetica", 16))
        cycle3_label.config(font = ("Helvetica", 16))
        cycle4_label.config(font = ("Helvetica", 16))
        cycle5_label.config(font = ("Helvetica", 16))
        refresh_button.config(font = ("Helvetica", 16))
    if e.height < 700 and e.height > 600:
        custom_entry_label.config(font = ("Helvetica", 14))
        entry_field.config(font = ("Helvetica", 14))
        custom_button.config(font = ("Helvetica", 14))
        current_time_label.config(font = ("Helvetica", 14))
        us_nap_label.config(font = ("Helvetica", 14))
        short_nap_label.config(font = ("Helvetica", 14))
        power_nap_label.config(font = ("Helvetica", 14))
        longer_nap_label.config(font = ("Helvetica", 14))
        ss_label.config(font = ("Helvetica", 14))
        sr_label.config(font = ("Helvetica", 14))
        cycle1_label.config(font = ("Helvetica", 14))
        cycle2_label.config(font = ("Helvetica", 14))
        cycle3_label.config(font = ("Helvetica", 14))
        cycle4_label.config(font = ("Helvetica", 14))
        cycle5_label.config(font = ("Helvetica", 14))
        refresh_button.config(font = ("Helvetica", 14))
    if e.height < 600 and e.height > 500:
        custom_entry_label.config(font = ("Helvetica", 12))
        entry_field.config(font = ("Helvetica", 12))
        custom_button.config(font = ("Helvetica", 12))
        current_time_label.config(font = ("Helvetica", 12))
        us_nap_label.config(font = ("Helvetica", 12))
        short_nap_label.config(font = ("Helvetica", 12))
        power_nap_label.config(font = ("Helvetica", 12))
        longer_nap_label.config(font = ("Helvetica", 12))
        ss_label.config(font = ("Helvetica", 12))
        sr_label.config(font = ("Helvetica", 12))
        cycle1_label.config(font = ("Helvetica", 12))
        cycle2_label.config(font = ("Helvetica", 12))
        cycle3_label.config(font = ("Helvetica", 12))
        cycle4_label.config(font = ("Helvetica", 12))
        cycle5_label.config(font = ("Helvetica", 12))
        refresh_button.config(font = ("Helvetica", 12))
    elif e.height < 500 and e.height > 400:
        custom_entry_label.config(font = ("Helvetica", 10))
        entry_field.config(font = ("Helvetica", 10))
        custom_button.config(font = ("Helvetica", 10))
        current_time_label.config(font = ("Helvetica", 10))
        us_nap_label.config(font = ("Helvetica", 10))
        short_nap_label.config(font = ("Helvetica", 10))
        power_nap_label.config(font = ("Helvetica", 10))
        longer_nap_label.config(font = ("Helvetica", 10))
        ss_label.config(font = ("Helvetica", 10))
        sr_label.config(font = ("Helvetica", 10))
        cycle1_label.config(font = ("Helvetica", 10))
        cycle2_label.config(font = ("Helvetica", 10))
        cycle3_label.config(font = ("Helvetica", 10))
        cycle4_label.config(font = ("Helvetica", 10))
        cycle5_label.config(font = ("Helvetica", 10))
        refresh_button.config(font = ("Helvetica", 10))
    elif e.height < 400 and e.height >= 348:
        custom_entry_label.config(font = ("Helvetica", 9))
        entry_field.config(font = ("Helvetica", 9))
        custom_button.config(font = ("Helvetica", 9))
        current_time_label.config(font = ("Helvetica", 9))
        us_nap_label.config(font = ("Helvetica", 9))
        short_nap_label.config(font = ("Helvetica", 9))
        power_nap_label.config(font = ("Helvetica", 9))
        longer_nap_label.config(font = ("Helvetica", 9))
        ss_label.config(font = ("Helvetica", 9))
        sr_label.config(font = ("Helvetica", 9))
        cycle1_label.config(font = ("Helvetica", 9))
        cycle2_label.config(font = ("Helvetica", 9))
        cycle3_label.config(font = ("Helvetica", 9))
        cycle4_label.config(font = ("Helvetica", 9))
        cycle5_label.config(font = ("Helvetica", 9))
        refresh_button.config(font = ("Helvetica", 9))

root.bind('<Configure>', resize)

#Start UI & show times retrieved from https://www.programiz.com/python-programming/datetime/current-time
update_times()

#Setting tkinter loop retrieved from https://www.geeksforgeeks.org/python-gui-tkinter/
root.mainloop()
