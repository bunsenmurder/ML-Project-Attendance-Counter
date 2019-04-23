# High Level Description of Our Project
### The problem we aimed to solve
Teachers use up valuable class time taking attendance when they could be spending more time teaching. In addition, there are several loopholes to traditional attendance systems. For example, one student can write another student’s name on an attendance sheet. At a large university with several hundred students, attendance can take a very long time if it is done at all. Generally speaking, taking roll at the beginning of class is an inconvenience that can be avoided, so we want to create a facial recognition system to solve this problem. 

### The solution that we envisioned
Our solution is a facial recognition software that will automate the attendance process. It will receive input from a webcam, and will simultaneously process all of the students in the classroom. Ideally, it would label each face with a name, but we acknowledge that this is a very ambitious goal for our skill sets. Without recognizing individual faces, the software counts the number of heads in the room and will notify the user how this compares to the expected number. At Florida Polytechnic, there is a webcam at the back of every classroom, which could potentially integrate with our software. This way, professors are not required to bring their own cameras or take a picture with their phones. Our ideal final deliverable is a computer application that uses a webcam to count the number of faces it sees on screen, which works consistently and accurately.

### What we ended up accomplishing
Over the course of the semester, we achieved some of our goals, but also fell short of many. We successfully created software that is able to point and count faces through a webcam, although the accuracy leaves much to be desired. While a more consistent and accurate model, as well as a prettier user interface would have been nice, we are still satisfied with the work we have done and the skills we learned along the way. 


# Setup Instructions
## Dependencies: 
- OpenCV 3.4.X
- Perl 5.x.x
- Python 3.6.X

## Directions For Linux 
1. Follow the "INSTALLING OPENCV ON UBUNTU.txt" for install instructions of dependances on Linux.
2. Clone this repository.
3. cd ML-Project-Attendance-Counter
4. cd tar
5. python3 runFirst.py
6. cd ..
7. python3 crop_pos.py
8. python random_sample.py
9. For the "random_sample.py" script it will ask you to pick how many positive and negative samples you want reference the "bash commands.txt" and see the amount of samples it recommends for the particular model you choose. Just make sure NOT to select more 435 positive samples or more than 3019 negative samples.
10. Make sure you backup any previously trained models then remove all files within the classifier directory. 
11. Next open up the "bash commands.txt" file and run the commands in order for the model you are choosing. Note: The opencv_traincascade process can take from a 1-5 days depending on your processor and memory.
12. Once you follow the directions for your particular model, the model itself should be saved as "cascade.xml" in the classifier directory. 
13. The output of your model tests will be stored in a file called "output_X.txt" where X is replaced with your type of model, which located in the classifier directory.
14. python3 webcam.py
15. The application would be running now, press q to take a picture of the current attendace and quit the application.

Optional:
16. To view Hit rate and False Alarm rates of our models , run the test.py file and it will output the results within terminal for each model file in our model folder.

## Directions for Windows
After dependancies are installed, open up gitbash and follow these instructions.

1. Download and install this version of python first https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe
2. Then download and install Perl from here http://strawberryperl.com 
3. Then download and run this git installer, make sure it installs everything https://git-scm.com/downloads
4. Then up the command prompt and run the command below.
5. git clone https://github.com/bunsenmurder/ML-Project-Attendance-Counter
6. After that close command prompt and open up the git bash application. Then follow the commands listed out below from there.
7. cd ML-Proj*
8. cd tar
9. python runFirst.py
10. cd ..
11. pip install scipy Pillow opencv-python
12. python crop_pos.py
13. For the crop_pos.py it will ask you which data set to choose, enter the number that corresponds with the dataset(Cal tech 101 or MIT CBCL) you wish to use.
14. python random_sample.py
15. For the "random_sample.py" script it will ask you to pick how many positive and negative samples you want reference the "bash commands.txt" and see the amount of samples it recommends for the particular model you choose.
16. Download from here: https://sourceforge.net/projects/opencvlibrary/files/3.4.5/opencv-3.4.5-vc14_vc15.exe/download and run the extractor, you can extract this to any folder you want.
17. Once the contents are extract navigate to the folder then go to build > x64 > vc15 > bin
18. Copy the contents of that folder to the ML-Project-Attendance-Counter
19. Next open up the "bash commands.txt" file and run the commands in order for the model you are choosing. Make sure to check the example section all the way at bottom of the file, so you can adjust your commands to run for windows. 
20. The output of your model tests will be stored in a file called "output_X.txt" where X is replaced with your type of model, which located in the root directory.
21. python3 webcam.py
22. The application would be running now, press q to take a picture of the current attendance and quit the application.

## The problem we wanted to solve.
Teachers use up valuable class time taking attendance when they could be spending more time teaching. In addition, there are several loopholes to traditional attendance systems. For example, one student can write another student’s name on an attendance sheet. At a large university with several hundred students, attendance can take a very long time if it is done at all. Generally speaking, taking roll at the beginning of class is an inconvenience that can be avoided, so we’re creating a system to solve this problem.

## Our solution and its features.
Our solution is a facial recognition software that will automate the attendance process. It will receive input from a webcam, and will simultaneously process all of the students in the classroom. Ideally, it would label each face with a name, but we acknowledge that this is a very ambitious goal for our skill sets. Without recognizing individual faces, the software counts the number of heads in the room and will notify the user how this compares to the expected number. At Florida Polytechnic, there is a webcam at the back of every classroom, which integrates with our software. This way, professors are not required to bring their own cameras or take a picture with their phones. Using OpenCV we would access the camera, and to detect objects within the room and correctly identify a person using the model we train within it. 
