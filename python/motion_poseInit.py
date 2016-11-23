"""
PoseInit

Small example to make Nao go to an initial position.
"""

import config
proxy = config.loadProxy("ALMotion")

import time
import motion

# Feel free to experiment with these values
kneeAngle  = 40
torsoAngle =  0
wideAngle  =  0

#----------------------------- prepare the angles ----------------------------
#Get the Number of Joints
NumJoints = len(proxy.getJointNames("Body"))
print NumJoints

# Define The Initial Position
Head     = [0, 0]
LeftArm  = [120,  15, -90, -80]
LeftLeg  = [0,  wideAngle, -kneeAngle/2-torsoAngle, kneeAngle, -kneeAngle/2, -wideAngle]
RightLeg = [0, -wideAngle, -kneeAngle/2-torsoAngle, kneeAngle, -kneeAngle/2,  wideAngle]
RightArm = [120, -15,  90,  80]

# If we have hands, we need to add angles for wrist and open/close hand
if (NumJoints == 26):
    LeftArm  += [0, 0]
    RightArm += [0, 0]

# Gather the joints together
pTargetAngles = Head + LeftArm + LeftLeg + RightLeg + RightArm

# Convert to radians
pTargetAngles = [ x * motion.TO_RAD for x in pTargetAngles]

#------------------------------ send the commands -----------------------------
#We use the "Body" name to signify the collection of all joints
pNames = "Body"
#We set the fraction of max speed
pMaxSpeedFraction = 0.2
#Ask motion to do this with a blocking call
proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)
