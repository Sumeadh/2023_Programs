import pygame
import pickle
class Spot():
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.x = column*c_width
        self.y = row*c_width
        self.in_set=False

# funtion to generate a grid
    def draw_rect(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, c_width, c_width))

    def plus_neighbours(self, grid,command=False):
        N = []
        if self.row > 0:
            if grid[self.row-1][self.column].color != BLUE or command:  # UP
                N.append(grid[self.row-1][self.column])
        if self.column+1 < R:
            if grid[self.row][self.column+1].color != BLUE or command:  # RIGHT
                N.append(grid[self.row][self.column+1])
        if self.row+1 < R:
            if grid[self.row+1][self.column].color != BLUE or command:  # DOWN
                N.append(grid[self.row+1][self.column])
        if self.column > 0:
            if grid[self.row][self.column-1].color != BLUE or command:  # LEFT
                N.append(grid[self.row][self.column-1])
        return N
    
    def cross_neighbours(self, grid,command=False):
        N1 = self.plus_neighbours(grid, command)
        if self.column+1 < R:
            if self.row > 0:
                if grid[self.row-1][self.column+1].color != BLUE or command:  # TOP-RIGHT
                    N1.append(grid[self.row-1][self.column+1])
            if self.row+1 < R:
                if grid[self.row+1][self.column+1].color != BLUE or command:  # BOTTOM-RIGHT
                    N1.append(grid[self.row+1][self.column+1])
        if self.column > 0:
            if self.row+1 < R:
                if grid[self.row+1][self.column-1].color != BLUE or command:  # BOTTOM-LEFT
                    N1.append(grid[self.row+1][self.column-1])
            if self.row > 0:
                if grid[self.row-1][self.column-1].color != BLUE or command:  # TOP-LEFT
                    N1.append(grid[self.row-1][self.column-1])
        return N1
    
    def block_neighbours(self,grid):
        N=[]
        #Plus Neighbours in clockwise direction
        if self.column+1 < R:
            if grid[self.row][self.column+1].color == BLUE:  # RIGHT
                N.append(grid[self.row][self.column+1])
        if self.column > 0:
            if grid[self.row][self.column-1].color == BLUE:  # LEFT
                N.append(grid[self.row][self.column-1])
        if self.row+1 < R:
            if grid[self.row+1][self.column].color == BLUE:  # DOWN
                N.append(grid[self.row+1][self.column])
        if self.row > 0:
            if grid[self.row-1][self.column].color == BLUE:  # UP
                N.append(grid[self.row-1][self.column])
        
        #Cross Neighbours
        if self.column+1 < R:
            if self.row > 0:
                if grid[self.row-1][self.column+1].color == BLUE:  # TOP-RIGHT
                    N.append(grid[self.row-1][self.column+1])
            if self.row+1 < R:
                if grid[self.row+1][self.column+1].color == BLUE:  # BOTTOM-RIGHT
                    N.append(grid[self.row+1][self.column+1])
        if self.column > 0:
            if self.row > 0:
                if grid[self.row-1][self.column-1].color == BLUE:  # TOP-LEFT
                    N.append(grid[self.row-1][self.column-1])
            if self.row+1 < R:
                if grid[self.row+1][self.column-1].color == BLUE:  # BOTTOM-LEFT
                    N.append(grid[self.row+1][self.column-1])
        return N
# Store nodes in a nested list
def grid(rows, col):
    grid=[]
    for i in range(rows):
        temp = []
        for j in range(col):
            cell = Spot(i, j, BLACK)
            temp.append(cell)
        grid.append(temp)
    return grid

# function to draw the grid
def draw_line(rows, column):
    for i in range(rows+1):  # 0-20
        pygame.draw.line(win, GREY, (0, i*c_width),
                         (20*c_width, i*c_width), 3)  # horizontal
        for j in range(column+1):  # 0-20
            pygame.draw.line(win, GREY, (j*c_width, 0),
                             (j*c_width, 20*c_width), 3)  # vertical

