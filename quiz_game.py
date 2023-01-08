print ("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay!Let's play :)") 
score = 0


question1 = input("What does CPU stand for? ")
if question1.lower() == "central processing unit":
    print('True!')
    score += 1
else:
    print('False!')

question2 = input("What does GPU stand for? ")
if question2.lower() == "graphics processing unit":
    print('True!')
    score += 1
else:
    print('False!')

question3 = input("What does RAM stand for? ")
if question3.lower() == "random access memory":
    print('True!')
    score += 1
else:
    print('False!')

question4 = input("What does PSU stand for? ")
if question4.lower() == "power supply unit":
    print('True!')
    score += 1
else:
    print('False!')


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")