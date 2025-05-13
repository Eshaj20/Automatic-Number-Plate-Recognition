## Automatic License/Number Plate Recognition (ANPR)

Automatic License/Number Plate Recognition (ANPR) is the process of detecting the position of a number plate and then using Optical Character Recognition (OCR) to identify the text on the plate. This system is widely used in real-world applications where accuracy is critical, such as traffic monitoring, parking management, and security systems.

Overview :
This project demonstrates the implementation of an ANPR system using Python. The system:
1. Detects number plates in an image.
2. Extracts the alphanumeric text using EasyOCR.

---------------------------------------------------------

# Steps Implemented

1. Installing and Importing Dependencies
Installed Python libraries:
     i)  OpenCV (for image processing)
     ii) EasyOCR (for text extraction)

2. Reading the Image
i)  Loaded the input image.
ii) Applied preprocessing filters (grayscale conversion, blurring) to enhance quality.

4. Edge Detection
Performed edge detection (e.g., Canny edge) to highlight object boundaries.

5. Contour Detection
Identified and marked contours to localize the number plate region.

6. Text Extraction Using OCR
Integrated EasyOCR to extract alphanumeric text from the detected plate.

7. Rendering the Result
Displayed the processed image with:
i) Detected number plate (bounding box).
ii) Extracted text for verification.

-------------------------------
# Key Optimizations

- High Accuracy: Used EasyOCR for robust text extraction.
- Real-World Adaptability: Optimized for varying:

1.Lighting conditions.
2.Plate designs (fonts, colors, backgrounds).

-------------------------------
# Tools and Technologies Used

- Category   ---> Technology       
- Language   ---> Python
- Libraries  ---> OpenCV, EasyOCR

-------------------------------
# Usage
Clone the repository:

                    git clone <repo-url>

Install dependencies:

                   pip install opencv-python easyocr

Run the script:

                   python anpr.py --image <input_image_path>

--------------------------------
                    
# Results

- Successfully detected license plates in test images.
- Extracted text with high accuracy using EasyOCR.


