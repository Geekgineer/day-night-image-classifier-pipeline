import cv2 # computer vision library
import helpers
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# Image data directories
image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

# Using the load_dataset function in helpers.py
# Load training data
IMAGE_LIST = helpers.load_dataset(image_dir_training)

# Standardize all training images
STANDARDIZED_LIST = helpers.standardize(IMAGE_LIST)

# Display a standardized image and its label

# Select an image by index
image_num = 0
selected_image = STANDARDIZED_LIST[image_num][0]
selected_label = STANDARDIZED_LIST[image_num][1]

# Display image and data about it
# plt.imshow(selected_image)
# print("Shape: "+str(selected_image.shape))
# print("Label [1 = day, 0 = night]: " + str(selected_label))

# Find the average Value or brightness of an image
def avg_brightness(rgb_image):
    # Convert image to HSV
    hsv = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)

    # Add up all the pixel values in the V channel
    sum_brightness = np.sum(hsv[:,:,2])
    area = 600*1100.0  # pixels
    
    # find the avg
    avg = sum_brightness/area
    
    return avg


# Testing average brightness levels
# Look at a number of different day and night images and think about 
# what average brightness value separates the two types of images


# As an example, a "night" image is loaded in and its avg brightness is displayed
#################TESTING###################
#image_num = 190                    
#test_im = STANDARDIZED_LIST[image_num][0]
#
#avg = avg_brightness(test_im)
#print('Avg brightness: ' + str(avg))
#plt.imshow(test_im)
###########################################

# This function should take in RGB image input
def estimate_label(rgb_image):
    
    # Extract average brightness feature from an RGB image 
    avg = avg_brightness(rgb_image)
        
    # Use the avg brightness feature to predict a label (0, 1)
    predicted_label = 0
    threshold = 99 #tune this threshold for better model accuracy 
    if(avg > threshold):
        # if the average brightness is above the threshold value, we classify it as "day"
        predicted_label = 1
        if (predicted_label == 1):
             my_decision = "day" 
    else:
            my_decision = "night"
    # else, the pred-cted_label can stay 0 (it is predicted to be "night")
    
    return my_decision    

