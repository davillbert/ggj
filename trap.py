from tkinter import *
import graphics as gr

root = Tk()
root.geometry('200x100')
root.title('LASER')
     
T = True


def new_window(event):
    window = gr.GraphWin("Fluid", 400, 400)
        
    def clear_window():
        las = gr.Rectangle(gr.Point(0, 0), gr.Point(400, 400))
        las.setFill('blue')
        las.draw(window)
     #   rectangle1 = gr.Rectangle(gr.Point(0, 0), gr.Point(400, 50))
    #    rectangle1.setFill('blue')
     #   rectangle1.draw(window)
     #   rectangle2 = gr.Rectangle(gr.Point(0, 100), gr.Point(400, 400))
      #  rectangle2.setFill('blue')
     #   rectangle2.draw(window)

        
    def draw_ball(coords, color):
        circle = gr.Circle(coords, 10)
        circle.setFill(color)
        circle.draw(window)
            
    SIZE_X = 400
    SIZE_Y = 400

    coords = gr.Point(200, 200)
    velocity = gr.Point(1, -2)
    acceleration = gr.Point(0, -0.01)

    coords2 = gr.Point(300, 300)
    velocity2 = gr.Point(-1, 2)
    acceleration2 = gr.Point(-0.01, 0)

    def add(point_1, point_2):
        new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

        return new_point

    def check_coords(coords, velocity):
        if coords.x < 0 or coords.x > SIZE_X:
                velocity.x = -velocity.x

        if coords.y < 0 or coords.y > SIZE_Y:
                velocity.y = -velocity.y    
            
    def check_velocity(velocity, acceleration):
        return add(velocity, acceleration)
        
    def check_acceleration(coords1, coords_):
        pass
        
    while True:
        clear_window()
        draw_ball(coords, 'red')
        coords = add(coords, velocity)
        velocity = check_velocity(velocity, acceleration)

        draw_ball(coords2, 'black')
        coords2 = add(coords2, velocity2)
        velocity2 = check_velocity(velocity2, acceleration2)
    
        check_coords(coords, velocity)
        check_coords(coords2, velocity2)
    
        gr.time.sleep(0.02)
                
            
def new_window_las(event):
        window = gr.GraphWin("Fluid with LASER", 400, 400)
        
        def clear_window():
            las = gr.Rectangle(gr.Point(0, 50), gr.Point(400, 100))
            las.setFill('yellow')
            las.draw(window)
            rectangle1 = gr.Rectangle(gr.Point(50, 0), gr.Point(100, 50))
            rectangle1.setFill('yellow')
            rectangle1.draw(window)
            rectangle8 = gr.Rectangle(gr.Point(50, 100), gr.Point(100, 400))
            rectangle8.setFill('yellow')
            rectangle8.draw(window)
            rectangle2 = gr.Rectangle(gr.Point(0, 0), gr.Point(50, 50))
            rectangle2.setFill('blue')
            rectangle2.draw(window)
            r1 = gr.Rectangle(gr.Point(100, 0), gr.Point(400, 50))
            r1.setFill('blue')
            r1.draw(window)
            r2 = gr.Rectangle(gr.Point(0, 100), gr.Point(50, 400))
            r2.setFill('blue')
            r2.draw(window)
            r3 = gr.Rectangle(gr.Point(100, 100), gr.Point(400, 400))
            r3.setFill('blue')
            r3.draw(window)

        
        def draw_ball(coords, color):
            circle = gr.Circle(coords, 10)
            circle.setFill(color)
            circle.draw(window)
            
        SIZE_X = 400
        SIZE_Y = 400

        coords = gr.Point(200, 200)
        velocity = gr.Point(1, -2)
        acceleration = gr.Point(0, -0.01)

        coords2 = gr.Point(300, 300)
        velocity2 = gr.Point(-1, 2)
        acceleration2 = gr.Point(-0.01, 0)

        def add(point_1, point_2):
            new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

            return new_point

        def check_coords(coords, velocity):
            if coords.x < 0 or coords.x > SIZE_X:
                velocity.x = -velocity.x

            if coords.y < 0 or coords.y > SIZE_Y:
                velocity.y = -velocity.y    
            
        def las_acceler(coords, velocity, t):
            if coords.x > 50 and coords.x < 100 and coords.y > 0 and coords.y < 50:
                coords.x = 75
                velocity.y = t
                coords.y = 75
            if coords.x > 50 and coords.x < 100 and coords.y > 50 and coords.y < 100:
                coords.x = 75
                velocity.y = t
                coords.y = 75
            if coords.x > 50 and coords.x < 100 and coords.y > 100 and coords.y < 400:
                coords.x = 75
                velocity.y = t
                coords.y = 75 
            if coords.y > 50 and coords.y < 100 and coords.x > 0 and coords.x < 50:
                coords.y = 75
                velocity.x = t
                coords.x = 75
            if coords.y > 50 and coords.y < 100 and coords.x > 50 and coords.x < 100:
                coords.y = 75
                velocity.x = t
                coords.x = 75 
            if coords.y > 50 and coords.y < 100 and coords.x > 100 and coords.x < 400:
                coords.y = 75
                velocity.x = t
                coords.x = 75
            
            
            
        def check_velocity(velocity, acceleration):
            return add(velocity, acceleration)
        
        def check_acceleration(coords1, coords_):
            pass
        
        while True:
            clear_window()
            draw_ball(coords, 'red')
            coords = add(coords, velocity)
            velocity = check_velocity(velocity, acceleration)

            las_acceler(coords, velocity, 10)
            
            
            
            draw_ball(coords2, 'black')
            coords2 = add(coords2, velocity2)
            velocity2 = check_velocity(velocity2, acceleration2)
    
            check_coords(coords, velocity)
            check_coords(coords2, velocity2)
            las_acceler(coords2, velocity2, 20)
            gr.time.sleep(0.02)



but = Button(root, text='Кювета')
but.bind('<Button->', new_window)
 
but_las = Button(root, text='Кювета с ловушкой')
but_las.bind('<Button->', new_window_las)

but_las.pack()
but.pack()
#entry.pack()
 
root.mainloop()
