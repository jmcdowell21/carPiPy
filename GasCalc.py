import time
import random
from tkinter import *

def getStartVariables():
  """Get the starting fuel and mileage variables"""
  fuelStart = float(19.0)  # percentage of tank
  mileageStart = float(134004) # odometer reading

  #fuelStart = carMaxFuelGallons * fuelStart
  return fuelStart, mileageStart

def getEndVariables():
  """Get the ending fuel and mileage variables"""
  fuelEnd = float()  # percentage of tank
  mileageEnd = float() # odometer reading

  #fuelEnd = carMaxFuelGallons * fuelEnd
  return fuelEnd, mileageEnd

def calculateMPG(carVars):
  """Calculate MPG from carVars dictionary"""
  fuelConsumed = carVars['fuelStart'] - carVars['fuelEnd']
  milesDriven = carVars['mileageStart'] - carVars['mileageEnd']
  mpg = milesDriven / fuelConsumed
  return mpg

def endLoop():
  runLoop = False
  return runLoop

# Establish constants
carMaxFuelGallons = 19.0  # gallons

runLoop = True

while runLoop == True:

  """Get start variables from OBD2"""
  fuelStart, mileageStart = getStartVariables()

  """Wait 10 seconds"""
  time.sleep(10)

  """Get end variables from OBD2"""
  fuelEnd, mileageEnd = getEndVariables()

  carVars = {
      'fuelStart': fuelStart,
      'fuelEnd': fuelEnd,
      'mileageStart': mileageStart,
      'mileageEnd': mileageEnd
  }

  mpg = calculateMPG(carVars)

  root = Tk()

  button = Button(root, text="Stop", command=endLoop)
  button.pack()

  root.mainloop()
