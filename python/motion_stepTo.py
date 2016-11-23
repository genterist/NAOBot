"""
Step To

Small example to make Nao one Step

"""
import time
import config
motionProxy = config.loadProxy("ALMotion")

#Set NAO in stiffness On
config.StiffnessOn(motionProxy)

# send robot to Pose Init
config.PoseInit(motionProxy)

#####################
## Enable arms control by Walk algorithm
#####################
motionProxy.setWalkArmsEnable(False, False)

#STEPTO
Leg = "RLeg"
X = 0.04
Y = -0.02
Theta = -0.3
motionProxy.stepTo(Leg, X, Y, Theta)
motionProxy.waitUntilWalkIsFinished()

#~ #STEPTO
Leg = "RLeg"
X = 0.00
Y = 0.00
Theta = 0.00
motionProxy.stepTo(Leg, X, Y, Theta)
