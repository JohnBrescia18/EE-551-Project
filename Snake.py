# Snake
# Author: John Brescia
#

import random
import pygame
import tkinter as tk
from tkinter import messagebox
from tkinter import *




class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        self.pos = start    #position of the snake at the start
        self.dirnx = 1      #have the snake move to the right at the start
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0] #rows
        j = self.pos[1] #colums

        pygame.draw.rect(surface, self.color, (i * dis + 1, j * dis + 1, dis - 2, dis - 2)) #Makes the snake draw sligthly inside of the grid so that the grid is still visible.
        if eyes:    #if eyes is true (Only on the Head)
            centre = dis // 2
            radius = 3  #size of the eyes
            circleMiddle = (i * dis + centre - radius, j * dis + 8) # Left Eye
            circleMiddle2 = (i * dis + dis - radius * 2, j * dis + 8) # Right Eye
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle, radius) #Drawing Both Eyes on the Head of the snake
            pygame.draw.circle(surface, (0, 0, 0), circleMiddle2, radius)


class snake(object):
    body = []  #to keep track of the body
    turns = {} #to keep track of where the snake turned

    def __init__(self, color, pos):
        self.color = color          #color of the snake
        self.head = cube(pos)       #head is where the current location of the snake
        self.body.append(self.head) #body is the after the snake
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]: #if the left arrow key is pressed go to the left
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_RIGHT]: #if the right arrow key is pressed go to the left
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]: #if the up arrow key is pressed go up
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]: #if the down arrow key is pressed go down
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):       #index and cube object in self.body
            p = c.pos[:]
            if p in self.turns:                 #if the position is in current turn list
                turn = self.turns[p]            #complete the turn at the index p
                c.move(turn[0], turn[1])        #turn in the appropraite x and y
                if i == len(self.body) - 1:     #once the tail completes the turn remove that turn from the turn list
                    self.turns.pop(p)
            else:                                               #if the snakes position is not in the turn list
                if c.dirnx == -1 and c.pos[0] <= 0:             #if the snake is moving left and hits the wall
                    c.pos = (c.rows - 1, c.pos[1])              #move the snake to the right side of the screen
                elif c.dirnx == 1 and c.pos[0] >= c.rows - 1:   #if the snake is moving right and hits the wall
                    c.pos = (0, c.pos[1])                       #move the snake to the left side of the screen
                elif c.dirny == 1 and c.pos[1] >= c.rows - 1:   #if the snake is moving down and hits the bottom wall
                    c.pos = (c.pos[0], 0)                       #move the snake to the top of the screen
                elif c.dirny == -1 and c.pos[1] <= 0:           #if the snake is moving up and hits the top wall
                    c.pos = (c.pos[0], c.rows - 1)              #move the snake to the bottom of the screen
                else:                                           #if the snake is somewhere in the middle of the grid
                    c.move(c.dirnx, c.dirny)                    #move it to whatever direction it is currently

    def reset(self, pos):   # resets the snake to the default position
        global speed
        self.head = cube(pos)           # resets the snake head position
        self.body = []                  # resets the snake head body to empty
        self.body.append(self.head)
        self.turns = {}                 # resets the turn list
        self.dirnx = 0
        self.dirny = 1
        speed = 10

    def addCube(self):
        tail = self.body[-1]                                        #put extra body at the tail
        dx = tail.dirnx
        dy = tail.dirny

        if dx == 1 and dy == 0:                                     #if the snakes tail is moving to the right
            self.body.append(cube((tail.pos[0] - 1, tail.pos[1])))  #place the extra body of the snake to the left of the tail
        elif dx == -1 and dy == 0:                                  #if the snakes tail is moving to the left
            self.body.append(cube((tail.pos[0] + 1, tail.pos[1])))  #place the extra body of the snake to the right of the tail
        elif dx == 0 and dy == 1:                                   #if the snakes tail is moving down
            self.body.append(cube((tail.pos[0], tail.pos[1] - 1)))  #place the extra body of the snake above the tail
        elif dx == 0 and dy == -1:                                  #if the snakes tail is moving up
            self.body.append(cube((tail.pos[0], tail.pos[1] + 1)))  #place the extra body of the snake below the tail

        self.body[-1].dirnx = dx                                    #set the new tail in the correct direction
        self.body[-1].dirny = dy


    def removeCube(self):
        tail = self.body[-1]
        dx = tail.dirnx
        dy = tail.dirny
        self.body = self.body[:-1]





    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:                      #is this the head of the snake
                c.draw(surface, True)       #eyes == true so draw eyes
            else:
                c.draw(surface)             #draw body without eyes



