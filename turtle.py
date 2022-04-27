import turtle
import random

#Setting the players appearance
turtle.title("Racing Game")
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.shapesize(2.0,2.0,2)
player_one.penup()
player_one.goto(-200,100)
player_two = turtle.Turtle()
player_two.color("purple")
player_two.shape("turtle")
player_two.shapesize(2.0,2.0,2)
player_two.penup()
player_two.goto(-200,-100)
turtle.bgcolor("pink")


#Moving the players initially
player_one.goto(300,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)
player_two.goto(300,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

#creating the die
die = [1,2,3,4,5,6]

# Main Game loop

for i in range(20):
     if player_one.pos() >= (300,100):
             print("Player One Wins!")
             break
     elif player_two.pos() >= (300,-100):
             print("Player Two Wins!")
             break
     else:
             player_one_turn = input("Press 'Enter' to roll the die ")
             die_outcome = random.choice(die)
             print("The result of the die roll is: ")
             print(die_outcome)
             print("The number of steps will be: ")
             print(20*die_outcome)
             player_one.fd(20*die_outcome)
             player_two_turn = input("Press 'Enter' to roll the die ")
             die_outcome = random.choice(die)
             d = random.choice(die)
             print("The result of the die roll is: ")
             print(die_outcome)
             print("The number of steps will be: ")
             print(20*die_outcome)
             player_two.fd(20*die_outcome)
