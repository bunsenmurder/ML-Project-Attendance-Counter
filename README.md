# Our Project
## Directions
1. Ensure OpenCV 3.4.x, Python, and Perl are installed and within path.
2. Run the runFirst.py file found with the tar folder, it will extract all the folder ImageDB where our data set is stored.
3. Next run the crop_pos.py file next, it will crop all the positive images based on their bounding boxes and convert them to 100x128 sizes.
3. Next run the random_sample.py file, it will give you the option to set the amount of random positive and random negative samples you would like to select. Just make sure NOT to select more 435 positive samples or more than 7897 negative samples. 
4. Next open up the bash commands.txt file and run the commands in order. Make sure to follow the comments!
5. From there your trained model will be located in the classifier directory, and most likely will replace any previous models there.
6. Run the webcam.py file to see how well your model runs.

## The problem we wanted to solve.
Teachers use up valuable class time taking attendance when they could be spending more time teaching. In addition, there are several loopholes to traditional attendance systems. For example, one student can write another student’s name on an attendance sheet. At a large university with several hundred students, attendance can take a very long time if it is done at all. Generally speaking, taking roll at the beginning of class is an inconvenience that can be avoided, so we’re creating a system to solve this problem.

## Our solution and its features.
Our solution is a facial recognition software that will automate the attendance process. It will receive input from a webcam, and will simultaneously process all of the students in the classroom. Ideally, it would label each face with a name, but we acknowledge that this is a very ambitious goal for our skill sets. Without recognizing individual faces, the software counts the number of heads in the room and will notify the user how this compares to the expected number. At Florida Polytechnic, there is a webcam at the back of every classroom, which integrates with our software. This way, professors are not required to bring their own cameras or take a picture with their phones. Using OpenCV we would access the camera, and to detect objects within the room and correctly identify a person using the model we train within it. 

If the basic functionality of the software is complete, and there is still time left, the next step is to try and integrate facial identification. Once a bounding box is created around the head of each student, those faces will be processed individually, and the result will be a name of that student and confidence in the identification of that student. We could possibly use a different algorithm like a convolutional neural net, where the program will identify some faces be based on a database of student photos. If we could get this feature working for a photo that contains three or more people, we would consider that a great success. 
