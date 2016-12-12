# Maps the positions of the leap motion hand into 2-D space

#### Code to be modified per usage ####
TEXT_FILENAME = "leap_position.txt"
PATH_TO_LEAP_SDK = 'insert absolute path here'
window_width = 1920
window_height = 1080
#######################################

import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = os.path.abspath(os.path.join(PATH_TO_LEAP_SDK))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import numpy as np

file = open(TEXT_FILENAME, 'ab')

class SampleListener(Leap.Listener):

	counter = 0

	def on_connect(self, controller):
		print "Connected"

	def on_frame(self, controller):
		frame = controller.frame()
		iBox = frame.interaction_box

		# Assume only one hand in frame
		if len(frame.hands) == 1:
			hand = frame.hands.frontmost
			fingerPos = []
			for finger in hand.fingers:
				normalizedPoint = iBox.normalize_point( finger.tip_position )
				x = window_width  * normalizedPoint.x
				y = window_height - window_height * (1 - normalizedPoint.z)
				fingerPos.append((x,y))

			# Sort by smallest y coordinate
			fingerPos = sorted(fingerPos, key=lambda x: x[1])
			np.savetxt(file, fingerPos, fmt='%10.5f', delimiter=',')

			# Draw circle using opencv

		else:
			print "No Hand Detected"

def main():
	listener = SampleListener()
	controller = Leap.Controller()

	controller.add_listener(listener)
	print "Press Enter to quit..."
	try:
		sys.stdin.readline()
	except KeyboardInterrupt:
		pass
	finally:
		controller.remove_listener(listener)
		file.close()

if __name__ == "__main__":
    main()

