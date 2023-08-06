# Proc_Image
Small and simple image processing library

# How to Install The Library?
## pip install ProcImage

## First, this is a simple and compact package for image processing and hardware management developed using the Pillow package
------------------------

* First: This package contains two volumes, the first folder is called *Image_* This folder contains a file called *image_processing.py* and this file is for image processing

--------------------


* Secondly: The second folder is called *organize* and this folder contains a file called *organize_hard.py* for organizing the  that arranges the pictures, folders, applications, etc... It arranges and organizes them well and neatly.



1- Now: We start giving examples of the folder *Image_* We agree that this folder contains a Python file named *processing_image.py* and this file contains several functions. We will now give examples of these functions in this file.


## Let's take an example : about the function <font color='red'>get_list(path)</font> it takes the path of a folder and then returns all the images as a table


```python
from processing import ImageProcessing

my_object = ImageProcessing()
print(my_object.get_list(r"C:\Users\Alaa\Pictures"))

```
# Output

|  Name Image |
| ---------------|
|  33.jpg
|A.jpg
|aesthetic-ocean-cell-phone-art-94x4pcvrtazi8upm.jpg |
|                   palm-tree-1.jpg                   |
|                        rr.jpg                       |
|                       test.jpg                      |
|                      test1.jpg                      |
|                      veidz.jpg             





##### ['33.jpg', 'A.jpg', 'aesthetic-ocean-cell-phone-art-94x4pcvrtazi8upm.jpg', 'palm-tree-1.jpg', 'rr.jpg', 'test.jpg', 'test1.jpg', 'veidz.jpg']

-----
# Example Two

### The first function <font color='red'>get_list_sorted(main_path , answer)</font> takes the full path of the target image folder,
###and takes the user's answer, in order to arrange the images in ascending or descending order. In the entered folder


```python
from processing import ImageProcessing
my_object = ImageProcessing()

print(my_object.get_list_sorted(r"C:\Users\Alaa\Pictures",False))

```

# Output
##### ['33.jpg', 'A.jpg', 'aesthetic-ocean-cell-phone-art-94x4pcvrtazi8upm.jpg', 'palm-tree-1.jpg', 'rr.jpg', 'test.jpg', 'test1.jpg', 'veidz.jpg']

------

### The second function <font color='red'>best_image(path_image )</font> takes the full path of the target image folder and then returns the best image in terms
### of resolution and it takes only one parameter, which is the full path of the folder containing the images

```python
from processing import ImageProcessing

my_object = ImageProcessing()
print(my_object.best_image(r"C:\Users\Alaa\Pictures"))

```

# Output
##### ['A.jpg', 6400, 'C:\\Users\\Alaa\\Pictures']


##### name Image :A.jpg
##### total dimensions :6400 Pixel
##### Location :C:\Users\Alaa\Pictures
----


![Developer](https://lh3.googleusercontent.com/ogw/ADea4I69npfzwotm16-3HpRfSP4VbW87nXPfi5b8FD-mNu4=s32-c-mo)
["Developer"](https://www.facebook.com/alaa.jassim.mohammed)
