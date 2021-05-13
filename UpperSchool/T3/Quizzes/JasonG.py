value= 0
print("This quiz will determine what kind of \nchacter you are from spongebob!!!")
number = 1
while number < 11:
# Question 1
    if number == 1: 
        print()
        print("When you go out with friends, who are you?: ")
        print("- The partier (1)")
        print("- The chill one (2)")
        print("- The sleepy one (3)")
        print("- The one who doesn't show up (4)")
# Question 2
    elif number == 2:
        print()
        print("If you could eat one of these, \nwhich would you chose?: ")
        print("- Pizza (1)")
        print("- PB&J(2)")
        print("- Crackers (3)")
        print("- Salad (4)")
# Question 3
    elif number == 3:
        print()
        print("Do you like to travel?: ")
        print("- Yes, it's my fav! (1)")
        print("- I don't mind it... (2)")
        print("- I'll do it if I have to (3)")
        print("- I like to stay home (4)")
# Question 4
    elif number == 4:
        print()
        print("Fav cookies!?: ")
        print("- Safeway cookies (1)")
        print("- Snickerdoodle (2)")
        print("- Peanut butter (3)")
        print("- I'm a biscuit person (4)")
# Question 5
    elif number == 5:
        print()
        print("What is your fav season?: ")
        print("- Summer (1)")
        print("- Winter (2)")
        print("- Spring (3)")
        print("- Fall (4)")
# Question 6
    elif number == 6:
        print()
        print("What is your best subject in school?: ")
        print("- English (1)")
        print("- Math (2)")
        print("- P.E. (3)")
        print("- Music (4)")
# Question 7
    elif number == 7:
        print()
        print("What is your favorite weather?: ")
        print("- Sun (1)")
        print("- Snow (2)")
        print("- Cloudy (3)")
        print("- Rain (4)")
# Question 8
    elif number == 8:
        print()
        print("What is your favorite thing in nature?: ")
        print("- Butterflies (1)")
        print("- Flowers (2)")
        print("- Bushes (3)")
        print("- Thorns (4)")
# Question 9
    elif number == 9:
        print()
        print("Who is your favorite marvel character?: ")
        print("- Spider man (1)")
        print("- Hulk (2)")
        print("- Black Widow (3)")
        print("- Deadpool (4)")
# Question 10
    elif number == 10:
        print()
        print("What Harry Potter house do you \nthink you fit into most?: ")
        print("- Gridvendor (1)")
        print("- Hufflepuff (2)")
        print("- Ravenclaw (3)")
        print("- Slytherin (4)")
    answer = int(input("Enter the number correlated to what fits you best: "))
    if answer == 1:
        value = value + 1
    elif answer == 2:
        value = value + 2
    elif answer == 3:
        value = value + 3
    elif answer == 4:
        value = value + 4
    else:
        value = value + 100
    number = number + 1 

# Final Decision
print()
if value < 15:
    print("Spongebob - You the the craziest of the group. You're \nthe one who doesn't really care what other think, \nbut you do what you love. You have a lot of frineds but \nnot many close friends but the ones who are close to \nyou will stay forever. ")
elif value < 25:
    print("Patrick - You are super goofy and loved by all. You \ntry to make people happy and don't care too much of \nwhat other think of you.")
elif value < 35:
    print("Gary - You're the quite introvert of the group. You \noften times don't speak up but when you do you have \nsomething very important to say.")
elif value < 45:
    print("Squidward - You're the pessimist of the friend group, \nand you don't try to make friends easily. When people \nask you how your day was, you often reply with \n'It's ok' and nothing more.")
