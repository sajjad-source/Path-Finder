#Author: Sajjad
#Date: 11.14.2022
#Purpose: BFS

from collections import deque



def bfs(start, end):

    frontier = deque()
    backpointer = {}


    frontier.append(start) #Add start to frontier
    backpointer[start] = None #Add start as key and None as value into backpointer dictionary

    while len(frontier) != 0: # while frontier is not empty:

        curr_v = frontier.popleft() # Get a vertex from the front of frontier


        for adj_v in curr_v.adj_list: #for every adj_v in adjacency list of curr_v
            if adj_v not in backpointer: #if adj_v is not visited
                frontier.append(adj_v) #Add adj_v to frontier
                backpointer[adj_v] = curr_v #Add adj_v as key and curr_v as value to backpointer dictionary

        if end in backpointer: #if end goal in backpointer dictionary
            break #break

    path = [] #Initialize path to empty list
    v = end #v = end
    while v is not None: #while v is not None
        path.append(v) #add v to path
        v = backpointer[v] #use v as key and get the backpointer of v and change it to that

    return path #return the path

