# FaceCheck
This is a ready to deploy facial authentication solution built with 100% python, including the GUI. 

Built using [face_recognition](https://github.com/ageitgey/face_recognition)'s state-of-the-art face recognition built with deep learning. That project was further built on top of [dlib](http://dlib.net/). The model has an accuracy of 99.38% on the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) benchmark.

## Use Cases
- __Testing integrity in the classroom:__ Most colleges across the country manually have to scan and id students individually to prevent fradulent behavior such as having someone else take the test for them. The current solution is optimized for this task.
- __Attendance in schools:__ Because this system can identify multiple individuals in the frame of the video, the teacher can easily take attendance without manually calling out or recognizing the student.
- __Enforcing drinking laws:__ It's common for those under 21 to use another person's ID card in the hopes that the bouncer or cashier will not notice. This system prevents mistakes and bias by providing a quick and accurate authentication service.

## Features
- __Logging:__ At the end of every session a log is created so the admin can see who successfully authenticated and who attempted but failed
- __Custom Training:__ Includes modules so that training on custom data is simple.
- __Accuracy vs Speed:__ Allows for the system to be optimized for accuracy or speed

## Demo
![](demo.gif)

## Additional Notes
- Most of the code is self-explanatory or commented, but I will add a Docs section later. 
- Feel free to open an issue or a pull request if you see something wrong or an improvement!
