#Snake Game

from tkinter import *
import random 

#Framework size and color
GAME_WIDTH = 800
GAME_HEIGHT = 500
SPEED = 100
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "blue"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "black"

#Snake setup
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0 , BODY_PARTS):
            self.coordinates.append([0,0])

        for x , y in self.coordinates:
            square = canvas.create_rectangle(x , y , x + SPACE_SIZE , y + SPACE_SIZE , fill=SNAKE_COLOR , tag="snake")
            self.squares.append(square)


#Food setup
class Food:
    def __init__(self):
        
        #create random food in the game spaces
        x = random.randint(0 , int((GAME_WIDTH/SPACE_SIZE)-1))*SPACE_SIZE
        y = random.randint(0 , int((GAME_HEIGHT/SPACE_SIZE)-1))*SPACE_SIZE

        self.coordinates = [x , y]

        #Draw food
        canvas.create_oval(x , y , x + SPACE_SIZE , y + SPACE_SIZE , fill=FOOD_COLOR , tag="food")


#Create snake directions
def nextTurn(snake , food):
    #Head of Snake
    x , y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE

    elif direction == "down":
        y += SPACE_SIZE

    elif direction == "left":
        x -= SPACE_SIZE

    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0 , (x , y))

    square = canvas.create_rectangle(x , y , x + SPACE_SIZE , y + SPACE_SIZE , fill=SNAKE_COLOR)

    snake.squares.insert(0 , square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if checkCollisions(snake):
        gameOver()

    else:
        window.after(SPEED , nextTurn , snake , food)

def changeDirection(newDirection):

    global direction

    if newDirection == 'left':
        if direction != 'right':
            direction = newDirection

    elif newDirection == 'right':
        if direction != 'left':
            direction = newDirection

    elif newDirection == 'down':
        if direction != 'up':
            direction = newDirection

    elif newDirection == 'up':
        if direction != 'down':
            direction = newDirection

#Make collision in game (GAME OVER)
def checkCollisions(snake):
    
    x , y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True


def gameOver():
    canvas.delete(ALL)

    canvas.create_text(canvas.winfo_width()/2 , canvas.winfo_height()/2 , font=('consolas' , 70) , text="GAME OVER" , fill="red" , tag="GAME OVER")

#Make the game adress
window = Tk()
window.title("SNAKE GAME")
window.resizable(False , False)

score = 0
direction = 'down'

#Make score int the top of the window
label = Label(window , text="Score:{}".format(score) , font=('consolas' , 40))
label.pack()

canvas = Canvas(window , bg = BACKGROUND_COLOR , height = GAME_HEIGHT , width = GAME_WIDTH)
canvas.pack()

window.update()

#Make window in the midlle of screeen
windowWidth = window.winfo_width()
windowHeight = window.winfo_height()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth / 2) - (windowWidth / 2))
y = int((screenHeight / 2) - (windowHeight / 2))

window.geometry(f"{windowWidth}x{windowHeight}+{x}+{y}")

#set buttons to change direction
window.bind('<Right>', lambda event: changeDirection('right'))
window.bind('<Left>', lambda event: changeDirection('left'))
window.bind('<Up>', lambda event: changeDirection('up'))
window.bind('<Down>', lambda event: changeDirection('down'))

snake = Snake()
food = Food()

nextTurn(snake , food)

window.mainloop()