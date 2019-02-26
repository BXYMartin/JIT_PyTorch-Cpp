# PyTorch JIT Experiments
Test for running a PyTorch Module in C++

## img-bin
Convert a image file to binary file.

## cpp-torch
Run the model export by PyTorch using the image file or the preprocessed binary file.

## Tests
Using OpenCV to open a image and feed it to the model in C++ results in a slight difference in the output. 
Considering the possibility that the input could be different, I preprocessed the image in Python. After that the result is exactly the same.
