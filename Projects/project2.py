winter_points = 1
summer_points = 1
spring_points = 1

answer1 = input ("do you prefer summer or spring?")
if answer1 == "summer":
    summer_points += 1
elif answer1 == "spring":
    spring_points += 1




answer2 = input ("do you like sledding or swimming?")
if answer2 == "sledding":
    winter_points += 1
elif answer2 == "swimming":
    summer_points+= 1


answer3 = input (" do you like snow or sun?")
if answer3 == "snow" or answer3 == "Snow":
    winter_points += 1
elif answer3 == "sun":
    summer_points += 1

answer4 = input("do you like hot chocolate or ice cream?")
if answer4 == "hot chocolate":
    winter_points += 1
elif answer4 == "ice cream":
    summer_points += 1

answer5 = input("do you like ice or snow?")
if answer5 == "ice" or answer5 == "B":
   winter_points += 1
elif answer5 == "snow":
    winter_points += 2


if winter_points >= summer_points and winter_points >= spring_points:
    print("you are a winter person")
elif summer_points > winter_points and summer_points > spring_points:
    print("you are a summer person")
elif spring_points > summer_points:
    print("you are a spring person")