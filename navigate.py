from tkinter import Tk, Label, Button, StringVar, Canvas
from time import sleep
import random

class Snake:
    SIZE = 300, 300
    TITLE = 'Snake'
    BODY_LEN = 3
    
    def __init__(self, master):
        
        self.master = master
        self.master.bind('<Up>', lambda x: self.navigate('up'))
        self.master.bind('<Left>', lambda x: self.navigate('left'))
        self.master.bind('<Right>', lambda x: self.navigate('right'))
        self.master.bind('<Down>', lambda x: self.navigate('down'))
        self.directions = {'down': [0,5,0,5], 'up': [0,-5,0,-5], 'right': [5,0,5,0], 'left': [-5,0,-5,0]}
        self.direction = self.directions.get('right')
        self.status_label_text = StringVar()
        self.w = Canvas(master, width=self.SIZE[0], height=self.SIZE[1] - 100)
        self.w.pack()
        self.snake_body = [self.w.create_rectangle([50, 20, 55, 25], fill="#476042")]
        for i in range(self.BODY_LEN - 1):
            self.snake_body.append(self.w.create_rectangle([self.w.coords(self.snake_body[-1])[i]+self.directions.get('left')[i] for i in range(len(self.w.coords(self.snake_body[-1])))]))
        self.w.after(100, self.onTimer)
        x, y = self.generate_apple_coords()
        self.apple = self.w.create_rectangle(x, y, x+5, y+5, fill="#476042")
            
    def generate_apple_coords(self):
        return random.randint(0, (self.SIZE[0] - 5)/5) * 5, random.randint(0, (self.SIZE[1] - 105)/5) * 5

    def check_border_collision(self, checklist):
        if checklist[0] < 0 or checklist[1] < 0 or checklist[2] > self.SIZE[0] or checklist[3] > self.SIZE[1] - 100:
            return 1
        
    def navigate(self, direction):
        move_opposites = {'left': 'right', 'right': 'left', 'up': 'down', 'down': 'up'}
        if self.direction[0] == self.directions.get(move_opposites.get(direction))[0] or \
        self.direction[1] == self.directions.get(move_opposites.get(direction))[1]:
            return None
        else:
            self.direction = self.directions.get(direction)
    
    def check_body_collision(self):
        head = self.w.coords(self.snake_body[0])
        for i in range(1, len(self.snake_body)):
            if head == self.w.coords(self.snake_body[i]):
                return 1
        return 0
    
    def check_eat_apple(self):
        if self.w.coords(self.snake_body[0]) == self.w.coords(self.apple):
            return True
    
    def eat_apple(self):
        self.snake_body.append(self.w.create_rectangle(self.w.coords(self.snake_body[len(self.snake_body)-1])))
        x, y = self.generate_apple_coords()
        self.w.coords(self.apple, [x, y, x+5, y+5])
            
    def onTimer(self):
        if self.check_body_collision() or self.check_border_collision(self.w.coords(self.snake_body[0])):      
            self.status_label_text.set('You lost the game')
            self.status_label = Label(self.master, textvariable=self.status_label_text)
            self.status_label.pack()
        else:
            # assign head to tmp
            tmp = self.w.coords(self.snake_body[0])
            for i in range(1, len(self.snake_body)):
                tmp1 = self.w.coords(self.snake_body[i])
                # assign coords of prev elem to the next
                self.w.coords(self.snake_body[i], tmp)
                tmp = tmp1
                
                
            # head = self.w.coords(self.snake_body[0])
            the_coords = self.w.coords(self.snake_body[0])
            for j in range(len(the_coords)):
                the_coords[j] += self.direction[j]
            self.w.coords(self.snake_body[0], the_coords)
            if self.check_eat_apple():
                self.eat_apple()
            self.w.after(100, self.onTimer)
        
        
root = Tk()
snake = Snake(root)
root.configure(background='black', )
root.geometry("{width}x{height}".format(width=snake.SIZE[0],height=snake.SIZE[1] - 80))
root.mainloop()
