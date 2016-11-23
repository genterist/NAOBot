#-*- coding: iso-8859-15 -*-

''' Cartesian control: Arm trajectory example '''

import config
import motion

def main():
    ''' Example showing a path of two positions
    Warning: Needs a PoseInit before executing
    Example available: path/to/aldebaran-sdk/modules/src/examples/
                       python/motion_cartesianArm1.py
    '''

    proxy = config.loadProxy("ALMotion")

    #Set NAO in stiffness On
    config.StiffnessOn(proxy)

    # send robot to Pose Init
    config.PoseInit(proxy)

    effector   = "LArm"
    space      = motion.SPACE_NAO
    axisMask   = 7          # just control position
    isAbsolute = False

    # Since we are in relative, the current position is zero
    currentPos = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # define the changes relative to the current position
    dx         =  0.06      # translation axis X (meters)
    dy         =  0.06      # translation axis Y (meters)
    dz         =  0.00      # translation axis Z (meters)
    dwx        =  0.00      # rotation axis X (radians)
    dwy        =  0.00      # rotation axis Y (radians)
    dwz        =  0.00      # rotation axis Z (radians)
    targetPos  = [dx, dy, dz, dwx, dwy, dwz]

    # go to the target and back again
    path       = [targetPos, currentPos]
    times      = [2.0, 4.0] # seconds

    proxy.positionInterpolation(effector, space, path,
                                axisMask, times, isAbsolute)

if __name__ == "__main__":
    main()
