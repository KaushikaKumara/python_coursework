###
###
###
###

#Welcoming the users’ and Initializing what this program is about and
#small guideline what the user have to do and
#how the program will work
print("*Welcome to the marks calculation software of Kaushika Kumara.")
print("*First you have to input your number of subjects and the marks of each subject.")
print("*Then you'll get five options. You can select ant of them at a time and get your results")
print("*Enjoy \n*Thank you!")
print("")


marksList = ""
while marksList.isnumeric() == False or marksList == "1" or marksList == "0":
    marksList = input("please enter your number of subjects: ")
    if marksList.isnumeric() == False:
        try: 
            a=int(marksList)
            if a<0:
                print("Please enter a positive value!")
                
        except ValueError:
            print("please enter a numeric value !!")
    
       
    if marksList == "1":
        print("There should be at least two subjects!!")
        

    if marksList == "0":
        print("There should be at least two subjects!!")
    
    
marksList = int(marksList)
#Defining a list to put the numbers according to the number count
marks = []

#setting the range for the numbers only for the number count
for i in range(marksList):
#asking the user to input each number for the number count as an integer
    mark = ""
    while mark.isnumeric() == False:
        mark= input("please enter the marks of each subject: ")
        if mark.isnumeric() == False:
            try:
                b=int(mark)
                if b<0:
                    print("please enter 0 or positive value for each subject ")
            

            except ValueError: 
                print("please enter a numeric value for your each subject ")

    #Appending the above defined numbers to the list named as marks
    marks.append(mark)
    mark = int(mark)
    



def mode(marks):
    counter=0
    num = marks[0]

    for i in marks:
        currentfrequancy = marks.count(i)
        if(currentfrequancy > counter):
            counter = currentfrequancy
            num = i
        if len(set(marks))==len(marks):
            return "there is no mode"
    return num
choice = 1
while choice != 5:
    print(marks)
    print("         ")  
    print("Please select which option do you want from the below things:\n\n1 mean of the marks\n2 median of the marks\n3 mode of the marks\n4 Enter a new set of numbers\n5 Exit the program")
    print("")
    choice = int(input(" >> "))
    print("You have choosen the choice ",choice)

    exit = "Exit"

    if choice == 1:
        print("")
        print("The sum of the marks are: ",sum(marks))
        mean = print("mean is: ", sum(marks)//len(marks))

    if choice ==2:
        print("")
        marks.sort()
        print("sorted marks are: ",marks)
        
        if len(marks) % 2 == 0:
            print("As you have even count for the marks list!! ")
            median1 = marks[len(marks)//2]
            print("Median 1 is: ",median1)
            median2 = marks[len(marks)//2 - 1]
            print("Median 2 is: ",median2)
            median = (median1 + median2)/2
        
        else:
            print("As you have odd count for the marks list!!")
            median = marks[len(marks)//2]
            
        print("Median is: " + str(median))

    if choice == 3:
        mode(marks)
        print("Mode is: ", mode(marks))
 
    if choice == 4:
       #Defining a collection of numbers and asking the user to input the count of that numbers
       marksList=int(input("please enter your number of subjects: "))
       #Defining a list to put the numbers according to the number count
       marks = []
       #setting the range for the numbers only for the number count
       for i in range(marksList):
           #asking the user to input each number for the number count as an integer
           mark=int(input("please enter the marks of each subject: ")) 
           #Appending the above defined numbers to the list named as marks
           marks.append(mark)


    if choice == 5:
        exit
        print("thnank you")
