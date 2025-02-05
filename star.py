"""A program to prompt for a CGPA score."""
#This is just a testing file.

def computegrade():


    try:
        cgpa = float(input("Enter your CGPA score: "))
        if cgpa >= 4.5 and cgpa <= 5.0:
            print("You have a first class grade.")
        elif cgpa >= 3.5 and cgpa < 4.5:
            print("You have a second class upper division.")
        elif cgpa >= 2.4 and cgpa < 3.5:
            print("You have a second class lower division.")
        elif cgpa >= 1.5 and cgpa < 2.4:
            print("You have a third class grade.")
        elif cgpa < 0.0 or cgpa > 5.0:
            print("Error!!!!,Please input a valid CGPA")
        else:
            print("You failed.")
    except ValueError:
        print("Invalid")


computegrade()