#-*- coding: iso-8859-15 -*-

''' Cartesian control: Torso trajectory '''

import config
import motion

def main():
    ''' Example showing a path of five positions
    Warning: Needs a PoseInit before execution
    Example available: path/to/aldebaran-sdk/modules/src/examples/
                       python/motion_cartesianTorso.py
    '''

    proxy = config.loadProxy("ALMotion")

    #Set NAO in stiffness On
    config.StiffnessOn(proxy)

    # send robot to Pose Init
    config.PoseInit(proxy)

    effector   = "Torso"
    space      =  motion.SPACE_NAO

    # Position Only
    axisMask   = 63                             # Full control
    isAbsolute = False

    # define the changes relative to the current position
    dx         = 0.040                          # translation axis X (meter)
    dy         = 0.040                          # translation axis Y (meter)

    path       = [
      [+dx, 0.0, 0.0, 0.0, 0.0, 0.0],           # Point 1
      [0.0, -dy, 0.0, 0.0, 0.0, 0.0],           # Point 2
      [-dx, 0.0, 0.0, 0.0, 0.0, 0.0],           # Point 3
      [0.0, +dy, 0.0, 0.0, 0.0, 0.0],           # Point 4
      [+dx, 0.0, 0.0, 0.0, 0.0, 0.0],           # Point 5
      [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]           # Point 6

    times      = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0] # seconds

    proxy.positionInterpolation(effector, space, path,
                                axisMask, times, isAbsolute)

if __name__ == "__main__":
    main()
