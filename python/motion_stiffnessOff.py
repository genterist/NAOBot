import config
proxy = config.loadProxy("ALMotion")

#We use the "Body" name to signify the collection of all joints
pNames = "Body"
pStiffnessLists = 0.0
pTimeLists = 1.0
proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

