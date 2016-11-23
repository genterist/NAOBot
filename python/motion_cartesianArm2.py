#-*- coding: iso-8859-15 -*-

''' Cartesian control: Arm trajectory example '''

import config
import motion

def main():
    ''' Example showing a hand ellipsoid
    Warning: Needs a PoseInit before executing
    Example available: path/to/aldebaran-sdk/modules/src/examples/
                       python/motion_cartesianArm2.py
    '''

    proxy = config.loadProxy("ALMotion")

    #Set NAO in stiffness On
    config.StiffnessOn(proxy)

    # send robot to Pose Init
    config.PoseInit(proxy)

    effector   = "LArm"
    space      = motion.SPACE_NAO
    path       = [
     [0.0, -0.02, +0.00, 0.0, 0.0, 0.0],        # Point 1
     [0.0, +0.00, +0.01, 0.0, 0.0, 0.0],        # Point 2
     [0.0, +0.08, +0.00, 0.0, 0.0, 0.0],        # Point 3
     [0.0, +0.00, -0.04, 0.0, 0.0, 0.0],        # Point 4
     [0.0, -0.02, +0.00, 0.0, 0.0, 0.0],        # Point 5
     [0.0, +0.00, +0.00, 0.0, 0.0, 0.0]]        # Point 6
    axisMask   = 7                              # just control position
    times      = [0.5, 1.0, 2.0, 3.0, 4.0, 4.5] # seconds
    isAbsolute = False
    proxy.positionInterpolation(effector, space, path,
                                axisMask, times, isAbsolute)

if __name__ == "__main__":
    main()
