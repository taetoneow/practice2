types_of_people = 10 #a defined variable of 10 people
x = f"There are {types_of_people} types of people." #this is a formatted string
binary = "binary" #a defined variable of binary, self defined
do_not = "don't" #a defined variable of a contraction that doesn't need a escape character because it is in a string with different quote marks
y = f"Those who know {binary} and those who {do_not}." #A formatted string 
print(x) #a print command for (x)
print(y) #a print command for (y)
print(f"I said: {x}.") #a formatted string within a string for (x)
print(f"I also said: '{y}'") #a formatted string within a string for (y)
hilarious =  False
joke_evaluation = "Isn't that joke so funny? {}"





print(joke_evaluation.format(hilarious))
hilarious =  False
w = "This is the left side of..." # a string
e = 'a string with a right side.' # a string
print(w + e) #a string plus a string