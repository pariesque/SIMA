print "|--------------------------------------------|"
print "|         Starting Character Demo            |"
print "|--------------------------------------------|"
# from os import environ
import os
import __builtin__

# from os import environ

# sys.path.append("c:/users/Ari/avatarchat/nonverbalbehavior")

inEditMode = False



# Add asset paths
scene.addAssetPath('mesh', 'ChrOlivia/mesh/clean')
scene.addAssetPath('motion', 'ChrOlivia/face3')
#scene.addAssetPath('motion', 'ChrOlivia/motion')
scene.addAssetPath("script", "behaviorsets")
scene.addAssetPath('script', 'scripts')
#scene.addAssetPath("script", "sbm-common/scripts")
scene.loadAssetsFromPath("ChrOlivia/mesh/clean")
scene.loadAssets()

# # Set scene parameters and camera
# print 'Configuring scene parameters and camera'
# scene.setScale(1.0)
# scene.setBoolAttribute('internalAudio', True)
# scene.run('default-viewer.py')
# camera = getCamera()
# camera.setEye(0, 1.71, 1.86)
# camera.setCenter(0, 1, 0.01)
# camera.setUpVector(SrVec(0, 1, 0))
# camera.setScale(1)
# camera.setFov(1.0472)
# camera.setFarPlane(100)
# camera.setNearPlane(0.1)
# camera.setAspectRatio(0.966897)
# cameraPos = SrVec(0, 1.6, 10)
# scene.getPawn('camera').setPosition(cameraPos)




# Set scene parameters and camera
print 'Configuring scene parameters and camera'
scene.setScale(1.0)
scene.setBoolAttribute('internalAudio', True)
scene.run('default-viewer.py')
camera = getCamera()

camera.setEye(-0.00759659, 1.75002, 1.94873)
camera.setCenter(0, 1.5, 0.01)
# camera.setCenter(.12, 1.46355, -0.332304)
camera.setUpVector(SrVec(-0.00280115, 0.999989, -0.00365))
camera.setScale(1)
camera.setFov(0.329337)
camera.setFarPlane(100)
camera.setNearPlane(0.1)
camera.setAspectRatio(0.877778)
cameraPos = SrVec(-0.00759659, 1.75002, 1.94873)
camera.setDoubleAttribute("rotX",-7.15803)
camera.setDoubleAttribute("rotY",0.408051)
camera.setDoubleAttribute("rotZ",0.160177)
scene.getPawn('camera').setPosition(cameraPos)


#scene.run("light.py")
scene.run("light.py")
scene.setBoolAttribute("GUI.ShowGrid", False)
scene.setBoolAttribute("GUI.ShowFloor", False)
#scene.setVec3Attribute("GUI.BackgroundColor", .33, .78, .95) # lavender
scene.setVec3Attribute("GUI.BackgroundColor", 1, .85, .90) # pink








# Set up joint map for Olivia
print 'Setting up joint map and configuring Olivia\'s skeleton'
OliviaSkeleton = scene.getSkeleton('ChrOlivia.dae')
scene.run('zebra2-map.py')
zebra2Map = scene.getJointMapManager().getJointMap('zebra2')
# OliviaSkeleton.rescale(.01)
zebra2Map.applySkeleton(OliviaSkeleton)


# Establish lip syncing data set
scene.run('init-diphoneDefault.py')


print 'Adding character into scene'
# Set up Olivia
Olivia = scene.createCharacter('ChrOlivia', '')
OliviaSkeleton = scene.createSkeleton('ChrOlivia.dae')


print "skeleton is      kjbkjbwkjfbekbekjbkjebkjeb" + str(OliviaSkeleton)
print "Skeleton Name is:       " + str(OliviaSkeleton.getName())
Olivia.setSkeleton(OliviaSkeleton)

Olivia.createStandardControllers()


# zebra2Map.applyMotionRecurse('ChrOlivia')

# Establish lip syncing data set
print 'Establishing lip syncing data set'
scene.run('init-diphoneDefault.py')

# Set up face definition
print 'Setting up face definition'
# Olivia's face definition
OliviaFace = scene.createFaceDefinition('ChrOlivia')



