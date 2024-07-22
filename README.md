# Color-transfer-technique
This project is about the color transfer technique using image processing theories. basically, here it uses LAB color space conversions


This project studies using Python to apply color transfer techniques to improve the visual aesthetics of photographs. The objective of this project is to generate visually pleasing and cohesive outcomes by applying an innovative process that makes it easier to transfer color attributes from a reference image to five target images at once.The technique first analyzes the color distributions of the reference and target photos. Then, mathematical adjustments are applied. Color integrity and artistic quality are assessed on the resultant images, showcasing color transfer’s potential in digital art, photography, and film, among other industries. The project finishes with saved outputs of the altered photos, offering a thorough foundation for other image processing applications in the future

The output results are like this. i done the process for 5 images simultaneously and view those like below. These are done by using software made by me.

# Introduction 
Hello everyone. My name is S.Y.D. Senadheera, 
and today I am excited to present my individual project on color transfer between 
images. This project involves applying sophisticated image processing techniques 
using Python to transfer the color characteristics of a target image to a source 
image, achieving visually appealing transformations. 

# Project Background

Color transfer is a fascinating technique in image processing that alters the colors 
of a source image to match the color palette of a target image. This technique is 
extensively used in various fields such as photography, to enhance aesthetics, 
correct color imbalances, and match thematic elements; in film production, to 
maintain visual continuity, achieve color grading, and unify the visual scheme; and 
in graphic design, to create cohesive designs and harmonize colors. 

# Methodology

The process of color transfer in this project is carried out in the LAB color space. 
The LAB color space is particularly suitable for color manipulation because it 
separates the lightness component (L) from the color components (A and B). The L 
channel represents lightness, which ranges from black to white, while the A and B 
channels represent color components, with A ranging from green to red and B 
ranging from blue to yellow. This separation allows for more precise and 
independent manipulation of color and luminance. 

To implement color transfer, we follow a systematic approach: 

1. Calculation of Statistical Properties: We calculate the mean and standard 
deviation for each channel (L, A, B) in both the source and target images. 
The mean represents the average color value across all pixels in an image 
channel, which provides a central tendency. The standard deviation 
measures the spread of color values around the mean, indicating the color 
contrast and variability.

3. Normalization and Transfer: We then normalize the color values in the 
source image by subtracting the mean and dividing by the standard 
deviation. After normalization, we scale and shift the values to match the 
target image's mean and standard deviation. This step effectively transfers 
the color distribution from the target image to the source image, ensuring the 
resulting image adopts the desired color characteristics.

# Tools and Resources 

In this project, we processed five pairs of images and performed statistical 
calculations in the LAB color space using several powerful libraries and tools: 

• NumPy: For numerical operations and array manipulations.

• OpenCV: For image processing tasks such as reading, writing, and 
converting images between different color spaces. 

• Tkinter: For creating a graphical user interface (GUI) that allows users to 
interact with the application by selecting source and target images and 
viewing results. 

• Matplotlib: For plotting and visualizing the results. 

• Threading: To improve the efficiency and responsiveness of the application 
by performing tasks concurrently. 

• PYInstaller: For packaging the Python application into a standalone 
executable. 

The main tools used include Python as the programming language, Tkinter for the 
GUI elements, file dialogs for file selection, an Integrated Development 
Environment (IDE) like VSCode for coding, an image viewer for displaying 
results, and the command line or terminal for running the application." 

# Results 
Our results demonstrate the successful application of color transfer to five images. 
The transformed images clearly showcase the desired color characteristics, with the 
source images adopting the color palette of the target images. This process 
illustrates the practical application of mean and standard deviation calculations in 
the LAB color space, resulting in visually coherent and aesthetically pleasing 
images.

# Challenges 

"Throughout the project, we encountered several engineering challenges: 

1. Handling Different Image Formats: We had to manage various image 
formats such as BMP, JPG, and JPEG, ensuring they were appropriately 
converted and processed.

