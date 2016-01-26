# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich


peanut_butter = 10
jelly = 0
bread = 1


if jelly < 1:
	print "You need to get jelly!"
else:
	print "You have jelly!"

if peanut_butter < 1:

	print "You need to get peanut_butter!"
else: 
	print "You have peanut butter!"

if bread < 2:
	print "You need to get bread!"
else:
	print "You have bread!"



# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make


peanut_butter = 10
jelly = 0
bread = 4

number_of_bread = bread/2

sandwiches = (str)

if sandwiches > jelly:
	sandwiches = jelly
elif sandwiches > peanut_butter:
	sandwiches = peanut_butter
else:
	sandwiches = number_of_bread

print "You have enough bread to make {0} sandwiches.".format(number_of_bread)
print "You need {0} dollops of jelly and peanut butter to make your sandwiches. You have {1} jelly and {2} peanut butter.".format(number_of_bread, jelly, peanut_butter)
print "You can make {0} sandwiches.".format(sandwiches)



# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

if number_of_bread % 2 == 1 and peanut_butter > 0 and jelly > 0:

# How to say %2 OR 1 slice available???

	print "You can make an open-face sandwich."
elif number_of_bread % 2 == 0:
	print "You're eating PB & J, no bread."
else:
	print "You're going to be hungry!"



# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

if bread == 1:
	print "You can make one open-face sandwich but you need bread for a full sandwich."

if peanut_butter < 1:
	print "You need peanut butter."
else:
	print "Peanut butter is in stock."

if jelly < 1:
	print "You need jelly."
else:
	print "Jelly is in stock."




# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

if bread >= 2 and peanut_butter >= 1 and jelly < 1:
	print "You can make a peanut butter sandwich but you should take a hard, honest look at your life."

else:
	print "You can have a PB&J sandwich."
# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.





# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)

# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:
#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"

# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before

# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01_(basics)/simple_math.py

# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches

# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.
