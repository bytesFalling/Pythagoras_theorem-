import math
#Pythagoras theorem

#Main function
def main():

    #Displaying menu
    print ( "%s: opposite"%("1"))
    print ( "%s: Adjacent"% ("2"))
    print ( "%s: Hypotenuse"%("3") )

    #Collecting user_input
    user_input = int ( input ( "Which side would you like to find: "))

    #Validating user_input
    if ( user_input == 1 ):
        adjSide()

    if ( user_input == 2 ):
        oppSide()

    if ( user_input == 3):
        hypSide()

#Function that calculate Adjacent
def adjSide ():
    c_side = float ( input ( "Enter the Hypotenus value: "))
    a_side = float ( input ( "Enter the Opposite value: "))

    if ( a_side > c_side ):
        print ( "Imaginary value ")
    else:
        b_side = math.sqrt( pow ( c_side, 2) - pow( a_side, 2))
        print ( f"Adjacent side value is %s: "%(b_side))

#Function calculating Opposite side
def oppSide ():
    c_side = float ( input ( "Enter the Hypotenus value: "))
    b_side = float ( input ( "Enter the Adjacent value: "))

    if (  b_side > c_side ):
        print ( "Imaginary value ")
    else:
        a_side = math.sqrt( pow ( c_side, 2) - pow( b_side, 2))
        print ( f"Opposite side value is %s: "%(a_side))

#Function calculating Hpyotenus
def hypSide():
    a_side = float ( input ( "Enter the Adjacent value: "))
    b_side = float ( input ( "Enter the Opposite value: "))

    if ( b_side > a_side ):
        print ( "Imaginary value ")
    else:
        c_side = math.sqrt( pow ( a_side, 2) + pow( b_side, 2))
        print ( f"Hpyotenus side value is %s: "%(c_side))

#Calling main function
main()