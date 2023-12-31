# FACIAL_RECOGNITION_BASED_ATTENDANCE_SYSTEM

<h3>TITAL:</h3> 

FACIAL RECOGNITION BASED ATTEBNDABCE SYSTEM 

<h3>INTRODUCTION:</h3>

Faces are the most decorated pictures in the visual system within the life time of a human being. it is not surprising that humans have the ability to recognize faces. With regards to face recognition by humans, it is thought that the brain remembers important details such as the shapes and colors of crucial features corresponding to the eyes, nose, forehead, cheeks and the mouth. Thus, this work is aimed at developing a face recognition system that will be able to detect an imperfect human face and tell whose face it is.
Face recognition has been a very trending and developing area of research. There is continuous research in the domain of face recognition and it has reached a point where a computer recognises human face better than humans ourselves. As such it has become a very reliable technique to use in security applications like Theft monitoring systems, criminal database etc. Face recognition can also be used in educational institutes for taking attendance. Manually taking attendance by calling out individual student’s name one by name is a time-consuming process, hence inefficient. Face recognition based attendance system is by far the best solution to address this problem.

<h3>METHODOLOGY:</h3>

![image](https://github.com/Rohanpophale/FACIAL_RECOGNITION_BASED_ATTENDANCE_SYSTEM/assets/97818946/9aa73e94-2ac1-46ae-87e0-33f1045dcbef)

1. Image Acquisition : Our proposed system uses a camera mounted at a proper place for acquiring students’ face images in a controlled environment.  
2. Image Pre-processing : For image pre-processing, histogram equalization is used to enhance input image quality.  
3. Face Detection : Face is detected from the image using Viola-Jones and HAAR Cascade algorithm.  
4. Feature Extraction : The features are extracted and the feature vectors dimensionality is reduced using the LDA algorithm.  
5. Face Recognition : With the help of LDA, SVM and KNN are used to classify images for face recognition purpose.  
6. Mark Attendance : If a match is found in the database, then it will automatically mark the student’s attendance in the Excel Sheet, as per lecture name and time. Else, it will display an error and attendance will not be marked.

<h3>RESULT:</h3>

![image](https://github.com/Rohanpophale/FACIAL_RECOGNITION_BASED_ATTENDANCE_SYSTEM/assets/97818946/910332da-35db-44e0-a001-d8f2080834bb)

<h3>KEY FINDINGS:</h3>

The proposed model for taking attendance is effective in reducing extra hardware components required to take attendance. All the devices required for this purpose are already available with almost everyone in the present day and age. 

<h3>OUTPUT:</h3> 


![image](https://github.com/Rohanpophale/FACIAL_RECOGNITION_BASED_ATTENDANCE_SYSTEM/assets/97818946/955ceb03-fdb4-4371-a7e2-b7c6325f1bd2)

![image](https://github.com/Rohanpophale/FACIAL_RECOGNITION_BASED_ATTENDANCE_SYSTEM/assets/97818946/38fac0f6-b46f-437b-b989-8841e0f1d710)

![image](https://github.com/Rohanpophale/FACIAL_RECOGNITION_BASED_ATTENDANCE_SYSTEM/assets/97818946/5dc00480-b16b-4934-9193-7a8f9047792a)

<h3>HOW TO RUN:</h3>

Download the following
1. OpenCV (cv2): Computer vision library for image and video processing.
2. face_recognition: Python library for face detection and recognition.
3. NumPy: Fundamental package for scientific computing with Python.
4. datetime: Module for date and time manipulation in Python.
5. os: Module for interacting with the operating system.
6. CSV: Module for reading and writing CSV files in Python.
7. PyQt5: Python bindings for the Qt application framework for creating graphical user interfaces.

Steps

1. Download the repository
2. Open the cmd in this repository and run the command : python mainwindow.py
3. App will run
