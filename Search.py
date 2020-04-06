from collections import deque
import numpy as np
from heapq import *
from itertools import permutations
import sys
from queue import PriorityQueue


# c=dong la y , r=cot la x
class BFSItem:
    def __init__(self,matrix,start,end):
        self.m=matrix
        self.R=len(matrix)                             #so dong
        self.C=len(matrix[0])                            #so cot
        self.sr,self.sc=start                        #toa bo diem bat dau
        self.er,self.ec=end
        self.rq=deque()                 #QUEUE dong
        self.cq=deque()                 #QUEUE COT
        self.move_count=0               #Cac bien dung de xac dinh duong di
        self.nodes_left_in_layer=1      
        self.nodes_in_next_layer=0
        self.reached_end=False          #Neu tim duoc end thi bang True
        self.visited=np.zeros((self.R,self.C),dtype=np.bool)         #Ma tran danh dau nhung diem da di hoac chua
        self.dr = [-1,+1,0,0]             #huong bac, huong nam, huong dong, huong tay
        self.dc = [0,0,+1,-1]
        self.prev = [[[-1,-1] for x in range(self.C)]for y in range(self.R)]

    def  solve(self):
        self.m[self.er][self.ec]=5
        self.rq.appendleft(self.sr)
        self.cq.appendleft(self.sc)
        self.visited[self.sr][self.sc]=True
        while len(self.rq)>0:
            r = self.rq.pop()
            c = self.cq.pop()
            if self.m[r][c] == 5:
                self.reached_end=True
                break
            self.explore_neighbours(r,c)
            self.nodes_left_in_layer-=1
            if self.nodes_left_in_layer==0:
                self.nodes_left_in_layer=self.nodes_in_next_layer
                self.nodes_in_next_layer=0
                self.move_count+=1

    def explore_neighbours(self,r,c):
        #g=Graphic()
        for i in range(4):
            rr=r + self.dr[i]
            cc=c + self.dc[i]

            if rr >=0 and cc >= 0:
                if rr <self.R and cc < self.C:
                    if self.visited[rr][cc]==False:
                        if self.m[rr][cc]!=1:
                             self.rq.appendleft(rr)
                             self.cq.appendleft(cc)
                             self.visited[rr][cc]=True
                             self.nodes_in_next_layer+=1
                             self.prev[rr][cc]=[r,c]

    def reconstructPath(self):
        path=[]
        aty=self.er
        atx=self.ec
        t=0
        while t<self.move_count+1:
            if aty!=-1 and atx !=-1:
                path.append([aty,atx])
                t+=1
            [aty,atx]=self.prev[aty][atx]
        path.reverse()
        y,x=path[0]
        if y==self.sr and x==self.sc:
            return path
        return []
    def BFS(self):
        area=self.solve()
        road=self.reconstructPath()
        return road
    def area(self):
        return self.prev




