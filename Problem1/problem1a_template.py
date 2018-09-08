##################################################################################
##################################################################################
## Template file for problem 1. 						##
## First, fill in your answer logic below					##
##################################################################################
#                                LOGIC GOES BELOW                     		#
##################################################################################
# first time i roll the die and store its value in a variable                    #
# then i will apply a while loop  untill i am getting the value larger than the 
# previous value after each time rolling and i will store the value in a sum variable which intialises to zero.
# and one more variable to count (intialised to 0) the number of rools if condition is following i will increase its value by 1
# else if i am getting value less than previous value i will break the loop.
# and finally return the value of sum and value of count
# i know the c++ programming language so it is difficult for me to implement it in python . 
##################################################################################
##################################################################################
## You have to fill in two functions BELOW 					##
## Both take in input n = number of sides in the die 				##
## 										##									##
## 1. findSumDieRoll(n)	: Return expected value of sum 				##
## 2. findNumberOfRolls(n)  : Return expected value of number of rolls 		##
## 										##									##
## For both, you only have to fill in the math function where indicated     	##
## 										##									##
## You can run this template file to see the output of your functions       	##
## for a 6 sided die.								##
## Simply run: `python problem1_template.py`                            	##
## You should see the output printed once your program runs.                	##
##                                                                          	##
## DO NOT CHANGE ANYTHING ELSE BELOW. ONLY FILL IN THE LOGIC.      		##
##                                                                          	##
## Good Luck!                                                               	##
##################################################################################
##################################################################################


def findSumDieRoll(n):
	
		                   ##################################
	                           ##          FILL ME IN          ##
	                           ##################################
	# n is a float
	sumRolls = n/2 # Replace me with your answer

	return round(sumRolls, 2)

def findNumberOfRolls(n):
	##################################
	##          FILL ME IN          ##
	##################################
	# n is a float
	numRolls = n/2	# Replace me with your answer

	return round(numRolls, 2)

if __name__ == "__main__":
	numberOfSides = 6.0
	sumOfRolls = findSumDieRoll(numberOfSides)
	numberOfRolls = findNumberOfRolls(numberOfSides)
	print('For a %i-sided die, expected value of sum: %.2f and number of rolls: %.2f'%(numberOfSides, sumOfRolls, numberOfRolls))