3. Consistent Color Transfer: Achieving consistent color transfer across 
images with varying lighting conditions and color distributions required 
careful normalization and scaling.

5. Computational Efficiency: Processing larger images demanded efficient 
algorithms and parallel processing techniques to manage computational load 
and reduce processing time.

Despite these challenges, we were able to develop robust solutions that ensured the 
accuracy and efficiency of the color transfer process." 

# Conclusion 
In conclusion, this project has demonstrated the effectiveness of color transfer 
techniques in achieving visually appealing transformations. By leveraging the LAB 
color space and statistical calculations, we were able to accurately transfer color 
characteristics from target images to source images. Moving forward, further 
refinements can be made to improve efficiency, handle a wider range of image 
formats, and adapt to different lighting conditions. Thank you for your attention, 
and I am now happy to take any questions you may have.

Thank you.

Result 1
![Screenshot 2024-07-16 160629](https://github.com/user-attachments/assets/556e51f2-2613-475c-b59d-f64fed8bdeae)

Result 2
![Screenshot 2024-07-16 161219](https://github.com/user-attachments/assets/14306866-fc67-423f-946e-1e42fe3754f5)

Result 3
![Screenshot 2024-07-16 174538](https://github.com/user-attachments/assets/a0139fae-9ae3-4b62-9085-d5e57f5f2ea0)

Result 4
![Screenshot 2024-07-16 162347](https://github.com/user-attachments/assets/2b48da04-fcbd-4084-b320-ff89c95131ad)

Result 5
![Screenshot 2024-07-16 174554](https://github.com/user-attachments/assets/2fbd3a72-84d5-4bfc-abeb-e8a6c4654ae8)

Software interface

![app](https://github.com/user-attachments/assets/215833ba-a364-46c7-95d7-42d15e2af34f)



Detailed Explanation of the Code 

1. Imports and Setup 
Your code begins with importing various libraries necessary for the image processing and 
GUI components of the project: 

•  NumPy 

Purpose: NumPy is a fundamental package for scientific computing in Python. 

Functionality: It provides support for arrays, matrices, and many mathematical functions 
to operate on these data structures efficiently. 

Usage in Project: NumPy is used for numerical operations and array manipulations, such 
as calculating the mean and standard deviation of the color channels. 

•  OpenCV 

Purpose: OpenCV (Open Source Computer Vision Library) is an open-source library 
that provides tools for computer vision and image processing. 

Functionality: It includes functions for reading, writing, and manipulating images, as 
well as various image processing algorithms. 

Usage in Project: OpenCV is used to read images, convert them between color spaces 
(BGR to LAB and vice versa), and perform the core color transfer operations. 

•  OS 

Purpose: The OS module in Python provides a way of using operating system-dependent 
functionality like reading or writing to the file system. 

Functionality: It includes functions to interact with the file system, such as file and 
directory manipulation. 

Usage in Project: The OS module is used to construct file paths and handle file 
operations such as saving the processed images. 

•  Tkinter 

Purpose: Tkinter is the standard GUI (Graphical User Interface) library for Python. 

Functionality: It provides a toolkit to create and manage GUI elements like windows, 
buttons, labels, and dialogs. 

Usage in Project: Tkinter is used to create the main application window, buttons for 
selecting files and folders, labels for displaying messages, and a progress bar to indicate 
the status of the conversion process. 

•  Matplotlib 

Purpose: Matplotlib is a plotting library for the Python programming language. 

Functionality: It provides an API for embedding plots into applications and creating 
static, animated, and interactive visualizations. 

Usage in Project: Matplotlib is used to display the source, target, and result images side 

•  Threading 

Purpose: The threading module in Python is used to run multiple threads (tasks, function 
calls) concurrently. 

Functionality: It allows the program to perform tasks in the background, keeping the 
main application responsive. 

Usage in Project: Threading is used to run the color transfer process in a separate thread, 
preventing the GUI from freezing during the operation.
