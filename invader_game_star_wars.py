import turtle
import random

"""
    Constants and variables
"""

# General parameters
window_height = 600
window_width = 800
window_margin = 50
update_interval = 25    # The screen update interval in ms, which is the
score = 0                        # interval of running the updatescreen function
bonuschk=1

# Player's parameters
player_size = 50        # The size of the player image plus margin
player_init_x = 0
player_init_y = -window_height / 2 + window_margin
player_speed = 10       # The speed the player moves left or right

score_display = turtle.Turtle()
score_display.up()
score_display.goto(-280,280)
score_display.color("white")
score_display.hideturtle()

# Enemy's parameters
enemy_number = 18       # The number of enemies in the game

enemy_size = 50         # The size of the enemy image plus margin
bonusenemy_size= 30
enemy_init_x = -window_width / 2 + window_margin
enemy_init_y = window_height / 2 - window_margin - 70
enemy_min_x = enemy_init_x
enemy_max_x = window_width / 2 - enemy_size * 6
bonusenemy_init_x= (window_width / 2) - window_margin
bonusenemy_init_y = window_height / 2 - window_margin
bonusenemy_max_x = - ( window_width / 2 - bonusenemy_size * 6 )
    # The maximum x coordinate of the first enemy, which will be used
    # to restrict the x coordinates of all other enemies
enemy_kill_player_distance = 35
    # The player will lose the game if the vertical
    # distance between the enemy and the player is smaller
    # than this value
stopenemy=0
# Enemy movement parameters
enemy_speed = 2
enemy_speed_increment = 1
bonusenemy_speed= 2.5    # The increase in speed every time the enemies move
    # across the window and back
enemy_direction = 1
bonusenemy_direction=-1
    # The current direction the enemies are moving:
    #     1 means from left to right and
    #     -1 means from right to left

# The list of enemies
enemies = []

# Laser parameter
laser_width = 2
laser_height = 15
laser_speed = 20
laser_kill_enemy_distance = 20
    # The laser will destory an enemy if the distance
    # between the laser and the enemy is smaller than
    # this value
turtle.addshape("enemyship.gif")
bonusenemy = turtle.Turtle()
bonusenemy.shape("enemyship.gif")
bonusenemy.up()
bonusenemy.goto(bonusenemy_init_x, bonusenemy_init_y)
bonusenemy.hideturtle()
    
def bonus():
#   bonusenemy.goto(bonusenemy_init_x, bonusenemy_init_y)
    global bonuschk
    bonuschk=1
    bonusenemy.showturtle()
    


# This function is run when the "Left" key is pressed. The function moves the
# player to the left when the player is within the window area
def playermoveleft():

    # Get current player position
    x, y = player.position()

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range
    if x - player_speed > -window_width / 2 + window_margin:

        player.goto(x - player_speed, y)

# This function is run when the "Right" key is pressed. The function moves the
# player to the right when the player is within the window area
def playermoveright():

    # Get current player position
    x, y = player.position()
    if x + player_speed < window_width / 2 - window_margin:

    # Part 2.2 - Keeping the player inside the window
    # Player should only be moved only if it is within the window range

        player.goto(x + player_speed, y)

    

"""
    Handle the screen update and enemy movement
"""
def stopenemies():
    global stopenemy
    if stopenemy == 0:
        stopenemy = 1
    else:
        stopenemy=0

