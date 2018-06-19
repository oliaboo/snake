from tkinter import Tk, Label, Button, StringVar, Canvas
from time import sleep

class Snake:
    SIZE = 600, 600
    TITLE = 'Snake'
    
    def __init__(self, master):
        
        self.master = master
        self.master.bind('<Up>', lambda x: self.navigate('up'))
        self.master.bind('<Left>', lambda x: self.navigate('left'))
        self.master.bind('<Right>', lambda x: self.navigate('right'))
        self.master.bind('<Down>', lambda x: self.navigate('down'))
        self.directions = {'down': [0,5,0,5], 'up': [0,-5,0,-5], 'right': [5,0,5,0], 'left': [-5,0,-5,0]}
        self.direction = self.directions.get('right')

        self.w = Canvas(master, width=self.SIZE[0], height=self.SIZE[1] - 100)
        self.w.pack()
        self.snake_tail = [self.w.create_rectangle(50, 20, 55, 25, fill="#476042"), self.w.create_rectangle(40, 20, 45, 25, fill="#476042"), self.w.create_rectangle(45, 20, 50, 25, fill="#476042")]
        self.w.after(100, self.onTimer)

        
    def check_head(self, checklist):
        if checklist[0] < 0 or checklist[1] < 0 or checklist[2] > self.SIZE[0] or checklist[3] > self.SIZE[1] - 100:
            return 1
    
    
    def navigate(self, direction):
        self.direction = self.directions.get(direction)
        return None

        
    def onTimer(self):
        # head = self.w.coords(self.small)
        if self.check_head(self.w.coords(self.snake_tail[0])):
            self.status_label_text = StringVar()
            self.status_label_text.set('You lost the game')
            self.status_label = Label(self.master, textvariable=self.status_label_text)
            self.status_label.pack()
        else:
            tmp = self.w.coords(self.snake_tail[0])
            for i in range(1, len(self.snake_tail)):
                tmp1 = self.w.coords(self.snake_tail[i])
                self.w.coords(self.snake_tail[i], tmp)
                tmp = tmp1
                
                
            # head = self.w.coords(self.snake_tail[0])
            the_coords = self.w.coords(self.snake_tail[0])
            for j in range(len(the_coords)):
                the_coords[j] += self.direction[j]
            self.w.coords(self.snake_tail[0], the_coords)
            
                #else:
                #    the_coords = self.w.coords(self.snake_tail[i-1])
                
                
            self.w.after(100, self.onTimer)
        
        
root = Tk()
snake = Snake(root)
root.configure(background='black', )
root.geometry("{width}x{height}".format(width=snake.SIZE[0],height=snake.SIZE[1] - 80))
root.mainloop()
