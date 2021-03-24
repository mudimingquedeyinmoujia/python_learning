import skimage
import dlib
from skimage import io
from skimage import transform
import numpy as np
import matplotlib.pyplot as plt

predictor_path='../dlib/shape_predictor_68_face_landmarks.dat'
face_path='../matplot_test/image002.jpg'

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
img = dlib.load_rgb_image(face_path)
dets = detector(img, 1)
image=io.imread(face_path)
for i,d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        i, d.left(), d.top(), d.right(), d.bottom()))
    center=[(d.left()+d.right())/2,(d.top()+d.bottom())/2]
    shape = predictor(img, d)
    x_dots=[shape.part(i).x for i in range(68)]
    y_dots=[shape.part(i).y for i in range(68)]

xy_dots=np.array([x_dots,y_dots,[1 for i in range(68)]]).reshape(3,68).T
print(xy_dots)
plt.imshow(image)
plt.plot(x_dots,y_dots,'o')
plt.show()
size=256*0.7
[crop_h, crop_w, crop_c] = 256,256,3
src_pts = np.array([[center[0] - size / 2, center[1] - size / 2], [center[0] - size / 2, center[1] + size / 2],
                            [center[0] + size / 2, center[1] - size / 2]])
dst_pts = np.array([[0, 0], [0, crop_h - 1], [crop_w - 1, 0]])
tform = transform.estimate_transform('similarity', src_pts, dst_pts)
print('tform is',tform)
trans_mat = tform.params
print('trans mat is')
print(trans_mat)
trans_mat_inv = tform._inv_matrix
print('trans mat inv is')
print(trans_mat_inv)
scale = trans_mat[0][0]
cropped_image = skimage.transform.warp(image, trans_mat_inv, output_shape=(crop_h, crop_w))
dots_after=np.dot(xy_dots,trans_mat.T)

plt.imshow(cropped_image)
plt.plot(dots_after[:,0],dots_after[:,1],'o')
plt.show()