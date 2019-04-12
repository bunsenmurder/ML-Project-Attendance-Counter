## Dependencies: 
- OpenCV 3.4.X
- Perl 5.x.x
- Python 3.6.X

## Directions For Linux 
1. Follow the "INSTALLING OPENCV ON UBUNTU.txt" for install instructions of dependances on Linux.
2. git clone git@github.com:bunsenmurder/ML-Project-Attendance-Counter.git
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

## Directions for Windows
1. Check the "Directions for Windows.txt" for how to run on a Windows Machine.

## The problem we wanted to solve.
Teachers use up valuable class time taking attendance when they could be spending more time teaching. In addition, there are several loopholes to traditional attendance systems. For example, one student can write another student’s name on an attendance sheet. At a large university with several hundred students, attendance can take a very long time if it is done at all. Generally speaking, taking roll at the beginning of class is an inconvenience that can be avoided, so we’re creating a system to solve this problem.

## Our solution and its features.
Our solution is a facial recognition software that will automate the attendance process. It will receive input from a webcam, and will simultaneously process all of the students in the classroom. Ideally, it would label each face with a name, but we acknowledge that this is a very ambitious goal for our skill sets. Without recognizing individual faces, the software counts the number of heads in the room and will notify the user how this compares to the expected number. At Florida Polytechnic, there is a webcam at the back of every classroom, which integrates with our software. This way, professors are not required to bring their own cameras or take a picture with their phones. Using OpenCV we would access the camera, and to detect objects within the room and correctly identify a person using the model we train within it. 

If the basic functionality of the software is complete, and there is still time left, the next step is to try and integrate facial identification. Once a bounding box is created around the head of each student, those faces will be processed individually, and the result will be a name of that student and confidence in the identification of that student. We could possibly use a different algorithm like a convolutional neural net, where the program will identify some faces be based on a database of student photos. If we could get this feature working for a photo that contains three or more people, we would consider that a great success. 
