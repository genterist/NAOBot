# This test demonstrates how to use the ALVisionRecognition module.
# Note that you might not have this module depending on your distribution.
#
# - We first instantiate a proxy to the ALVisionRecognition module
#     Note that this module should be loaded on the robot's NaoQi.
#     The module output its results in ALMemory in a variable
#     called "PictureRecognized".

# - We then read this AlMemory value and check whether we get
#   interesting things.


import os
import sys
import time

import naoqi
from naoqi import *

count = 10
period = 500
moduleName = "pythonModule"
NAO_IP = "10.0.252.124"  # Replace here with your robot's IP address
PC_IP = "10.0.252.130" # Replace here with your computer IP address
PORT = 9559
memValue = "PictureDetected" # ALMemory variable where the ALVisionRecognition module outputs its results.


# create python module
class myModule(ALModule):
  """python class myModule test auto documentation"""

  def pictureChanged(self, strVarName, value, strMessage):
    """callback when data change"""
    print "datachanged", strVarName, " ", value, " ", strMessage
    global count
    count = count-1

broker = ALBroker("pythonBroker", PC_IP,9999, NAO_IP,9559)
pythonModule = myModule(moduleName)


# Create a proxy to ALVisionRecognition
try:
  recoProxy = ALProxy("ALVisionRecognition", NAO_IP, PORT)
except RuntimeError,e:
  print "Error when creating ALVisionRecognition proxy:"
  exit(1)

# Load ALVisionRecognition database
# Database files (database.ar1,.ar2,etc. have to be in
# /home/nao/naoqi/data/visionrecognition
try:
  recoProxy.load()
except RuntimeError,e:
  print "Error when loading ALVisionRecognition database"
  exit(1)


# Subscribe to the ALVisionRecognition proxy
# This means that the module will write in memValue with the given period below.
try:
  recoProxy.subscribe(moduleName, period, 0.0 )
except RuntimeError,e:
  print "Error when subscribing to ALVisionRecognition"
  exit(1)


# Create a proxy to ALMemory
try:
  memoryProxy = ALProxy("ALMemory", NAO_IP, PORT)
except RuntimeError,e:
  print "Error when creating ALMemory proxy:"
  exit(1)


# Have the python module called back when picture recognition results change.
try:
  memoryProxy.subscribeToMicroEvent(memValue, moduleName, "", "pictureChanged")
except RuntimeError,e:
  print "Error when subscribing to micro event"
  exit(1)


# Let the picture recognition run for a little while.
while count>0:
  time.sleep(1)


# unsubscribe modules
memoryProxy.unsubscribeToMicroEvent(memValue, moduleName)
recoProxy.unsubscribe(moduleName)


print 'end of vision_recognition python script'

