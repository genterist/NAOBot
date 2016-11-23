#-*- coding: iso-8859-15 -*-

''' Cartesian control: Torso and Foot trajectories '''

import config
import motion

def main():
    ''' Example of a cartesian foot trajectory
    Warning: Needs a PoseInit before executing
    Example available: path/to/aldebaran-sdk/modules/src/examples/
                       python/motion_cartesianFoot.py
    '''

    proxy = config.loadProxy("ALMotion")

    #Set NAO in stiffness On
    config.StiffnessOn(proxy)

    # send robot to Pose Init
    config.PoseInit(proxy)

    space      =  motion.SPACE_NAO
    axisMask   = 63                     # control all the effector's axes
    isAbsolute = False

    # Lower the Torso and move to the side
    effector   = "Torso"
    path       = [0.0, -0.07, -0.03, 0.0, 0.0, 0.0]
    time       = 2.0                    # seconds
    proxy.positionInterpolation(effector, space, path,
                                axisMask, time, isAbsolute)

    # LLeg motion
    effector   = "LLeg"
    path       = [0.0,  0.06,  0.00, 0.0, 0.0, 0.8]
    times      = 2.0            # seconds

    proxy.positionInterpolation(effector, space, path,
                                axisMask, times, isAbsolute)

if __name__ == "__main__":
    main()