def drawGrid(w, rows, surface): #constructs the grid
    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))


def redrawWindow(surface):          #resets grid
    global rows, width, s, snack, poison, meal, boost
    surface.fill((0, 0, 0))
    s.draw(surface)
    snack.draw(surface)
    poison.draw(surface)
    meal.draw(surface)
    boost.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()


def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)                                          #puts snack randomly in the grid without placing it in any space occupied by the snake
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def randomPosion(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)  # puts Poison randomly in the grid without placing it in any space occupied by the snake
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)


def randomMeal(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)  # puts Meal randomly in the grid without placing it in any space occupied by the snake
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)

def randomBoost(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)  # puts Meal randomly in the grid without placing it in any space occupied by the snake
        y = random.randrange(rows)
        if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
            continue
        else:
            break

    return (x, y)

def message_box(subject, content):      #creates message box
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def game_intro():
    root = Tk()




    Name_Entry = Entry(root)
    title = Label(root, text="SNAKE!!!", bg="white", fg="black")
    Rules_Button = Button(root, text="Rules", fg="blue", bg="black", command=rules)
    Start_Button = Button(root, text="Start", fg="red", bg="black", command=main)


    title.grid(row=0)
    Start_Button.grid(row=1)
    Rules_Button.grid(row=2)




    root.mainloop()


def rules():

    root = Tk()
    title = Label(root, text="Rules", fg="black")
    Objective = Label(root, text="Feed your snake to become HUGE the bigger your snake gets the higher your score", fg="black")
    Rule1 = Label(root, text="You cannot collide with your tail", fg="black")
    Rule2 = Label(root, text="Blue Food increases your snakes length and thus your score", fg="black")
    Rule3 = Label(root, text="Green Poison decreases your snakes length and thus your score", fg="black")
    Rule4 = Label(root, text="Pink Meals increase your snakes length by 2 and thus your score", fg="black")
    Rule5 = Label(root, text="White Boosts increase your snakes speed and thus make your snake harder to control", fg="black")
    Rule6 = Label(root, text="Use the Arrow Keys to Move")


    title.grid(row=0)
    Objective.grid(row=1)
    Rule1.grid(row=2)
    Rule2.grid(row=3)
    Rule3.grid(row=4)
    Rule4.grid(row=5)
    Rule5.grid(row=6)
    Rule6.grid(row=7)





def main():
    global width, rows, s, snack, poison, meal, boost, speed
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))       #snake is red
    speed = 10
    snack = cube(randomSnack(rows, s), color=(0, 0, 255))        #snack is blue
    poison = cube(randomPosion(rows, s), color=(0, 255, 0))      #poison is green
    meal = cube(randomMeal(rows, s), color=(255, 51, 255))       #meal is pink
    boost = cube(randomBoost(rows, s), color=(255, 255, 255))      #boost is white

    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(10)
        clock.tick(speed)          #snake runs at 10 cubes per second to start
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color=(0, 0, 255))

        if s.body[0].pos == poison.pos:
            s.removeCube()
            poison = cube(randomPosion(rows, s), color=(0, 255, 0))

        if not s.body:
            print('Score: ', len(s.body))  # score = length of the snake
            message_box('You Lost!  ', 'Tip: Avoid the Green poison, while eating the Blue food ')
            s.reset((10, 10))  # reset the snake in the middle of the board
            break

        if s.body[0].pos == boost.pos:

            speed += 5
            boost = cube(randomBoost(rows, s), color=(255, 255, 255))

        if s.body[0].pos == meal.pos:
            s.addCube()
            s.addCube()
            meal = cube(randomMeal(rows, s), color=(255, 51, 255))


        redrawWindow(win)

        for x in range(len(s.body)):                                        #colision check
            if s.body[x].pos in list(map(lambda z: z.pos, s.body[x + 1:])):
                print('Score: ', len(s.body))                               #score = length of the snake
                message_box('You Lost!', 'Play again...')
                s.reset((10, 10))                                           #reset the snake in the middle of the board
                break

        redrawWindow(win)

game_intro()
