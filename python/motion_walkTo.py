"""
Step To

Small example to make Nao one Step

"""
import time
import math
import config
motionProxy = config.loadProxy("ALMotion")

#Set NAO in stiffness On
config.StiffnessOn(motionProxy)

#~ DUBINS_INTERPOLATION = True
DUBINS_INTERPOLATION = False

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

#####################
##get robot position before move
#####################
RobotPositionBeforeCommand  = motionProxy.getRobotPosition(False)
print "ROBOT before : " + str(RobotPositionBeforeCommand)

if (DUBINS_INTERPOLATION):
  X = 0.0
  Y = -0.5
  Theta = 0.0
  motionProxy.walkTo(X, Y, Theta)
  motionProxy.waitUntilWalkIsFinished()
else:
  X = 0.3
  Y = 0.1
  Theta = math.pi/2.0
  motionProxy.walkTo(X, Y, Theta)
  motionProxy.waitUntilWalkIsFinished()

#####################
##get robot position after move
#####################
RobotPositionAfterCommand = motionProxy.getRobotPosition(False)
print "ROBOT after : " + str(RobotPositionAfterCommand)

#####################
##compute robot motion
#####################
RobotMoveCommand = []
RobotMoveCommand.append( (RobotPositionAfterCommand[0] - RobotPositionBeforeCommand[0])*math.cos(RobotPositionBeforeCommand[2]) + (RobotPositionAfterCommand[1] - RobotPositionBeforeCommand[1])* math.sin(RobotPositionBeforeCommand[2]) )
RobotMoveCommand.append( -(RobotPositionAfterCommand[0] - RobotPositionBeforeCommand[0])*math.sin(RobotPositionBeforeCommand[2]) + (RobotPositionAfterCommand[1] - RobotPositionBeforeCommand[1])* math.cos(RobotPositionBeforeCommand[2]) )
RobotMoveCommand.append(RobotPositionAfterCommand[2] - RobotPositionBeforeCommand[2])
print "The Robot Move Command: " + str(RobotMoveCommand)
