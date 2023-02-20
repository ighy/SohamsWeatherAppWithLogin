#Created by: Soham Jani, February 19, 2023

##username: username0405
##password: password0504

def Mains():
    key = '3c08649eb63b30c80da09801fa1025bc'
    




    win = Tk()
    def submitFunc():
        
        dispWin = Tk()

        city = str(cityEntry.get())

        country = str(countyEntry.get())

        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city},{country}&units=imperial&appid=edc5e652d7983cdcf71c6c5c5b546612')

        rj = r.json()
        rjm = rj['main']
        wrjm = rj['weather']
        wwrjm = wrjm[0]
        typeshi = wwrjm['description']
        print(typeshi)
        temp = rjm['temp']
        feels = rjm['feels_like']
        min = rjm['temp_min']
        max = rjm['temp_max']
        humid = rjm['humidity']
        
        dispLabelCity = Label(dispWin,text=f"Weather for {city.upper()}, {country.upper()}: ",font=('Helvetica',32),fg='white').grid(row=0,column=1)
        dispLabelTemp = Label(dispWin,text=f"{temp} ℉",font = ('helvetica',45),fg='white').grid(row=1,column=1)
        tempinCel = (float(temp)-32)*(5/9)
        tempinCel = int(tempinCel)
        tempInC = Label(dispWin,text=f'{tempinCel} °C',font = 'helvetica 40',fg='gray').grid(row=2,column=1)
        dispLabelFeels = Label(dispWin,text=f' Feels Like: {feels} °F',font = 'joker 20').grid(row=5,column=1)
        dispLabelMinMax = Label(dispWin,text=f'Min: {min} °F, Max: {max} °F',font = 'helvetica 20').grid(row=3,column = 1)
        dispLabelDesc = Label(dispWin,text=f'{str(typeshi).upper()}',font = 'helvetica 15').grid(row=4,column=1)






    title = Label(win,text="Weather App",font=('Helvetica',32)).grid(row = 0,column = 1)
    cityLbl = Label(win,text='Enter city',font=('Helvetica',20)).grid(row=1,column = 0)
    countryLbl = Label(win,text='Country',font=('Helvetica',20)).grid(row=1,column = 2)
    cityEntry = Entry(win,bg='black')
    cityEntry.grid(row=2,column=0)
    countyEntry = Entry(win,bg='black')
    countyEntry.grid(row=2,column =2)

    submitButton = Button(win,text='SUBMIT',command=submitFunc).grid(row=4,column=1)


    win.mainloop()

import requests,time

from tkinter import *
from ast import main
from tkinter import *

mainwin = Tk()

title = Label(mainwin,text = "Login to Access Weather App",fg='red',bg='black',font=("helvetica",30)).grid(row=0,column=1)
usernameLabel = Label(mainwin,text="Enter your username: ").grid(row=1, column=1)
passLabel = Label(mainwin,text="Enter your password: ").grid(row=2,column=1)
userEntry = Entry(mainwin)
passEntry = Entry(mainwin)
userEntry.grid(row=1,column=2)
passEntry.grid(row=2,column=2)
def submitFunc():
    username = 'username0405'
    password = 'password0504'
    userInput = userEntry.get()
    passInput=passEntry.get()
    if userEntry.get()==username and passEntry.get()==password:
        Mains()
        mainwin.destroy()
    else:
        print('Invalid, try again.')
submitButton = Button(mainwin,text='Submit',command=submitFunc).grid(row=3,column=1)






mainwin.mainloop()
