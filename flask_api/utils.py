"""@desc 
		Utilities for flask API

 	@author 
 		Domnan Diretnan
 		Artificial Intelligence Enthusiast & Software Engineer.
 		Email: diretnandomnan@gmail.com
 		Github: https://github.com/deven96
 		GitLab: https://gitlab.com/Deven96

 	@project
 		@create date 2018-12-31 03:38:44
 		@modify date 2018-12-31 03:38:44

	@license
		MIT License
		Copyright (c) 2018. Domnan Diretnan. All rights reserved

 """

from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import numpy as np



def prepare_image(image, target_size):
    """Prepare incoming image data to suite 

    :param image: image to be preprocessed
    :type image: bytes
    :param target_size: resize image to this size
    :type target_size: tuple

    :rtype: `np.ndarray`
    """
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image