OliviaFace.setFaceNeutral('ChrOlivia@face_neutral')
OliviaFace.setAU(1,  "both",  "ChrOlivia@001_InnerBrowRaiser")
OliviaFace.setAU(1,  "left",  "ChrOlivia@001_InnerBrowRaiserL")
OliviaFace.setAU(1,  "right", "ChrOlivia@001_InnerBrowRaiserR")
OliviaFace.setAU(2,  "both",  "ChrOlivia@002_OuterBrowRaiser")
OliviaFace.setAU(2,  "left",  "ChrOlivia@002_OuterBrowRaiserL")
OliviaFace.setAU(2,  "right", "ChrOlivia@002_OuterBrowRaiserR")
OliviaFace.setAU(4,  "both",  "ChrOlivia@004_BrowLowerer")
OliviaFace.setAU(5,  "both",  "ChrOlivia@005_UpperLidRaiser")
OliviaFace.setAU(6,  "both",  "ChrOlivia@006_CheekRaiser")
OliviaFace.setAU(6,  "left",  "ChrOlivia@006_CheekRaiserL")
OliviaFace.setAU(6,  "right",  "ChrOlivia@006_CheekRaiserR")
OliviaFace.setAU(7,  "both",  "ChrOlivia@007_LidTightener")
OliviaFace.setAU(7,  "left",  "ChrOlivia@007_LidTightenerL")
OliviaFace.setAU(7,  "right",  "ChrOlivia@007_LidTightenerR")
OliviaFace.setAU(9,  "both",  "ChrOlivia@009_NoseWrinkler")
OliviaFace.setAU(10, "both",  "ChrOlivia@010_UpperLipRaiser")
OliviaFace.setAU(10, "left",  "ChrOlivia@010_UpperLipRaiserL")
OliviaFace.setAU(10, "right",  "ChrOlivia@010_UpperLipRaiserR")

OliviaFace.setAU(11, "both",  "ChrOlivia@011_NasolabialDeepener")
OliviaFace.setAU(11, "left",  "ChrOlivia@011_NasolabialDeepenerL")
OliviaFace.setAU(11, "right",  "ChrOlivia@011_NasolabialDeepenerR")

OliviaFace.setAU(12, "both",  "ChrOlivia@012_LipCornerPuller")
OliviaFace.setAU(12, "left",  "ChrOlivia@012_LipCornerPullerL")
OliviaFace.setAU(12, "right", "ChrOlivia@012_LipCornerPullerR")

OliviaFace.setAU(13, "both",  "ChrOlivia@013_SharpLipPuller")

OliviaFace.setAU(14, "both",  "ChrOlivia@014_Dimpler")
OliviaFace.setAU(14, "left",  "ChrOlivia@014_DimplerL")
OliviaFace.setAU(14, "right",  "ChrOlivia@014_DimplerR")

OliviaFace.setAU(15, "both",  "ChrOlivia@015_LipCornerDepressor")
OliviaFace.setAU(16, "both",  "ChrOlivia@016_LowerLipDepressor")
OliviaFace.setAU(17, "both",  "ChrOlivia@017_ChinRaiser")

OliviaFace.setAU(20, "both",  "ChrOlivia@020_LipStretcher")
OliviaFace.setAU(20, "left",  "ChrOlivia@020_LipStretcherL")
OliviaFace.setAU(20, "right",  "ChrOlivia@020_LipStretcherR")

OliviaFace.setAU(22, "both",  "ChrOlivia@022_LipFunneler")
OliviaFace.setAU(23, "both",  "ChrOlivia@023_LipTightener")
OliviaFace.setAU(24, "both",  "ChrOlivia@024_LipPressor")
OliviaFace.setAU(25, "both",  "ChrOlivia@025_LipsPart")
OliviaFace.setAU(26, "both",  "ChrOlivia@026_JawDrop")
OliviaFace.setAU(27, "both",  "ChrOlivia@027_MouthStretch")
OliviaFace.setAU(38, "both",  "ChrOlivia@038_NostrilDilator")
OliviaFace.setAU(39, "both",  "ChrOlivia@039_NostrilCompressor")
OliviaFace.setAU(43, "both",  "ChrOlivia@043_EyesClosed")


OliviaFace.setAU(45, "left",  "ChrOlivia@045_BlinkL")
OliviaFace.setAU(45, "right", "ChrOlivia@045_BlinkR")
# au12 + au25
OliviaFace.setAU(100, "both", "ChrOlivia@100_LipCornerPuller-LipsPart")# au12 + au6
OliviaFace.setAU(101, "both", "ChrOlivia@101_LipCornerPuller-CheekRaiser")# au1 + au2
OliviaFace.setAU(102, "both", "ChrOlivia@102_InnerBrowRaiser-OuterBrowRaiser")
# OliviaFace.setAU(103, "both", "ChrOlivia@ChrOlivia@006_CheekRaiser")

OliviaFace.setViseme("open",    "ChrOlivia@open")
OliviaFace.setViseme("W",       "ChrOlivia@W")
OliviaFace.setViseme("ShCh",    "ChrOlivia@ShCh")
OliviaFace.setViseme("PBM",     "ChrOlivia@PBM")
OliviaFace.setViseme("FV",      "ChrOlivia@FV")
OliviaFace.setViseme("wide",    "ChrOlivia@wide")
OliviaFace.setViseme("tBack",   "ChrOlivia@tBack")
OliviaFace.setViseme("tRoof",   "ChrOlivia@tRoof")
OliviaFace.setViseme("tTeeth",  "ChrOlivia@tTeeth")



