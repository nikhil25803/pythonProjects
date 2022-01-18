import random

def ask_number(nb_min,nb_max):
    #no error management
    number_int=0;
    while number_int==0:
        number_str=input(f"What is the magic number between {nb_min} and {nb_max} ? ")
        try:
            number_int=int(number_str)
        except:
            print("Error")

        else:

            if number_int<nb_min or number_int>nb_max:
                print(f"Enter a number between {nb_min} and {nb_max}")
    return int(number_str)



MIN_NUMBER=1
MAX_NUMBER=10
MAGIC_NUMBER=random.randint(MIN_NUMBER,MAX_NUMBER)
nb_lives=4

number=0;
lives=nb_lives
while not number==MAGIC_NUMBER:
    print(f"You have {lives} remaining")
    number=ask_number(MIN_NUMBER,MAX_NUMBER)

    if number==MAGIC_NUMBER:    
        print("You Win")
    elif number>MAGIC_NUMBER:   
        print("The magic number is lower")
        lives-=1
    else:
        print("The magic number is greater")