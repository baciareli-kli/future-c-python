import datetime #ukradzione z https://www.w3schools.com/python/python_datetime.asp 
x = datetime.datetime.now() 
currentYear = int(x.strftime("%Y")) 
print(type(currentYear)) 
welcomeMessage = '''Hi, 
Do you want to create a birthday card for someone?  
''' 
firstWarnningMessage = 'Choose your destiny: Y or N. There is no more option. Trust me....Third option does not compute.' 
birthdayCard = input(welcomeMessage + 'Please press y/n: ') 

while birthdayCard != 'y' and birthdayCard !='n': 
    birthdayCard = input(firstWarnningMessage + 'Please press y/n: ') 


if birthdayCard == 'y': 

    userName = input('''Epic! There is no time to waste! What is the name of the mastermind behind this card? We need to sign the card somehow ''') 
    userName = userName.capitalize()
    dateOfbirth = input (userName  +' I hope that you remember the year of your friends birth? Please provide in YYYY format: ') 
    #giga przydatne bo inaczej pętla była https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_isnumeric
    while dateOfbirth.isnumeric() == False: 
            dateOfbirth = input(f'Dear {userName}, we do not know this system of numbers that you provide. Please use the decimal system that we use on Earth: ') 
    dateOfbirth = int(dateOfbirth) 
    age = currentYear - dateOfbirth 
    while age>111 or age<1 or type(age) != int: 
        print(f"Are you sure that your friend has {age}? You know because {currentYear} - {dateOfbirth} gives us: {age} + ... Let's try again.") 
        dateOfbirth = input ("Here we go again ... Please provide year in YYYY format: ") 
        dateOfbirth = int(dateOfbirth) 
        age = currentYear - dateOfbirth 
    friendName = input("Ops, we forgot about your friend's name, Please provide it: ") 
    friendName = friendName.capitalize()
    addNote= 1

    cardNote = input("Be sure no mistake there is no erase or return option what you will write this will be sent, let's show that you focus and spend energy for this card: ") 
    print ('''P E R F E C T ! 
    here is the version that we send! 
    ''') 
    while addNote == 1:
        addNoteAnswer = input ("Do you want to add new line? Please provide y/n (i am to lazy to add another validation): ")
        if addNoteAnswer == "y":
            cardNote = cardNote + '\n' + input("Awaiting for new line")
         

    print(f'{friendName}, \n Wszystkeigo najlepszego z okazji {str(age)} urodzin! \n {cardNote} \n {userName}')