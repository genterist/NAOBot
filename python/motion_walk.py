"""
Walk

Small example to make Nao walk

"""
import config
import motion
import time
motionProxy = config.loadProxy("ALMotion")

#Set NAO in stiffness On
config.StiffnessOn(motionProxy)

#####################
## Enable arms control by Walk algorithm
#####################
motionProxy.setWalkArmsEnable(True, True)
#~ motionProxy.setWalkArmsEnable(False, False)

#####################
## FOOT CONTACT PROTECTION
#####################
#~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",False]])
motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",True]])

#TARGET VELOCITY
X = -0.5  #backward
Y = 0.0
Theta = 0.0
Frequency =0.0 #low speed
motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

time.sleep(4.0)

#TARGET VELOCITY
X = 0.8
Y = 0.0
Theta = 0.0
Frequency =1.0 #Max speed
motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

time.sleep(4.0)

#TARGET VELOCITY
X = 0.2
Y = -0.5
Theta = 0.2
Frequency =1.0
motionProxy.setWalkTargetVelocity(X, Y, Theta, Frequency)

time.sleep(2.0)

#####################
## Arms User Motion
#####################

# desactivate Left Arm
motionProxy.setWalkArmsEnable(False, True)

JointNames = ["LShoulderPitch", "LShoulderRoll","LElbowYaw","LElbowRoll"]
Arm1 = [-40,  25, 0, -40]
Arm1 = [ x * motion.TO_RAD for x in Arm1]

Arm2 = [-40,  50, 0, -80]
Arm2 = [ x * motion.TO_RAD for x in Arm2]

motionProxy.angleInterpolationWithSpeed(JointNames,Arm1, 0.6)
motionProxy.angleInterpolationWithSpeed(JointNames,Arm2, 0.6)
motionProxy.angleInterpolationWithSpeed(JointNames,Arm1, 0.6)

# reactivate Left Arm
motionProxy.setWalkArmsEnable(True, True)

time.sleep(2.0)

#####################
## End Walk
#####################
#TARGET VELOCITY
X = 0.0
Y = 0.0
Theta = 0.0
motionProxy.setWalkTargetVelocity(  X, Y, Theta, Frequency)
