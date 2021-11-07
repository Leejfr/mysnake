from tkinter import *
import tkinter
from modules.Snake import MySnake
from modules.Apple import Apple

from time import sleep

def move():
    my_snake.move(snake_canvas)
    if my_snake.head_position == apple.current_position:
        my_snake.upgrade()
        apple.show(snake_canvas, my_snake.list_nodes_positions)
        
    if my_snake.check_collision():
        snake_canvas.create_text(400,263, text='PERDU !', font=('Ariel', 60, 'bold'))
    else:
        main_window.after(100, move)
    
def right(event):
    if my_snake.direction != "left":
        my_snake.direction = "right"
    
def left(event):
    if my_snake.direction != "right":
        my_snake.direction = "left"

def up(event):
    if my_snake.direction != "down":
        my_snake.direction = "up"
    
def down(event):
    if my_snake.direction != "up":
        my_snake.direction = "down"
    
if __name__ == '__main__':
    main_window = Tk()
    main_window.title("My Snake")
    main_window.geometry("800x650")
    
    snake_canvas = Canvas(main_window, width=800, height=600, background="grey")
    snake_canvas.pack()
    
    my_snake = MySnake(snake_canvas)
    apple = Apple()
    apple.show(snake_canvas)
    
    snake_canvas.pack()
    
    main_window.bind('<Right>', right)
    main_window.bind('<Left>', left)
    main_window.bind('<Up>' , up)
    main_window.bind('<Down>', down)
    
    #b1 = Button(fen, text='Rejouer', command=newGame, bg='black' , fg='green')
    
    move()
    
    main_window.mainloop()
    
    