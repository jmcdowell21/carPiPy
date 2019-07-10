#!/usr/bin/env python

import tkinter as tk
import time
import random
import sys

top = tk.Tk()
top.geometry("480x320")

fuelStart = 19.0
mileageStart = 134903.2

loopCount = 1
loopRun = True

def calculateMPG(fuelStart, mileageStart):
  """ Calcualte MPG from travelVars dictionary """
  mileageEnd = mileageStart + random.uniform(20,30)
  mileageChange = mileageEnd - mileageStart

  mpg = random.uniform(17, 20)

  fuelChange = mileageChange / mpg
  fuelEnd = fuelStart - fuelChange

  return mpg, fuelEnd, mileageEnd

def calculateMilesToEmpty(mpg, fuelLevel):
  milesToEmpty = mpg * fuelLevel
  return milesToEmpty

def close_window():
  top.destroy()

while loopRun == True:
  if loopCount <= 0:
    tk_mpg.pack_forget()
    tk_fuelLevel.pack_forget()
    tk_mileage.pack_forget()
    tk_hr.pack_forget()
    tk_mteTitle.pack_forget()
    tk_milesToEmpty.pack_forget()

  if fuelStart < 0:
    tk_mpg.pack_forget()
    tk_fuelLevel.pack_forget()
    tk_mileage.pack_forget()
    tk_hr.pack_forget()
    tk_mteTitle.pack_forget()
    tk_milesToEmpty.pack_forget()

    exitMessage = tk.Label(top, text="You're out of gas, dipshit.")
    exitButton = tk.Button(top, text="Exit", command=close_window)
    exitMessage.pack()
    exitButton.pack()
    top.update()
    time.sleep(5)
    close_window()
    break

  mpg, fuelEnd, mileageEnd = calculateMPG(fuelStart, mileageStart)

  fuelStart = fuelEnd
  mileageStart = mileageEnd

  milesToEmpty = calculateMilesToEmpty(mpg, fuelStart)

  p_mpg = 'MPG: ' + '{0:.2f}'.format(mpg)
  tk_mpg = tk.Label(top, text=p_mpg)

  p_fuelLevel = 'Fuel Level: ' + '{0:.2f}'.format(fuelStart)
  tk_fuelLevel = tk.Label(top, text=p_fuelLevel)

  p_mileage = 'Mileage: ' + '{0:.2f}'.format(mileageStart)
  tk_mileage = tk.Label(top, text=p_mileage)

  p_hr = '-' * 150
  tk_hr = tk.Label(top, text=p_hr)

  tk_mteTitle = tk.Label(top, text='Miles To Empty:', font=(16))

  p_milesToEmpty = '{0:.2f}'.format(milesToEmpty)
  tk_milesToEmpty = tk.Label(top, text=p_milesToEmpty, font=(20))

  loopCount -= 1

  tk_mpg.pack()
  tk_fuelLevel.pack()
  tk_mileage.pack()
  tk_hr.pack()
  tk_mteTitle.pack()
  tk_milesToEmpty.pack()
  top.update()
  time.sleep(1)

top.mainloop()