def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
def astar(array, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

    return False


'''Here is an example of using my algo with a numpy array,
   astar(array, start, destination)
   astar function returns a list of points (shortest path)'''


# Chi phi duong di theo thu tu trong file input
def tempCost(matrix, map, list):
    cost = 0
    for i in range(len(list)):
        if (i == 0):
            cost += len(astar(matrix, map.getStart(), list[i]))
        if (i == len(list) - 1):
            cost += len(astar(matrix, list[i], map.getEnd()))
        else:
            cost += len(astar(matrix, list[i], list[i + 1]))
    return cost


# Chi phi duong di nho nhat trong cac hoan vi
def minCost(matrix, map):
    permutationsList = list(permutations(map.getDon()))      # Hoan vi cac diem don
    min = tempCost(matrix, map, permutationsList[0])         # Gan chi phi nho nhat la hoan vi dau tien
    rList = permutationsList[0]                              # Gan danh sach diem don theo thu tu la hoan vi dau tien
    for i in range(len(permutationsList)):
        tempList = permutationsList[i]
        for j in range(len(tempList)):
            cost = tempCost(matrix, map, tempList)
            if (cost < min):
                min = cost
                rList = permutationsList[i]
    return rList, min



def xuatDuongDi(matrix, map):                                     #matrix: Ma tran, listPoint: Danh sach cac diem di qua da duoc sap xep(minCost)
    listPoint, cost = minCost(matrix, map)
    for i in range(len(listPoint)):
        if (i == 0):
            listTemp = astar(matrix, map.getStart(), listPoint[i])
            for j in range(len(listTemp)):
                x, y = listTemp[j]
                matrix[x][y] = 2
        if (i == (len(listPoint) - 1)):
            listTemp = astar(matrix, listPoint[i], map.getEnd())
            for j in range(len(listTemp)):
                x, y = listTemp[j]
                matrix[x][y] = 2
        else:
            listTemp = astar(matrix, listPoint[i], listPoint[i + 1])
            for j in range(len(listTemp)):
                x, y = listTemp[j]
                matrix[x][y] = 2
    return cost



#iterative Deepening Search
def ids(maze,Sx,Sy,Ex,Ey):
    #1: wall (can't pass)
    #0: road (can pass)
    #2: best path
    #s: start node
    #e: final node (it can be multiple)
    #fisrt letter of input.txt is columns
    #second letter of input.txt is rows
    #start value: 4     end value: 5    wall value: 1       blank value: 0
    Out = False
    max = 1
    s1 = Sx
    s2 = Sy
    maze[s1][s2] = 4
    e1 = Ex
    e2 = Ey
    maze[e1][e2] = 5
    visited = maze

    Col=len(maze[0])
    Row=len(maze)


    def dfs(s1,s2,depth):
        if visited[s1][s2] == 1 or maze[s1][s2] == 1 or depth > max:
            return False
        visited[s1][s2] = 1
        if maze[s1][s2] == 5:
            return True
        Out = False
        if s1+1 < Col and Out == False:
            Out = dfs(s1+1, s2, depth+1)
        if s2 > 0 and Out == False:
            Out = dfs(s1, s2-1, depth+1)
        if s1 > 0 and Out == False:
            Out = dfs(s1-1, s2, depth+1)
        if s2+1 < Row and Out == False:
            Out = dfs(s1, s2+1, depth+1)
        if Out == True:
            maze[s1][s2] = 2
        return Out

    while Out == False:
        Out = dfs(s1,s2,1)
        visited = [[0 for i in range(Col)] for j in range(Row)]
        max += 1

    maze[s1][s2] = 2
    maze[e1][e2] = 2

    #output: ket qua o dang string
    output=str()
    for row in maze:
        for point in row:
            output = output + str(point)+' '
        output += '\n'

#uniform-cost search
def ucs(maze,Sx,Sy,Ex,Ey):
    #1: wall (can't pass)
    #0: road (can pass)
    #2: best path
    #s: start node
    #e: final node (it can be multiple)

    # test case
    #  size: Column = 5, Row = 5
    # start location = (1, 1)
    # goal location = (2, 5)
    # -----------------------------------------
    # the maze:
    # s  0  0  0  0
    # 1  1  1  1  0
    # 0  0  0  1  0
    # 1  1  0  0  0 
    # 1  e  0  1  1
    # -----------------------------------------

    Col=len(maze[0])
    Row=len(maze)
    Input_cost_path = path_find(Col,Row,(Sx,Sy),(Ex,Ey),maze)
    for x in Input_cost_path:
        maze[x[0]][x[1]] = '2'

    output=str()
    for row in maze:
        for point in row:
            output = output + str(point)+' '
        output += '\n'

    # find the path
    # in this version, we don't show the sum_cost on the screen
    def path_find(Col, Row, start, goal, values):
        # queue holds all the frontier in the form: (sum_cost, [path])
        frontiers = PriorityQueue()
        # the list holds all the cells that have been visited
        cell_visited = []
        path = []
        sum_cost = 0
        # put the root into queue
        frontiers.put((sum_cost, [start]))

        # check if frontiers is empty
        while frontiers.empty() == False:
            # dequeue the frontier with the least cost
            frontier_expand = tuple(frontiers.get(-1))
            sum_cost = frontier_expand[0]
            # a list of tuples
            path = list(frontier_expand[1])
            # get the frontier on the path (a tuple)
            frontier_loc = path[-1]
            cell_visited.append(frontier_loc)
            
            # if reaches to the goal location => return the path and exit
            if frontier_loc == goal:
                return path
            # else we expand the frontier and get its neighbors
            else:
                row_index = frontier_loc[0]
                col_index = frontier_loc[1]
                # add its neighbors into frontiers
                # if cell is NOT on bottom edge
                if row_index != 1 and (row_index - 1, col_index) not in cell_visited:
                    cost = sum_cost + values[row_index - 2][col_index - 1] + 1
                    frontier_path = list(path)
                    frontier_path.append((row_index - 1, col_index))
                    frontier = (cost, frontier_path)
                    frontiers.put(frontier)
                # if cell is NOT on left edge
                if col_index != 1 and (row_index, col_index - 1) not in cell_visited:
                    cost = sum_cost + values[row_index - 1][col_index - 2] + 1
                    frontier_path = list(path)
                    frontier_path.append((row_index, col_index - 1))
                    frontier = (cost, frontier_path)
                    frontiers.put(frontier)
                # if cell is NOT on top edge
                if row_index != Row and (row_index + 1, col_index) not in cell_visited:
                    cost = sum_cost + values[row_index][col_index - 1] + 1
                    frontier_path = list(path)
                    frontier_path.append((row_index + 1, col_index))
                    frontier = (cost, frontier_path)
                    frontiers.put(frontier)
                # if cell is NOT on right edge
                if col_index != Col and (row_index, col_index + 1) not in cell_visited:
                    cost = sum_cost + values[row_index - 1][col_index] + 1
                    frontier_path = list(path)
                    frontier_path.append((row_index, col_index + 1))
                    frontier = (cost, frontier_path)
                    frontiers.put(frontier)
