from tkinter import *
from time import *

hari_dict = {
    "Monday": "Senin",
    "Tuesday": "Selasa",
    "Wednesday": "Rabu",
    "Thursday": "Kamis",
    "Friday": "Jumat",
    "Saturday": "Sabtu",
    "Sunday": "Minggu"
}

bulan_dict = {
    "January": "Januari",
    "February": "Februari",
    "March": "Maret",
    "April": "April",
    "May": "Mei",
    "June": "Juni",
    "July": "Juli",
    "August": "Agustus",
    "September": "September",
    "October": "Oktober",
    "November": "November",
    "December": "Desember"
}

def update():
    time_string = strftime("%H:%M:%S")
    time_label.config(text=time_string)
    
    hari = strftime("%A")
    bulan = strftime("%B")
    day_string = hari_dict[hari] + " " + bulan_dict[bulan] +" " + strftime("%d, %Y")
    day_label.config(text=day_string)
    
    window.after(1000, update)

window = Tk()
window.title("Clock Program")
window.resizable(False, False)

icon = PhotoImage(file='jam.png')
window.iconphoto(True, icon)

time_label = Label(window, font=("Arial", 50), fg="Black")
time_label.pack()
day_label = Label(window, font=("Arial", 20), fg="Black")
day_label.pack()

update()

window.mainloop()