# Draw the grid using pygames
def draw_grid(grid, row, col):
    for i in range(row):
        for j in range(col):
            cell = grid[i][j]
            cell.draw_rect(win)
    draw_line(row, col)
    pygame.display.update()

# To locate the row and column of the node if clicked upon
def get_clicked_pos(pos, row):
    x=pos[0]//c_width
    y=pos[1]//c_width
    return x,y

# To find the shortest path between the given two nodes
def line_algorithm(grid,start,end): 
    h_score= dist(start, end)
    path=[]
    current=start
    while current!=end:
        for neighbours in current.cross_neighbours(grid,True):
            h_score_temp = dist(neighbours, end)
            if h_score_temp<h_score:
                open=neighbours
                h_score=h_score_temp
        current=open
        path.append(current)
    path.append(current)
    return path

# Main algorithm executing bug1 algorithm
def main_algorithm(grid,start,end):
    main_path=[start]
    code = 1
    while main_path[-1]!=end:
        line_path=line_algorithm(grid,main_path[-1],end)
        for cnt in range (0,len(line_path)-1):
            if line_path[cnt+1].color==BLUE:
                find_set(grid,line_path[cnt+1],code)
                start = line_path[cnt]
                path ,high= go_round(grid,start, end,start, [1, start],start,code)
                path.pop(0)
                indx = path.index(high)
                path += path[0:indx+1]
                main_path.extend(path)
                code+=1
                break
            else:
                main_path.append(line_path[cnt]) 

    # Draw the points
    for i in range(1,len(main_path)):
        main_path[i-1].color=BLACK
        main_path[i].color=RED
        draw_grid(grid,R, C)
        pygame.time.delay(500)

# To Consider all block points as one entitiy
def find_set(grid,point,code,Set=set()):
    for i in point.block_neighbours(grid):
        if i not in Set:
            Set.add(i)
            i.in_set = code
            find_set(grid,i,code,Set)
    return True

# algorithm to go around the block if encountered
def go_round(grid,start,end,current,path,high,code):
    while True : 
        if current == start and len(path)>2:
            return path, high
        else:
            for i in current.plus_neighbours(grid):
                for j in i.block_neighbours(grid):
                    if j.in_set==code and i !=path[-2]:
                        path.append(i)
                        current = i
                        current.color=WHITE
                        draw_grid(grid,R,C)
                        if dist(i, end) < dist(high, end):
                            high = i
                        path,high=go_round(grid,start,end,current,path,high,code)

                        return path, high

# This is where the program starts.The heart of the program
def main(windows):
    running = True
    start = None  # starting coordinate
    end = None  # end coordinate
    global table
    with open('maze.bin', 'rb') as file:
        table=pickle.load(file)
    while running:
        for event in pygame.event.get():  # pygames.event is a que
            draw_grid(table, R, C)

            # if we click cross in windows program closes
            if event.type == pygame.QUIT:
                running = False

            # Left click is to implant a block. Order: Red(start)-->Green(end)
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()  # co-ordinates of mouse
                row, col = get_clicked_pos(pos, R)
                cell = table[col][row]
                if cell.color != BLUE:
                    if start == None and cell is not end:
                        cell.color = RED
                        start = cell
                    elif end == None and cell is not start:
                        cell.color = GREEN
                        end = cell
                    elif cell not in (start,end):
                        cell.color=BLUE

            # Right click is to cancel a block
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, R)
                cell = table[col][row]
                if cell == start:
                    cell.color = BLACK
                    start = None
                elif cell == end:
                    cell.color = BLACK
                    end = None
                elif cell.color==BLUE:
                    cell.color=BLACK

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:

                    main_algorithm(table, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    table = grid(R, C)

    pygame.quit()

def dist(n1, n2):
    x1, y1 = n1.row, n1.column
    x2, y2 = n2.row, n2.column
    return abs(x2-x1)+abs(y2-y1)


width = 900
R, C = 20, 20
c_width = width//(R)
win = pygame.display.set_mode((width, width))
pygame.display.set_caption('Pathfinder')  # default pathfinder windows

# Colours of blocks
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

table = grid(R, C)
main(win)

