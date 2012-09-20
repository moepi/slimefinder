import javarandom
import sys

def usage ():
	print("USAGE:\n"+
	sys.argv[0] + " <seed> <xcoord> <zcoord>\n"+
	"to obtain the seed press f3 or (for multiplayer) ask an op to check /seed")

try:
	#read cml arguments
	seed=int(sys.argv[1])
	xPosition=int(sys.argv[2])/16
	zPosition=int(sys.argv[3])/16
except Exception:
	#throw exception on studid user
	usage()	
	sys.exit()

#generate randomobject given notch's magical algorithm
slime=javarandom.Random(seed + (xPosition * xPosition * 0x4c1906) + (xPosition * 0x5ac0db) + (zPosition * zPosition) * 0x4307a7L + (zPosition * 0x5f24f) ^ 0x3ad8025f)
#check if slime found or not (0:slime,1-9:no slime)
if slime.nextInt(10) == 0:
	print "slimes can spawn in this chunk"
else:
	print "no slimes in this chunk"
