questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "d"
  ],
  [
    "Which is the national language of india?", "hindi", "French", "english",
    "malayalam", "a"
  ],
  [
    "Which is the national fruit of india?", "chakka", "coconut", "mango",
    "strawberry", "c"
  ],
  [
    "Which is the national flower of india?", "rose", "lotus", "jasmine",
    "lily", "b"
  ],
  
]

levels = [1000, 2000, 3000, 5000]
money = 0
for i in range(0, len(questions)):
  
  eachquestion = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]} is :")
  print(f"\n {eachquestion[0]}")
  print(f"a. {eachquestion[1]}          b. {eachquestion[2]} ")
  print(f"c. {eachquestion[3]}          d. {eachquestion[4]} ")
  reply = (input("Enter your answer (a-d) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == eachquestion[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")