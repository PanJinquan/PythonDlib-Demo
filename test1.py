import cv2
import dlib
from dlibFun import dlibFaceDetection
from dlibFun import landmark
#模型下载地址：http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
dlibPath="D:/MyGit/shape_predictor_68_face_landmarks.dat"
img = cv2.imread('image/1.jpg')
detect=dlibFaceDetection.dlibDetect(dlibPath)
faces = detect.detectFace(img)
shapes=detect.getlandmark(img, faces)
landmark.show_image(img, shapes)
