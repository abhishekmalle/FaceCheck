import faceCheck
while True:
    name = input("Enter your student id: ")

    if faceCheck.faceCheck(name):
        print("You passed!")
    else:
        print("You're not the person you say you are!")