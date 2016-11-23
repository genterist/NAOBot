"""
PoseZero

Set all the motors of the body to zero.

"""
import config
proxy = config.loadProxy("ALMotion")

#Get the Number of Joints
numJoints = len(proxy.getJointNames("Body"))

#We use the "Body" name to signify the collection of all joints
pNames = "Body"
#We prepare a collection of floats
pTargetAngles = [0.0] * numJoints
#We set the fraction of max speed
pMaxSpeedFraction = 0.3
#Ask motion to do this with a blocking call
proxy.angleInterpolationWithSpeed(pNames, pTargetAngles, pMaxSpeedFraction)