# This function is run in a fixed interval. It updates the position of all
# elements on the screen, including the player and the enemies. It also checks
# for the end of game conditions.
def updatescreen():
    # Use the global variables here because we will change them inside this
    # function
    global enemy_direction, enemy_speed
    global score, stopenemy, bonuschk
    
    
    
    # Move the enemies depending on the moving direction

    # The enemies can only move within an area, which is determined by the
    # position of 1st enemy at the top left corner, enemy_min_x and enemy_max_x

    # x and y displacements for all enemies
    dx = enemy_speed * enemy_direction
    dy = 0

    # Part 3.3
    # Perform several actions if the enemies hit the window border
    x0= enemies[0].xcor()
    #score_display.clear()
    #score_display.write(" SCORE: " + str(score), font=("System", 12, "bold"))
    
    if x0 + dx> enemy_max_x or x0 +dx <enemy_min_x:
    

        # Switch the moving direction
        enemy_direction = -1* enemy_direction 

        # Bring the enemies closer to the player
        dy = -enemy_size / 2

        # Increase the speed when the direction switches to right again
        if enemy_direction == 1:
            enemy_speed= enemy_speed + enemy_speed_increment

    
    
        
       
                 
   
            

    # Move the enemies according to the dx and dy values determined above
    turtle.onkeypress(stopenemies, "c" )
    turtle.listen()
    if stopenemy == 0:
        for enemy in enemies:
            x, y = enemy.position()
            enemy.goto(x + dx, y + dy)
            if(x//20)%2 == 0 : ## // gives pure integer
                enemy.shape("enemy.gif")
            else:
                enemy.shape("enemy2.gif")
        xpos, ypos= bonusenemy.position()
        if bonuschk==1:
            
            if xpos-bonusenemy_speed> bonusenemy_max_x:
                bonusenemy.hideturtle()
                bonusenemy.goto( xpos - bonusenemy_speed,bonusenemy_init_y )
                bonusenemy.showturtle()
            else:
                bonusenemy.hideturtle()
           
    # Part 4.3 - Moving the laser
    # Perform several actions if the laser is visible
    
    if laser.isvisible():
        # Move the laser forward
        laser.forward(laser_speed)        

        # Hide the laser if it goes beyond the window
        if laser.ycor()>= window_height/2:
            laser.hideturtle()
            
        

        # Check the laser against every enemy using a for loop
        for enemy in enemies:
            # If the laser hits a visible enemy, hide both of them
            if enemy.isvisible() and laser.distance(enemy)< laser_kill_enemy_distance:
                enemy.hideturtle()
                laser.hideturtle()
                score = score + 20
                score_display.clear()
                score_display.write(" SCORE: " + str(score), font=("System", 12, "bold"))

                # Stop if some enemy is hit
                break
        box, boy= bonusenemy.position()
        if box-bonusenemy_speed > bonusenemy_max_x:
            if bonusenemy.isvisible() and laser.distance(bonusenemy)< laser_kill_enemy_distance:
                bonusenemy.hideturtle()
                laser.hideturtle()
                score = score + 100
                bonuschk=0
                score_display.clear()
                score_display.write(" SCORE: " + str(score), font=("System", 12, "bold"))
                bonusenemy.goto(bonusenemy_init_x, bonusenemy_init_y)
                
                turtle.ontimer(bonus, 5000)
        else:
            bonusenemy.hideturtle()
            bonusenemy.goto(bonusenemy_init_x, bonusenemy_init_y)
            bonuschk=0
            turtle.ontimer(bonus, 5000)
            
       
        
        
        
    # Part 5.1 - Gameover when one of the enemies is close to the player

    # If one of the enemies is very close to the player, the game will be over
    for enemy in enemies:
        if enemy.ycor()-player.ycor() < enemy_kill_player_distance:
            # Show a message
            gameover("You lose!")

            # Return and do not run updatescreen() again
            return

    # Part 5.2 - Gameover when you have killed all enemies

    # Set up a variable as a counter
    count = 0

    

    # For each enemy
    for enemy in enemies:
        if enemy.isvisible():
        # Increase the counter if the enemy is visible
            count+=1

    # If the counter is 0, that means you have killed all enemies
    if count == 0:

        # Perform several gameover actions
        gameover("You win!")

        return    

    # Part 3.2 - Controlling animation using the timer event
    turtle.update()
    
   
    turtle.ontimer(updatescreen,update_interval)
   
    

"""
    Shoot the laser
"""

# This function is run when the player presses the spacebar. It shoots a laser
# by putting the laser in the player's current position. Only one laser can
# be shot at any one time.
def shootlaser():

    

    # Part 4.2 - the shooting function
    # Shoot the laser only if it is not visible
    #if laser is invisible, make it visible and move it to the player turtle's
    # position 
    n = random.randint(0,1)
    lasercolor= [ "red","blue"]
    if laser.isvisible() == False:
        laser.color(lasercolor[n]  )
        laser.showturtle()

        x, y = player.position()
        laser.goto(x,y) 
        

"""
    Game start
"""
# This function contains things that have to be done when the game starts.
def gamestart(x,y):
    # Use the global variables here because we will change them inside this
    # function
    global player, laser, score
    
    
    score_display.write(" SCORE: " + str(score), font=("System", 12, "bold"))
    #hide all GUI components

    start_button.hideturtle()
    start_button.clear()
    labels.clear()
    left_arrow.hideturtle()
    right_arrow.hideturtle()
    enemy_number_text.clear()
    enemy_number_text.hideturtle()
    welcome.hideturtle()
    welcome.clear()   
    ### Player turtle ###
    turtle.bgpic("bggame.gif")

    # Add the spaceship picture
    turtle.addshape("spaceship.gif")

    # Create the player turtle and move it to the initial position
    player = turtle.Turtle()
    player.shape("spaceship.gif")
    player.up()
    player.goto(player_init_x, player_init_y)

    # Part 2.1
    # Map player movement shandlers to key press events
    
    turtle.onkeypress(playermoveleft, "Left")
    turtle.onkeypress(playermoveright, "Right")

    turtle.listen()

    ### Enemy turtles ###

    # Add the enemy picture
    turtle.addshape("enemy.gif")
    turtle.addshape("enemy2.gif")
    # bonus enemy creation
    turtle.addshape("enemyship.gif")
    bonusenemy = turtle.Turtle()
    bonusenemy.shape("enemyship.gif")
    bonusenemy.up()
    bonusenemy.hideturtle()
    #bonusenemy.goto( bonusenemy_init_x - bonusenemy_size, bonusenemy_init_y )
    
    
    for i in range(enemy_number):
        # Create the turtle for the enemy
        enemy = turtle.Turtle()
        enemy.shape("enemy.gif")
        enemy.up()

        
        # Move to a proper position counting from the top left corner
        enemy.goto(enemy_init_x + enemy_size * (i % 7), enemy_init_y - enemy_size * (i // 7))
        #turtle.ontimer(updatescreen, 5000)
        
        # Add the enemy to the end of the enemies list
        enemies.append(enemy)
  
   
    
            
            


    ### Laser turtle ###

    # Create the laser turtle using the square turtle shape
    laser = turtle.Turtle()
    laser.shape("square")
    

    # Change the size of the turtle and change the orientation of the turtle
    laser.shapesize(laser_width / 20, laser_height / 20)
    laser.left(90)
    laser.up()

    # Hide the laser turtle
    laser.hideturtle()

    # Part 4.2 - Mapping the shooting function to key press event

    turtle.onkeypress(shootlaser, "space")

    turtle.update()

    # Part 3.2 - Controlling animation using the timer event

    turtle.ontimer(updatescreen,update_interval)
    #turtle.ontimer( bonus, 5000)


"""
    Game over
"""

# This function shows the game over message.
def gameover(message):

    # Part 5.3 - Improving the gameover() function
    gameover_turtle= turtle.Turtle()
    gameover_turtle.hideturtle()
    turtle.addshape("yoda.gif")
    gameover_turtle.shape("yoda.gif")
    gameover_turtle.pencolor("yellow")
    gameover_turtle.up()
    #gameover_turtle.goto(-50,-100)
    #gameover_turtle.down()
    gameover_turtle.write(message, align="center", font=("System", 30, "bold"))
   
    
    gameover_turtle.showturtle()    
    turtle.update()
    

    

    

"""
    Set up main Turtle parameters
"""

# Set up the turtle window
turtle.setup(window_width, window_height)
turtle.bgcolor("black")


turtle.up()
turtle.hideturtle()
turtle.tracer(False)

# Start the game
turtle.bgpic("bggame.gif")
message= "\t\t\t\tSTAR WARS\t\t\nWelcome cadets! To save our galaxy, you must kill all the stormtroopers with your lightsabers. \n \
Press left and right arrow keys to move your spaceship and speacebar to shoot the laser.\n\t\t For each enemy, earn 20 pts and for each bonus enemy earn 100 pts.\n\t\t \t To pause enemies, press 'c'\n \t \t \t MAY THE FORCE BE WITH YOU\n"
welcome = turtle.Turtle()
welcome.color("yellow","")
welcome.hideturtle()


welcome.write(message, font=("ariel",12,"bold"), align="center")  
start_button = turtle.Turtle()
start_button.onclick(gamestart)
#turtle.bgcolor("black")
start_button.color("white")
# Draw the button

start_button.up()
start_button.goto(-40, -40)
start_button.color("", "yellow")
start_button.begin_fill()
for _ in range(2):
    start_button.forward(80)
    start_button.left(90)
    start_button.forward(25)
    start_button.left(90)
start_button.end_fill()

start_button.color("black")
start_button.goto(0, -35)
start_button.write("Start", font=("System", 16, "bold"), align="center")
#resize variable to cover button drawn
start_button.goto(0, -28)
start_button.shape("square")
start_button.shapesize(1.25, 4)
# make start button trasnparent
start_button.color("")

#GUI components go here
#3.1.1 create text label
labels= turtle.Turtle()
labels.hideturtle()
labels.pencolor("white")
labels.up()
labels.goto(-100, 0) # Put the text next to the spinner control
labels.write("Number of Enemies:", font=("System", 12, "bold"))

#3.1.2 create a label to display no of enemies

enemy_number_text = turtle.Turtle()
enemy_number_text.hideturtle()
enemy_number_text.pencolor("white")
enemy_number_text.up()
enemy_number_text.goto(80,0)
enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
# create turtle for left/right arrow
left_arrow= turtle.Turtle()
left_arrow.shape("arrow")
left_arrow.color("white")
left_arrow.shapesize(0.5,1)
left_arrow.left(180)
left_arrow.up()
left_arrow.goto(60,8)

right_arrow= turtle.Turtle()
right_arrow.shape("arrow")
right_arrow.color("white")
right_arrow.shapesize(0.5,1)
right_arrow.up()
right_arrow.goto(100,8)


#3.3.2 creating event handler for arrows
def decrease_enemy_number(x,y):
    global enemy_number
    if enemy_number>1:
        enemy_number-=1

    enemy_number_text.clear()
    enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
    
    
def increase_enemy_number(x,y):
    global enemy_number
    if enemy_number<48:
        enemy_number+=1
        enemy_number_text.clear()
        enemy_number_text.write(str(enemy_number), font=("System", 12, "bold"), align="center")
    
    

left_arrow.onclick(decrease_enemy_number)
right_arrow.onclick(increase_enemy_number)


turtle.update()


# Switch focus to turtle graphics window
turtle.done()
#def main():
 #   bonus()
    
    
