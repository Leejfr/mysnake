from tkinter import *
from time import sleep

class MySnake():
    
    def __init__(self, main_canvas:Canvas) -> None:
        self.length = 6
        self.head_position = (100, 500)
        self.direction = "right"
        self.list_nodes = list()
        self.list_nodes_positions = list()
    
    
    def move(self, main_canvas:Canvas):
        r = l = d = u = 0
        if self.direction == "right":
            r = 20
        elif self.direction == "left":
            l = -20
        elif self.direction == "down":
            d = 20
        elif self.direction == "up":
            u = -20
        
        new_x = self.head_position[0]+r+l
        if new_x > main_canvas.winfo_reqwidth():
            new_x = 0
        if new_x < 0:
            new_x = main_canvas.winfo_reqwidth()//10*10
        new_y = self.head_position[1]+d+u
        if new_y > main_canvas.winfo_reqheight():
            new_y = 0
        if new_y < 0:
            new_y = main_canvas.winfo_reqheight()//10*10
        
        self.head_position = (new_x, new_y)    
        node = main_canvas.create_oval(self.head_position[0], self.head_position[1], self.head_position[0]+20, self.head_position[1]+20, fill="blue")
        self.list_nodes.append(node)
        self.list_nodes_positions.append(self.head_position)

        if len(self.list_nodes) >= self.length:
            main_canvas.delete(self.list_nodes[0])
            self.list_nodes.pop(0)
            self.list_nodes_positions.pop(0)
            
    def upgrade(self):
        self.length = self.length + 3
        
    def check_collision(self):
        if self.list_nodes_positions.count(self.head_position) > 1 and len(self.list_nodes_positions) > 6:
            return True
        return False
