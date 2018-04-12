import cv2
import dlib
class dlibDetect(object):
    def __init__(self, dlibPath):
        self.landmark_predictor = dlib.shape_predictor(dlibPath)
        self.detector = dlib.get_frontal_face_detector()



    def detectFace(self, img):
        faces = self.detector(img, 1)
        return faces

    def getlandmark(self,img, faces):
        if (len(faces) > 0):
            Shapes = []
            for k, d in enumerate(faces):
                # cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (255, 255, 255))
                # rect = [d.left(), d.top(), d.right(), d.bottom()]
                shape = self.landmark_predictor(img, d)
                Shapes.append(shape)
        return Shapes


