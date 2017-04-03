import turtle




#def draw_square(some_turtle):
#    for i in range(1,5):
#        some_turtle.forward(100)
#        some_turtle.right(90)



def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle albert and places him in the top left of the screen
    albert = turtle.Turtle()
    albert.shape("turtle")
    albert.color("red")
    albert.hideturtle()
    albert.speed(6)
    albert.left(180)
    albert.forward(350)
    albert.right(90)
    albert.forward(300)
    albert.right(90)
    albert.showturtle()
    albert.color("yellow")
    albert.speed(9)
    #
    #Draws Letter T
    albert.forward(200)
    albert.right(90)
    albert.forward(20)
    albert.right(90)
    albert.forward(90)
    albert.left(90)
    albert.forward(100)
    albert.right(90)
    albert.forward(20)
    albert.right(90)
    albert.forward(100)
    albert.left(90)
    albert.forward(90)
    albert.right(90)
    albert.forward(20)
    albert.hideturtle()
    #
    #
    #Moves albert to the next position and preps to start the second letter
    albert.right(90)
    albert.forward(200)
    albert.color("red")
    albert.forward(20)
    albert.right(90)
    albert.forward(125)
    albert.left(90)
    albert.left(77)
    albert.color("yellow")
    albert.showturtle()
    #
    #
    #Draws Letter A
    albert.forward(130)
    albert.right(77)
    albert.forward(40)
    albert.right(77)
    albert.forward(130)
    albert.right(103)
    albert.forward(32)
    albert.right(70)
    albert.forward(20)
    albert.left(70)
    albert.forward(20)
    albert.left(70)
    albert.forward(20)
    albert.right(70)
    albert.forward(32)
    albert.right(125)
    albert.color("red")
    albert.forward(70)
    albert.color("yellow")
    albert.forward(20)
    albert.right(120)
    albert.forward(20)
    albert.right(120)
    albert.forward(20)
    #
    #Places albert in position to begin third letter
    albert.color("red")
    albert.right(210)
    albert.forward(100)
    albert.left(35)
    albert.color("yellow")
    #
    #
    #Draws Letter P
    albert.left(90)
    albert.forward(130)
    albert.right(90)
    albert.forward(75)
    albert.right(90)
    albert.forward(60)
    albert.right(90)
    albert.forward(60)
    albert.left(90)
    albert.forward(70)
    albert.right(90)
    albert.forward(15)
    #
    albert.right(90)
    albert.forward(90)
    albert.right(90)
    albert.color("red")
    albert.forward(20)
    albert.color("yellow" )
    
    albert.forward(40)
    albert.left(90)
    albert.forward(20)
    albert.left(90)
    albert.forward(40)
    albert.left(90)
    albert.forward(20)
    albert.hideturtle()
    
    

    window.exitonclick()
        
draw_art()




    #
    #Create the turtle billy - draws a circle
    #billy = turtle.Turtle()
    #billy.shape("arrow")
    #billy.color("blue")
    #billy.circle(100)
    #
