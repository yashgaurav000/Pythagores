#-------------------------#
# Author : Yash Gaurav    #
# Date : 2/4/2018         #
# Program : Pythagores    #
# Written in : Python3    #
#-------------------------#

# Main program starts here

import math,os

def pythagores():
    print("Enter x if the value is unknown")
    base = input("Enter the value of base : ")
    opp = input("Enter the value of opposite : ")
    hypo = input("Enter the value of hypotenuese : ")

    if hypo.isalpha() == True:
        base = int(base)
        opp = int(opp)
        hypo = math.sqrt((base**2)+(opp**2))
        print("The value of hypotenuese is : {}".format(hypo))

    else:
        if base.isalpha() == True:
            opp = int(opp)
            hypo = int(hypo)
            base = math.sqrt((hypo**2)-(opp**2))
            print("The value of Base is : {}".format(base))
        else:
            if opp.isalpha() == True:
                base = int(base)
                hypo = int(hypo)
                opp = math.sqrt((hypo**2)-(base**2))
                print("The value of Opposite is : {}".format(opp))
            else:
                print("All the sides are already given")
    os.system('clear')
    pythagores()

pythagores()
