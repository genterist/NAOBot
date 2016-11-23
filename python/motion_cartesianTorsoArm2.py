#-*- coding: iso-8859-15 -*-

''' Cartesian control: Multiple Effector Trajectories '''

import config
import motion

def main():
    ''' Move the torso and keep arms fixed in nao space
    Warning: Needs a PoseInit before executing
    Example available: path/to/aldebaran-sdk/modules/src/examples/
                       python/motion_cartesianTorsoArm2.py
    '''

    proxy = config.loadProxy("ALMotion")

    #Set NAO in stiffness On
    config.StiffnessOn(proxy)

    # send robot to Pose Init
    config.PoseInit(proxy)

    space      = motion.SPACE_NAO
    coef       = 1.0                   # Speed motion
    times      = [coef, 2.0*coef, 3.0*coef, 4.0*coef] # seconds
    isAbsolute = False

    dx         = 0.04                  # translation axis X (meters)
    dy         = 0.04                  # translation axis Y (meters)

    # Motion of the Torso
    effector   = "Torso"
    path       = [
      [ 0.0, +dy, 0.0, 0.0, 0.0, 0.0], # Point 1
      [ -dx, 0.0, 0.0, 0.0, 0.0, 0.0], # Point 2
      [ 0.0, -dy, 0.0, 0.0, 0.0, 0.0], # Point 3
      [ 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]] # Point 4
    axisMask   = 63                    # control all the effector axis

    # Using 'post' makes this command execute in a another thread
    proxy.post.positionInterpolation(effector, space, path,
                                     axisMask, times, isAbsolute)

    # Motion of Arms
    axisMask   = 7                     # control the position
    time       = 4.0*coef              # seconds
    # Arms have a null relative motion during all the torso motion
    path       = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # Point 1

    # Motion of Right Arm
    effector   = "RArm"
    proxy.post.positionInterpolation(effector, space, path,
                                     axisMask, time, isAbsolute)

    # Motion of Left Arm
    effector   = "LArm"
    proxy.positionInterpolation(effector, space, path,
                                axisMask, time, isAbsolute)

if __name__ == "__main__":
    main()
