import os
import sys
import time

from naoqi import ALProxy
from vision_definitions import*

# Replace here with your robot's IP address.
IP = "10.0.252.84"

PORT = 9559

####
# Create proxy on ALVideoDevice

print "Creating ALVideoDevice proxy"

try:
  camProxy = ALProxy("ALVideoDevice", IP, PORT)
except Exception,e:
  print "Error when creating vision proxy:"
  print str(e)
  exit(1)

####
# Register a Generic Video Module

resolution = kQVGA
colorSpace = kYUVColorSpace
fps = 30

nameId = camProxy.subscribe("python_GVM", resolution, colorSpace, fps)
print nameId

print 'getting images in local'
for i in range(0, 20):
  camProxy.getImageLocal(nameId)
  camProxy.releaseImage(nameId)

print 'getting images in local'
for i in range(0, 20):
  camProxy.getImageLocal(nameId)
  camProxy.releaseImage(nameId)

resolution = kQQVGA
camProxy.setResolution(nameId, resolution)

print 'getting images in remote'
for i in range(0, 20):
  camProxy.getImageRemote(nameId)

camProxy.unsubscribe(nameId)

print 'end of gvm_getImageLocal python script'
