# This test demonstrates how to use the ALLogoDetection module.
# Note that you might not have this module depending on your distribution
#
# - We first instantiate a proxy to the ALLogoDetection module
#     Note that this module should be loaded on the robot's naoqi.
#     The module output its results in ALMemory in a variable
#     called "LogoDetected"

# - We then read this AlMemory value and check whether we get
#   interesting things.

import os
import sys
import time

from naoqi import ALProxy
from vision_definitions import*

# Replace here with your robot's IP address.
IP = "10.0.252.84"

PORT = 9559

# Create a proxy to ALLogoDetection
try:
  logoProxy = ALProxy("ALLogoDetection", IP, PORT)
except Exception, e:
  print "Error when creating logo detection proxy:"
  print str(e)
  exit(1)

# ALMemory variable where the ALLogoDetection modules
# outputs its results
memValue = "LogoDetected"

# Subscribe to the ALLogoDetection proxy
# This means that the module will write in memValue with
# the given period below
period = 500
logoProxy.subscribe("Test_Logo", period, 0.0 )


# Create a proxy to ALMemory
try:
  memoryProxy = ALProxy("ALMemory", IP, PORT)
except Exception, e:
  print "Error when creating memory proxy:"
  print str(e)
  exit(1)

print "Creating logo detection proxy"

# A simple loop that reads the memValue and checks whether logos are detected.

for i in range(0, 20):
  time.sleep(0.5)
  val = memoryProxy.getData(memValue)

  print ""
  print "*****"
  print ""

  # Check whether we got a valid output: a list with two fields.
  if(val and isinstance(val, list) and len(val) == 2):

    # We detected logos !
    # For each logo, we can read its shape info and ID.

    # First Field = TimeStamp.
    timeStamp = val[0]

    # Second Field = array of logo_Info's.
    logoInfoArray = val[1]

    try:
      # Browse the logoInfoArray to get info on each detected logo.
      for logoInfo in logoInfoArray:

        # First Field = Shape info.
        logoShapeInfo = logoInfo[0]

        # Second Field = Extra info (empty for now).
        logoExtraInfo = logoInfo[1]

        print "  alpha %.3f - beta %.3f" % (logoShapeInfo[1], logoShapeInfo[2])
        print "  width %.3f - height %.3f" % (logoShapeInfo[3], logoShapeInfo[4])

    except Exception, e:
      print "logos detected, but it seems getData is invalid. ALValue ="
      print val
      print "Error msg %s" % (str(e))
  else:
      print "No logo detected"

# Unsubscribe the module
logoProxy.unsubscribe("Test_Logo")

print "Test terminated successfully"
