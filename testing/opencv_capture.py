import cv2
import time
 
# Camera 0 is the integrated web cam on my netbook
camera_port = 0
 
#Number of frames to throw away while the camera adjusts to light levels
ramp_frames = 0
 
# Now we can initialize the camera capture object with the cv2.VideoCapture class.
# All it needs is the index to a camera port.
camera = cv2.VideoCapture(camera_port)
 
# Captures a single image from the camera and returns it in PIL format
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = camera.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in xrange(ramp_frames):
 temp = get_image()

now = time.time()
for i in range(30):
    print("Taking image... %i" % i)
    camera_capture = get_image()
    #file = "capture_%04i.bmp" % i
    #cv2.imwrite(file, camera_capture)
 
print time.time()-now

# You'll want to release the camera, otherwise you won't be able to create a new
# capture object until your script exits
del(camera)

