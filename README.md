
# Day and Night Image Classifier Pipeline

## Getting Started
The day/night image dataset consists of 200 RGB color images in two categories: day and night. There are equal numbers of each example: 100 day images and 100 night images.

We'd like to build a classifier that can accurately label these images as day or night, and that relies on finding distinguishing **features** between the two types of images!

*Note: All images come from the [AMOS dataset](http://cs.uky.edu/~jacobs/datasets/amos/) (Archive of Many Outdoor Scenes). and the project based on the work of Udacity CVND*

![buddha](https://user-images.githubusercontent.com/16764177/55517982-95bd9180-5672-11e9-9297-38a1ceefd650.jpg)

![image](https://user-images.githubusercontent.com/16764177/55518616-fea60900-5674-11e9-9cb5-b2cf90c9b641.png)

## Prerequisites

### Configure and Manage Your Environment with Anaconda

Per the Anaconda [docs](http://conda.pydata.org/docs):

> Conda is an open source package management system and environment management system 
for installing multiple versions of software packages and their dependencies and 
switching easily between them. It works on Linux, OS X and Windows, and was created 
for Python programs but can package and distribute any software.

## Overview
Using Anaconda consists of the following:

1. Install [`miniconda`](http://conda.pydata.org/miniconda.html) on your computer
2. Create a new `conda` [environment](http://conda.pydata.org/docs/using/envs.html) using this project
3. Each time you wish to work, activate your `conda` environment

---

## Installation

**Download** the version of `miniconda` that matches your system. Make sure you download the version for Python 3.5.

**NOTE**: There have been reports of issues creating an environment using miniconda `v4.3.13`. If it gives you issues try versions `4.3.11` or `4.2.12` from [here](https://repo.continuum.io/miniconda/).

|        | Linux | Mac | Windows | 
|--------|-------|-----|---------|
| 64-bit | [64-bit (bash installer)][lin64] | [64-bit (bash installer)][mac64] | [64-bit (exe installer)][win64]
| 32-bit | [32-bit (bash installer)][lin32] |  | [32-bit (exe installer)][win32]

[win64]: https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86_64.exe
[win32]: https://repo.continuum.io/miniconda/Miniconda3-latest-Windows-x86.exe
[mac64]: https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
[lin64]: https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
[lin32]: https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86.sh

**Install** [miniconda](http://conda.pydata.org/miniconda.html) on your machine. Detailed instructions:

- **Linux:** http://conda.pydata.org/docs/install/quick.html#linux-miniconda-install
- **Mac:** http://conda.pydata.org/docs/install/quick.html#os-x-miniconda-install
- **Windows:** http://conda.pydata.org/docs/install/quick.html#windows-miniconda-install

**Setup** your the `dn-classifier` environment. 

```sh
git clone https://github.com/Geekgineer/day-night-image-classifier-pipline.git
cd day-night-image-classifier-pipline
```


**Create** dn-classifier  Running this command will create a new `conda` environment that is provisioned with all libraries you need to be successful run this application.
```sh

 $ conda create --name dn-classifier --file package-list-conda.txt
```
**Verify** that the carnd-term1 environment was created in your environments:

```sh
 $ conda info --envs
```

**Cleanup** downloaded libraries (remove tarballs, zip files, etc):

```sh
 $ conda clean -tp
```

### For Uninstalling 

To uninstall the environment:

```sh
 $ conda env remove -n carnd-term1
```

## Project Manual 

### Using without much details  

1- import main.py

2- read your_image 
```py
image = dnc.mpimg.imread('your_image.jpg')
```
3- Call the following function it will return a decision which is string day or night!

```py
 decision = dnc.estimate_label(image)
```

### Training and Testing Data
The 200 day/night images are separated into training and testing datasets. 

* 60% of these images are training images, for you to use as you create a classifier.
* 40% are test images, which will be used to test the accuracy of your classifier.

First, we set some variables to keep track of some where our images are stored:

    image_dir_training: the directory where our training image data is stored
    image_dir_test: the directory where our test image data is stored

#### Using the load_dataset function in helpers.py to Load training data
​
These first few lines of code will load the training day/night images and store all of them in a variable, `IMAGE_LIST`. This list contains the images and their associated label ("day" or "night"). 
​
For example, the first image-label pair in `IMAGE_LIST` can be accessed by index: 
``` IMAGE_LIST[0][:]```.
​
```py
IMAGE_LIST = helpers.load_dataset(image_dir_training)
```

### Standardize all training images
Construct a STANDARDIZED_LIST of input images and output labels.
This function takes in a list of image-label pairs and outputs a standardized list of resized images and numerical labels.
```py
STANDARDIZED_LIST = helpers.standardize(IMAGE_LIST)
```



Classification and Visualizing Error
In this section, we'll turn our average brightness feature into a classifier that takes in a standardized image and returns a predicted_label for that image. This estimate_label function should return a value: 0 or 1 (night or day, respectively).

    
#### This function should take in RGB image input and return predectied lable wich present the 1 for day and 0 for night

```py
estimate_label(rgb_image) 
```

Testing the classifier
Here is where we test your classification algorithm using our test set of data that we set aside at the beginning of the notebook!

Since we are using a pretty simple brightess feature, we may not expect this classifier to be 100% accurate. We'll aim for around 75-85% accuracy usin this one feature.

Test dataset
Below, we load in the test dataset, standardize it using the standardize function you defined above, and then shuffle it; this ensures that order will not play a role in testing accuracy.

import random

---


## Visualize the standardized data
​
Display a standardized image from STANDARDIZED_LIST.

## Feature Extraction

Create a feature that represents the brightness in an image. We'll be extracting the **average brightness** using HSV colorspace. Specifically, we'll use the V channel (a measure of brightness), add up the pixel values in the V channel, then divide that sum by the area of the image to get the average Value of the image.

## Classification and Visualizing Error

In this section, we'll turn our average brightness feature into a classifier that takes in a standardized image and returns a `predicted_label` for that image. This `estimate_label` function should return a value: 0 or 1 (night or day, respectively).

## Testing the classifier

Here is where we test your classification algorithm using our test set of data that we set aside at the beginning of the notebook!

Since we are using a pretty simple brightess feature, we may not expect this classifier to be 100% accurate. We'll aim for around 75-85% accuracy usin this one feature.


### Test dataset

Below, we load in the test dataset, standardize it using the `standardize` function you defined above, and then **shuffle** it; this ensures that order will not play a role in testing accuracy.

## Determine the Accuracy

Compare the output of your classification algorithm (a.k.a. your "model") with the true labels and determine the accuracy.

This code stores all the misclassified images, their predicted labels, and their true labels, in a list called `misclassified`.

### Visualize the misclassified images

Visualize some of the images you classified wrong (in the `MISCLASSIFIED` list) and note any qualities that make them difficult to classify. This will help you identify any weaknesses in your classification algorithm.