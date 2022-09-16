from datetime import datetime
import random


data = [] #list that holds all the questions
correct_solutions = 0 #number of correct questions user has solved, running counter
finished_all_questions = False #flag to hold whether or not all of the questions have been solved

#populate data with all the unique combinations of numbers
for x in range(1,11):
    for y in range(x,11):
        data.append((str(x)+"x"+str(y)))


print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("----------------MATH------------------")
print ("-------------CHALLENGE----------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print ("--------------------------------------")
print("")
val = input ("Are you ready to kick mass ath?" )
print("")
print("Let's go then. I will start the timer at 5 minutes. You must answer 80% of ALL questions correctly.")
print("")
val = input ("Press Enter to go ")
print("Good luck superstar!")


starttime = datetime.now()
endtime = starttime

#find length of list to calculate the grade
data_length = len(data)

#Loop until endtime - starttime > 5 minutes
while ((endtime - starttime).seconds < 300):
    #pick random element from list and remove
    current_question = random.choice(data)
    data.remove(current_question)

    #calculate answer by splitting and calculating
    splitting = current_question.split('x')
    answer = int(splitting[0])*int(splitting[1])

    isalpha = True
    user_answer = 0
    #print element and get answe
    while (isalpha):
        user_answer = input(current_question+": ")
        try:
            int(user_answer)
            isalpha = False
        except ValueError:
            isalpha = True


    #check if answer is correct, if so add 1 to variable
    if int(user_answer) == answer:
        correct_solutions += 1

    #check if list is empty, if so leave loop and set flag to true
    if len(data) == 0:
        finished_all_questions = True
        break

    endtime = datetime.now()

#calculate score
howyoudid = correct_solutions*100/data_length
formatted_float_value = "{:.2f}".format(howyoudid)

if finished_all_questions == False:
    print("TIMES UP!")
    print("You got "+formatted_float_value+"%")
else:
    print("All done in time!")
    print("You got "+formatted_float_value+"%")
