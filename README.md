
#Automatic License/Number Plate Recognition (ANPR)

Automatic License/Number Plate Recognition (ANPR) is the process of detecting the position of a number plate and then using Optical Character Recognition (OCR) to identify the text on the plate. This process is widely used in real-life scenarios where accuracy is critical.

Overview

This project demonstrates the implementation of an ANPR system using Python. The system detects number plates in an image and extracts the alphanumeric text using EasyOCR.

Steps Implemented

Installing and Importing Dependencies:

Installed Python libraries such as OpenCV and EasyOCR.

Reading the Image:

Loaded the input image and applied preprocessing filters like grayscale conversion and blurring to enhance the image quality.

Edge Detection:

Performed edge detection to highlight the boundaries of objects in the image, aiding in plate detection.

Contour Detection:

Identified and marked contours to localize the number plate area in the image.

Text Extraction Using OCR:

Integrated EasyOCR to accurately extract alphanumeric text from the detected number plate.

Rendering the Result:

Displayed the processed image with the detected number plate and the extracted text for verification.

Key Optimizations

Integrated EasyOCR for high accuracy in extracting text from plates.

Optimized the system for real-world scenarios by addressing challenges such as varying lighting conditions and plate designs.

Tools and Technologies Used

Programming Language: Python

Libraries: OpenCV, EasyOCR

Usage

Clone the repository and install the required dependencies:

pip install opencv-python easyocr

Run the Python script on an input image to detect and recognize the license plate.

Results

Successfully detected license plates in test images.

Extracted text with high accuracy using EasyOCR.

