import pygame
import pygame.freetype
from math import *
import matplotlib.pyplot as plt
pygame.init()
screen = pygame.display.set_mode((500, 500))
#If The Program is Completed
done = False

# Parameters
start = False
### Goal Positions - All the intermediate points ###
a = []  # x  and y coordinates ###
screen.fill((0, 0, 0))

def controller(i,f):
    ######################################
    #          Controller Code           #
    ######################################
    Kp_x=0.01
    Kp_y=0.01
    #  error between the current position and the destination position
    error_x = f[0] - i[0]
    error_y = f[1] - i[1]
    dist=(error_x**2+error_y**2)**(0.5)
    #  control signal 
    control_signal_x = Kp_x * error_x
    control_signal_y = Kp_y * error_y

    return control_signal_x, control_signal_y,dist

def solve(lst,condn):
    #Initial System Variable
    xPos,yPos = lst[0]
    track=0
    #Varibles for plotting
    cnt=0
    time=[]
    position=[]

    if condn:
        for i in range (len(lst)-1):        
            while abs(xPos-lst[i+1][0]) > 0.5 or abs( yPos-lst[i+1][1]) > 0.5: # Sometimes position of object and actual coordinates won't exactly match
                Vel_x, Vel_y, distance = controller((xPos, yPos), lst[i+1])
                position.append(distance) #For each distance from destination pnt we append object's distance inside position
                # Updation
                xPos +=Vel_x
                yPos += Vel_y
                time.append(cnt)
                cnt += 1
                # Drawing
                pygame.time.delay(10)
                draw(track,lst[i][0],lst[i][1],xPos,yPos)
            track+=1# Adds if object reached the intermediate point

        #Displaying Completed after object reached the point    
        my_font = pygame.font.SysFont('Comic Sans MS', 25)
        text_surface = my_font.render('Completed', True, (255, 255, 255))
        screen.blit(text_surface, (a[-1][0]-0.5, a[-1][1]-50))
        pygame.display.flip()

        # Plotting
        plt.plot(time, position)
        plt.xlabel('Time')
        plt.ylabel('Position')
        plt.title('Position vs Time')
        plt.grid(True)
        plt.show()  
        return True
    
    else:# if intial point==destination point
        Vel_x=0
        Vel_y=0
        return 'Completed'

#TO DRAW GRID EACH AND EVERY TIME
def draw(cnt,start_xpos,start_ypos,end_xpos,end_ypos):
    screen.fill((0,0,0))
    for i in range(len(a)):# Drawing start,end,intermediate points
        if i==0:# Start
            pygame.draw.circle(screen, (255, 0,0), a[i], 5)
        if i==len(a)-1:# End
            pygame.draw.circle(screen, (0, 255, 0), a[i], 5)
        else: #Intermerdiate
            pygame.draw.circle(screen, (0, 0, 255), a[i], 5)
    for i in range(cnt):  # 0,1
        pygame.draw.line(screen, (0, 0, 255), a[i], a[i+1], 5)        
    pygame.draw.line(screen, (0, 0, 255), (start_xpos,start_ypos),(end_xpos,end_ypos), 5) #Drawing line from prev intermediate to current point
    pygame.draw.circle(screen, (255, 0, 0),(end_xpos, end_ypos), 5)
    pygame.display.flip()

#MAIN PROGRAM
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if len(a) == 1:
            pygame.draw.circle(screen, (255, 0, 0), a[0], 5)
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render('Start', True, (255, 255, 255))
            screen.blit(text_surface, (a[0][0]+0.5, a[0][1]+0.5))
            pygame.display.flip()
        if len(a) == 2:
            pygame.draw.circle(screen, (0, 255, 0), a[-1], 5)
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render('End', True, (255, 255, 255))
            screen.blit(text_surface, (a[-1][0]-0.5, a[-1][1]-50))
            pygame.display.flip()
            start = True
        if len(a)>2:
            if a[0]!=a[-1]:
                pygame.draw.circle(screen, (0, 0, 255), a[-1], 5)
                pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:  # Gets triggered for any kind of mouse action
            pos = pygame.mouse.get_pos()
            x, y = pos[0], pos[1]
            a.append((x, y))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                a.append(a.pop(1))# Shifting end point from 1st to end index
                solve(a, start)
                done=True
                break
       

