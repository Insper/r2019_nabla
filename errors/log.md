borg@borg-borg:~/catkin_ws/src/r2019_nabla/q1_opencv$ python3 videoplay.py 
[mov,mp4,m4a,3gp,3g2,mj2 @ 0x1de11e0] moov atom not found

(python3:6546): GStreamer-CRITICAL **: 14:31:07.501: gst_element_get_state: assertion 'GST_IS_ELEMENT (element)' failed
VIDIOC_REQBUFS: Inappropriate ioctl for device
Codigo de retorno False
Traceback (most recent call last):
  File "videoplay.py", line 18, in <module>
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
cv2.error: OpenCV(3.4.4) /home/borg/tmp/opencv/modules/imgproc/src/color.cpp:181: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor'


