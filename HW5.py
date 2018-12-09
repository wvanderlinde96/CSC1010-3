# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time
Names = ['Danielle', 'Reggie', 'Christian', 'Riley']
print(Names[-1])
print(Names[-3])
print(Names[-2])
print(Names[-4])

#3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name
names = ['Danielle', 'Reggie', 'Christian', 'Riley']
msg = "Hi, " + names[-1].title() + " How are you?"
print(msg)
msg = "Hi, " + names[-2].title() + " How are you?"
print(msg)
msg = "Hi, " + names[-3].title() + " How are you?"
print(msg)
msg = "Hi, " + names[-4].title() + " How are you?"
print(msg)

#3-3. Your Own List: Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”
cars = ['Caddy Fleetwood', 'Chevy K10', 'Buick Roadmaster', 'Chevy Impala SS']
message = "I would love to own a " + cars[1].title() + "."
print(message)
message = "I would love to own a " + cars[2].title() + "."
print(message)
message = "I would love to own a " + cars[3].title() + "."

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner
list = ['Danielle', 'Reggie', 'Christian']
message = "Would you like to come to dinner " + list[-1].title() + "?"
print(message)
message = "Would you like to come to dinner " + list[-2].title() + "?"
print(message)
message = "Would you like to come to dinner " + list[-3].title() + "?"
print(message)
# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite
# Invite some people to dinner.
# Invite some people to dinner.
guests = ['Danielle', 'Reggie', 'Christian']
name = guests[0].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print(name + ", please come to dinner.")
name = guests[2].title()
print(name + ", please come to dinner.")
name = guests[1].title()
print("\nSorry, " + name + " can't make it tonight.")
del(guests[1])
guests.insert(1, 'Leslie')
name = guests[0].title()
print("\n" + name + ", please come tonight for dinner.")
name = guests[1].title()
print(name + ",  come to dinner.")
name = guests[2].title()
print(name + ",  come to dinner.")

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# Store the locations in a list. Make sure the list is not in alphabetical order.
#  Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.
#  Use sorted() to print your list in alphabetical order without modifying the
# actual list.
#  Show that your list is still in its original order by printing it.
#  Use sorted() to print your list in reverse alphabetical order without changing
# the order of the original list.
#  Show that your list is still in its original order by printing it again.
#  Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
#  Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.
#  Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
#  Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
locations = ['Hong Kong', 'Tijuana', 'Juarez', 'Bern', 'Germany']
print("Original order:")
print(locations)
print("\nAlphabetical:")
print(sorted(locations))
print("\nOriginal order:")
print(locations)
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))
print("\nOriginal order:")
print(locations)
print("\nReversed:")
locations.reverse()
print(locations)
print("\nOriginal order:")
locations.reverse()
print(locations)
print("\nAlphabetical")
locations.sort()
print(locations)
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner
guests = ['Danielle', 'Reggie', 'Christian']
len(guests)

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
pizzas=['deep dish', 'peperroni', 'sausage']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(pizza.title() + ", that was a delicious pizza!")
for pizza in pizzas:
    print(pizza.title() + ", that was a great pizza!")
    print("I can't wait to eat more " + pizza.title() + ".\n")
# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal
animals=['dogs', 'cats', 'octopus']
for animal in animals:
    print(animal)
for animal in animals:
    print(animal.title() + " all have legs.")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive
numbers = list(range(1, 20))
for number in numbers:
    print(number)
#4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers
numbers = list(range(1, 1000000))
for number in numbers:
    print(number)
# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list
threes = list(range(3, 31, 3))
for number in threes:
    print(number)threes = list(range(3, 30)

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this
    car = 'subaru'
    print("Is car == 'subaru'? I predict True.")
    print(car == 'subaru')
    print("\nIs car == 'audi'? I predict False.")
    print(car == 'audi')
#
