import pygame
from queue import  PriorityQueue
import math
import random as r
# defining a pygame windows
width=900
R,C=20,20
c_width = width//(R)
percent = int(input('enter the percentage of obstrucles to be generated'))/100
win=pygame.display.set_mode((width,width))
pygame.display.set_caption('Pathfinder')# default pathfinder windows

#Colours of blocks
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot():
    def __init__(self,row,column,color):
        self.row=row
        self.column=column
        self.color=color
        self.x=column*c_width
        self.y=row*c_width

    def draw_rect(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, c_width, c_width))
    def neighbours(self,grid):
        N=[]
        if self.column+1<R:
            if grid[self.row][self.column+1].color!=BLUE:#RIGHT
                #print('RIGHT', self.row, self.column+1)
                N.append(grid[self.row][self.column+1])
        if self.column>0:
            if grid[self.row][self.column-1].color != BLUE:#LEFT
                #print('LEFT',self.row,self.column-1)
                N.append(grid[self.row][self.column-1])
        if self.row+1 < R:
            if grid[self.row+1][self.column].color != BLUE: #DOWN
                #print('DOWN', self.row+1, self.column)
                N.append(grid[self.row+1][self.column])
        if self.row> 0:
            if grid[self.row-1][self.column].color != BLUE:#UP
                #print('UP',self.row-1,self.column)
                N.append(grid[self.row-1][self.column])
        #print()
        return N
    
#funtion to generate a grid
def grid(rows,col): #
    grid=[]
    n=percent*(rows*col)
    block=set()
    while len(block)-1!=n and n!=0:
        rnd = r.randint(0, 400)
        if rnd not in block:
            block.add(rnd)
        
    for i in range(rows):
        temp=[]
        for j in range(col):
            if (i*R+j ) in block:    
                cell=Spot(i,j,BLUE)
            else:
                cell = Spot(i, j, BLACK)
            temp.append(cell)
        grid.append(temp)
    return grid

#function to draw grid lines
def draw_line(rows,column):
    for i in range(rows+1): #0-20
        pygame.draw.line(win, GREY, (0,i*c_width), (20*c_width,i*c_width),3)#horizontal
        for j in range(column+1): #0-20
            pygame.draw.line(win,GREY,(j*c_width,0),(j*c_width,20*c_width),3)#vertical

#function to draw the grid
def draw_grid(grid,row,col):
    for i in range(row):
        for j in range(col):
            cell=grid[i][j]
            cell.draw_rect(win)
    draw_line(row,col)
    pygame.display.update()

# get row column coordinates of mouse click
def get_clicked_pos(pos, row):
    x=pos[0]//c_width
    y=pos[1]//c_width
    return x,y

def main(windows):
    running = True     
    start = None #starting coordinate
    end=None #end coordinate
    table = grid(R, C)
    c_table=table[:]
    
    while running:
        for event in pygame.event.get(): # pygames.event is a que 
            draw_grid(table, R, C)

            # if we click cross in windows program closes
            if event.type == pygame.QUIT: 
                running = False

            #Left click is to implant a block. Order: Red(start)-->Green(end)
            if pygame.mouse.get_pressed()[0]: #(1,0,0)              
                pos = pygame.mouse.get_pos() #co-ordinates of mouse
                row, col = get_clicked_pos(pos, R) 
                cell=table[col][row]
                if cell.color != BLUE:
                    if start==None and cell is not end :
                        cell.color=RED
                        start = cell
                    elif end == None and cell is not start :
                        cell.color = GREEN
                        end = cell

            #Right click is to cancel a block
            elif pygame.mouse.get_pressed()[2] :
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, R)
                cell = table[col][row]
                if cell.color!=BLUE:
                    if cell==start :
                        cell.color = BLACK
                        start = None
                    elif cell==end:
                        cell.color = BLACK
                        end= None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    algorithm(table,start ,end)

                if event.key==pygame.K_c:
                    start=None
                    end=None
                    table=grid(R,C)

    pygame.quit()           

                    
def dist(n1,n2):
    x1,y1=n1.row,n1.column
    x2, y2 = n2.row, n2.column
    return abs(x2-x1)+abs(y2-y1)

def algorithm(grid,start,end):
    cnt=0 #If two cells have same h and f, cnt is used to decide priority ie whichever neighbour is found first
    came_from={} #To trace out the final path of shortest distance blocks using purple colour
    g_score = {spot: float("inf") for row in grid for spot in row} 
    g_score[start] = 0  # dist from start to given coordinate
    h_score = {spot: float("inf") for row in grid for spot in row}
    h_score[start] = dist(start, end)  # dist from given coordinate to end
    f=g_score[start]+h_score[start]
    open=PriorityQueue()#first in first out
    open_hash={start}# to access all neighbouring cell, doesn't have shortest path cells(cells in came_from)
    open.put((f,h_score[start],cnt,start))
    open_hash.add(start) 
    

    while not open.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open.get()[3]#shortest dist cell
      
        open_hash.remove(current)
        #Tracing out path after finding the path
        if current==end:
            while current in came_from:
                current=came_from[current]
                current.color=PURPLE
                draw_grid(grid, R, C)
            return True

        for neighbor in current.neighbours(grid):
            temp_g_score = g_score[current] + 1
            #print(neighbor.row, neighbor.column)

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                h_score[neighbor] =dist(neighbor, end)
                f = g_score[neighbor]+h_score[neighbor]
                #print(f)
                #print(h_score[neighbor])
                #print()
                if neighbor not in open_hash:
                    cnt += 1
                    open.put((f, h_score[neighbor], cnt, neighbor))
                    open_hash.add(neighbor)
                    neighbor.color=YELLOW

        
        draw_grid(grid,R,C)
main(win)

#Code for to print error message when maze cna't be solved.(Not fully completed)
'''         
        if current != end:
         if not current.neighbours(grid):
            print('1Maze Unsolvable')
            return True
         else:
            for i in current.neighbours(grid):
                if g_score[i]+h_score[i]<=g_score[current]+h_score[current]+1 and (i in open_hash or i in came_from)
                    continue
                else:
                       break
            else:
                print(g_score[i],h_score[i])
                print(g_score[current],h_score[current])
                print('2Maze Unsolvable')
                return True
        '''

