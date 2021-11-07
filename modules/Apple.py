from tkinter import *
from numpy import random
import numpy

class Apple():
    def __init__(self):
        self.current_position = None
    
    def get_new_position(self, main_canvas:Canvas, forbidden_list:list=list()):
        if self.current_position :
            main_canvas.delete(self.apple_shape)
            new_x = random.randint(50, main_canvas.winfo_reqwidth()-50)//10
            if new_x%2 != 0: new_x -= 1
            new_y = random.randint(50, main_canvas.winfo_reqheight()-50)//10
            if new_y%2 != 0: new_y -= 1
            if (new_x*10, new_y*10) not in forbidden_list:
                self.current_position = (new_x*10, new_y*10)
            else:
                self.get_new_position(main_canvas, forbidden_list)
        else:
            self.current_position = (400, 500)
        
    def show(self, main_canvas:Canvas, forbidden_list:list=list()):
        self.get_new_position(main_canvas, forbidden_list)
        self.apple_shape = main_canvas.create_oval(self.current_position[0], self.current_position[1], self.current_position[0]+20, self.current_position[1]+20, fill="green", outline="green")