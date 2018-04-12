import cv2
def show_image(img,Shapes):
    for k, shape in enumerate(Shapes):
        cv2.rectangle(img, (shape.rect.left(), shape.rect.top()), (shape.rect.right(), shape.rect.bottom()), (0, 0, 255))
        for i in range(shape.num_parts):
                cv2.circle(img, (shape.part(i).x, shape.part(i).y), 2, (255, 0, 0), -1, 2)
                cv2.putText(img, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0))
    cv2.imshow('Frame', img)
    cv2.waitKey(0)