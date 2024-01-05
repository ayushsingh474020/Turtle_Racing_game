import turtle as t
import random
color_list=["violet","blue","green","yellow","orange","red"]
turtle_list=["violet","blue","green","yellow","orange","red"]
x_distances=[-300,-300,-300,-300,-300,-300]
distances=[10,20,30,40,50]
screen=t.Screen()
for i in range(len(turtle_list)):
    turtle_list[i]=t.Turtle()
    turtle_list[i].shape("turtle")


screen.canvheight=600
screen.canvwidth=600

def start():
    user_choice=screen.textinput("Make a Bet", "Choose a Turtle")
    max_dist=-300
    for i in range(len(turtle_list)):
        turtle_list[i].penup()
        y_pos=240-80*i
        turtle_list[i].color(color_list[i])
        turtle_list[i].goto(-300,y_pos)
    while(max_dist<360):
        for i in range(len(turtle_list)):
            dist = random.choice(distances)
            turtle_list[i].forward(dist)
            x_distances[i] += dist
            if (max_dist < x_distances[i]):
                max_dist = x_distances[i]
            if (x_distances[i] >= 360):
                if(user_choice==color_list[i]):
                    print("Your Turtle Won!!")
                else:
                    print(f"{color_list[i]} Won!")

                return


screen.listen()
screen.onkey(fun=start,key="space")
screen.exitonclick()