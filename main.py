import day_night_image_classifier as dnc
import classifier_accuracy as dncacc
import helpers


# Read in the image
image = dnc.mpimg.imread('buddha.jpg')
img = dnc.np.copy(image) 


# take decision
decision = dnc.estimate_label(img)


# Display image and data about it
dnc.plt.imshow(img)
print("Shape: "+str(img.shape))
print("my decision is " + decision)