# Set position
OliviaPos = SrVec(0, 0, -1.0)
Olivia.setPosition(OliviaPos)
# Set facing direction
OliviaFacing = SrVec(0, 0, 0)
Olivia.setHPR(OliviaFacing)
# Set face definition
Olivia.setFaceDefinition(OliviaFace)
# Set standard controller

# Gesture map setup
Olivia.setStringAttribute('gestureMap', 'ChrRachel')
Olivia.setBoolAttribute('bmlRequest.autoGestureTransition', True)


# Deformable mesh
# ########### Olivia.setVec3Attribute('deformableMeshScale', .01, .01, .01)
Olivia.setStringAttribute('deformableMesh', 'ChrOlivia.dae')
Olivia.setActionAttribute("updateChannel")

# Lip syncing diphone setup
Olivia.setStringAttribute('lipSyncSetName', 'default')
Olivia.setBoolAttribute('usePhoneBigram', True)
Olivia.setVoice('remote')
import platform
if platform.system() == "Windows":
	windowsVer = platform.platform()
	if windowsVer.find("Windows-7") == 0:
		Olivia.setVoiceCode('Microsoft|Anna')
	elif windowsVer.find("Windows-10") == 0:
		Olivia.setVoiceCode('Microsoft|Zira|Desktop') 
	else:
		if windowsVer.find("Windows-8") == 0 or windowsVer.find("Windows-post2008Server") == 0:
			Olivia.setVoiceCode('Microsoft|Zira|Desktop')
else: # non-Windows platform, use Festival voices
	Olivia.setVoiceCode('voice_kal_diphone')


# setup locomotion

# setup reach 


# Turn on GPU deformable geometry
Olivia.setStringAttribute("displayType", "GPUmesh")

# Set up gaze
gazeTarget = scene.createPawn("None")
gazeTargetPos = SrVec(0, 2.0, 2.7)
gazeTarget.setPosition(gazeTargetPos)
bml.execBML(Olivia.getName(), '<gaze target="None" sbm:joint-range="EYES NECK" />')
# set up gestures
scene.run('BehaviorSetOliviaGestures.py')
setupBehaviorSet(OliviaSkeleton)
retargetBehaviorSet('ChrOlivia')
#gestureMap = scene.getGestureMapManager().createGestureMap('ChrRachel')
#gestureMap = scene.getGestureMapManager().createGestureMap('ChrOlivia')
#gestureMap.addGestureMapping("ChrRachel@Idle02_Approximation01.skm", "METAPHORIC", "APPROXIMATION", "RIGHT_HAND","","Idle02.skm") ##
#print(gestureMap)
bml.execBML('ChrOlivia', '<body posture="ChrRachel@Idle02" ready="0" relax="0" />')
print "posture is built"
# sim.setSimFps(60)
sim.resume()

#scene.run("runNVBG.py")
#nvbg = character.getNvbg().nvbg

# set the emotion
#etype = os.environ["EMOTIONTYPE"]
#character.getNvbg().setStringAttribute("emotion", etype)


# gaze target
# gazeTarget = scene.createPawn("None")
# gazeTargetPos = SrVec(0, 2.0, 2.7)
# gazeTarget.setPosition(gazeTargetPos)
# bml.execBML(Olivia.getName(), '<gaze target="None" sbm:joint-range="EYES NECK" />')
# HERE IS THE CALL THAT bml.execBML(Olivia.getName(), '<gaze target="None" sbm:joint-range="EYES NECK" ready="0" relax="0" start="0"/>')


# sim.start()
####bml.execBML('ChrOlivia', '<body posture="ChrRachel@Idle02"/>')
#bml.execBML('ChrOlivia', '<body posture="ChrRachel@IdleHandsAtSide01"/>')
# bml.execBML('ChrOlivia', '<body posture="ChrMarine@Idle01"/>')
# bml.execBML('ChrOlivia', '<saccade mode="listen"/>')
# #bml.execBML('ChrOlivia', '<gaze sbm:handle="Olivia" target="camera"/>')

# sim.resume()

# Set saccade mode for olivia
print 'Setting saccade mode to talk'
bml.execBML('*', '<saccade mode="talk"/>')


#sentence = "Hi, my name is Parisa."
#bml.execBML('ChrOlivia', '<speech type="text/plain">' + sentence + '</speech><head type="NOD" amount=".3"/><gaze sbm:joint-range="NECK EYES"/>')


