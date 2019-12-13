from Tkinter import *
from tkinter.ttk import *
window = Tk()
canvas = Canvas(window, width=800, height=500, background="white")
canvas.pack()

#Ball 1
x0 = 225
y0 = 225
x1 = 275
y1 = 275

#Timer
timer = 0


#Ball 1
speed_x = 5
speed_y = 15

#Array [x0, x1, y0, y1]
breakout = [[25, 150, 25, 75], [175, 300, 25, 75], [325, 450, 25, 75], [475, 600, 25, 75], [625, 750, 25, 75], [25, 150, 100, 150], [175, 300, 100, 150], [325, 450, 100, 150], [475, 600, 100, 150], [625, 750, 100, 150]]


#Platform
boxx0 = 0
boxx1 = 0
boxy0 = 0
boxy1 = 0
ball = canvas.create_oval(x0,y0,x1,y1,fill="black")
box = canvas.create_rectangle(450,475,450,475,fill="black")
breakoutbox1 = canvas.create_rectangle(breakout[0][0],breakout[0][2],breakout[0][1],breakout[0][3],fill="black")
breakoutbox2 = canvas.create_rectangle(breakout[1][0],breakout[1][2],breakout[1][1],breakout[1][3],fill="black")
breakoutbox3 = canvas.create_rectangle(breakout[2][0],breakout[2][2],breakout[2][1],breakout[2][3],fill="black")
breakoutbox4 = canvas.create_rectangle(breakout[3][0],breakout[3][2],breakout[3][1],breakout[3][3],fill="black")
breakoutbox5 = canvas.create_rectangle(breakout[4][0],breakout[4][2],breakout[4][1],breakout[4][3],fill="black")
breakoutbox6 = canvas.create_rectangle(breakout[5][0],breakout[5][2],breakout[5][1],breakout[5][3],fill="black")
breakoutbox7 = canvas.create_rectangle(breakout[6][0],breakout[6][2],breakout[6][1],breakout[6][3],fill="black")
breakoutbox8 = canvas.create_rectangle(breakout[7][0],breakout[7][2],breakout[7][1],breakout[7][3],fill="black")
breakoutbox9 = canvas.create_rectangle(breakout[8][0],breakout[8][2],breakout[8][1],breakout[8][3],fill="black")
breakoutbox10 = canvas.create_rectangle(breakout[9][0],breakout[9][2],breakout[9][1],breakout[9][3],fill="black")
boxes = [breakoutbox1, breakoutbox2, breakoutbox3, breakoutbox4, breakoutbox5, breakoutbox6, breakoutbox7, breakoutbox8, breakoutbox9, breakoutbox10]
broke = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    canvas.move(ball, speed_x, speed_y)
    
    canvas.after(30)
    canvas.update()



    #Ball 1
    if x1 >= window.winfo_width():     
        speed_x = -5
    if x0 <= 0:         
        speed_x = 5
    if y1 >= window.winfo_height():        
        canvas.delete(ball)
    if y0 <= 0:         
        speed_y = 15
        
    #Collision
    
    if x0 in range(breakout[0][0], breakout[0][1]) and y0 in range(breakout[0][2], breakout[0][3]) and broke[0] == 0:
        canvas.delete(boxes[0])
        speed_y = 15
        broke[0] = 1
    if x0 in range(breakout[1][0], breakout[1][1]) and y0 in range(breakout[1][2], breakout[1][3]) and broke[1] == 0:
        canvas.delete(boxes[1])
        speed_y = 15
        broke[1] = 1
    if x0 in range(breakout[2][0], breakout[2][1]) and y0 in range(breakout[2][2], breakout[2][3]) and broke[2] == 0:
        canvas.delete(boxes[2])
        speed_y = 15
        broke[2] = 1
    if x0 in range(breakout[3][0], breakout[3][1]) and y0 in range(breakout[3][2], breakout[3][3]) and broke[3] == 0:
        canvas.delete(boxes[3])
        speed_y = 15
        broke[3] = 1
    if x0 in range(breakout[4][0], breakout[4][1]) and y0 in range(breakout[4][2], breakout[4][3]) and broke[4] == 0:
        canvas.delete(boxes[4])
        speed_y = 15
        broke[4] = 1
    if x0 in range(breakout[5][0], breakout[5][1]) and y0 in range(breakout[5][2], breakout[5][3]) and broke[5] == 0:
        canvas.delete(boxes[5])
        speed_y = 15
        broke[5] = 1
    if x0 in range(breakout[6][0], breakout[6][1]) and y0 in range(breakout[6][2], breakout[6][3]) and broke[6] == 0:
        canvas.delete(boxes[6])
        speed_y = 15
        broke[6] = 1
    if x0 in range(breakout[7][0], breakout[7][1]) and y0 in range(breakout[7][2], breakout[7][3]) and broke[7] == 0:
        canvas.delete(boxes[7])
        speed_y = 15
        broke[7] = 1
    if x0 in range(breakout[8][0], breakout[8][1]) and y0 in range(breakout[8][2], breakout[8][3]) and broke[8] == 0:
        canvas.delete(boxes[8])
        speed_y = 15
        broke[8] = 1
    if x0 in range(breakout[9][0], breakout[9][1]) and y0 in range(breakout[9][2], breakout[9][3]) and broke[9] == 0:
        canvas.delete(boxes[9])
        speed_y = 15
        broke[9] = 1
   
    print[boxes[0]]

    #for x in range(len(breakout)):
    #    if y0 <= breakout[x][3]:
    #        speedy = 7
    #        breakout[x][0] = 0
    #        breakout[x][1] = 0
    #        canvas.delete(boxes[0])
            


    

    
    


    if boxx0 <= x1 and boxx1 >= x0 and boxy0 <= y1 and boxy1 >= y0:
        speed_y = -15
        timer = 50
        print("hit")
        
    if timer <= 50 and timer >= 0:
        timer-=1
    
    
    def mouseMove(event):
	#print canvas.canvasx(event.x), canvas.canvasy(event.y)
	canvas.coords(box, event.x-100, 450, event.x, 475)
	#canvas.move(box, event.x/25, 0)
	#box.place(x=20, y=0)
	#Ball with Platform
	#g(event.x, event.x - 100, event.y)
	global boxx0
        global boxx1
        global boxy0
        global boxy1
	
	boxx1 = event.x
	boxx0 = event.x - 100
	boxy0 = 450
	boxy1 = 475
	
	
    
	

    a = canvas.bbox(ball)
    canvas.bind('<Motion>',mouseMove)
    
    #Ball 1
    x0 += speed_x
    x1 += speed_x
    y0 += speed_y
    y1 += speed_y

mainloop()

#def g(x, y, z):
#    boxx1 = x
#    boxx0 = y
#    boxy0 = z


    
