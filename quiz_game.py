print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

#question 1
answer =  input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score+=1
else: 
    print("Incorrect!")
    
#question 2 
answer =  input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score+=1
else: 
    print("Incorrect!")
   
#question 3
answer =  input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score+=1
else: 
    print("Incorrect!")
    
#question 4
answer =  input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct!')
    score+=1
else: 
    print("Incorrect!")
    
print("You got " + str(score) + "/4 questions correct!" , end= " ")
print("thats " + str((score/4) *100), "%!")