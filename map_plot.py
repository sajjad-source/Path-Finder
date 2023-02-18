#Author: Sajjad C Kareem
#Date: 11.13.2022
#Purpose: Plot map

from cs1lib import *
from Vertex import Vertex
from load_graph import load_graph
from bfs import bfs


WIDTH = 1012 #width of screen
HEIGHT = 811 #height of screen
image = load_image('dartmouth_map.png') #load image
vertex_dict = load_graph("dartmouth_graph.txt") #get the vertex dict from load graph
m_pressed = False #set mouse press as False
start = None #starting vertex is None
end = None #ending vertex is None

mouse_x, mouse_y, hover_x, hover_y = 0, 0, 0, 0 #set press and hover mouse coord to 0

def mousePress(mx, my): #mosue press func
    global m_pressed, mouse_x, mouse_y #global var
    m_pressed = True #set mouse press to True
    if m_pressed: #if it is True
        mouse_x = mx #return the mouse press coord
        mouse_y = my #return the mouse press coord


def mouseMove(mx, my): #mouse move func
    global hover_x, hover_y #global var

    hover_x = mx #return mouse hover coord
    hover_y = my #return omuse hover coord



def main(): #main func
    global start, end #global vars
    draw_image(image, 0, 0) #draw image of the map

    for vertex in vertex_dict: #for each vertex in the vertex dict
        vertex_dict[vertex].draw_vertex(0, 0, 1) #draw the vertex
        vertex_dict[vertex].draw_all_edges(0, 0, 1) #draw all the edges adjacent to such vertex

    for vertex in vertex_dict: #for each vertex in vertex dict
        if m_pressed: #if the mouse is pressed
            if vertex_dict[vertex].onVertex(mouse_x, mouse_y): #check if mouse x, y is in area of that vertex
                vertex_dict[vertex].draw_vertex(1, 0, 0) #if it is, draw the vertex to be red
                start = vertex_dict[vertex] #set that vertex as the starting vertex

    if start is not None: #if start is not None, i.e. we already have a start vertex
        for vertex in vertex_dict: #for each vertex in vertex dict
            if vertex_dict[vertex].onVertex(hover_x, hover_y): #check if the mouse is hovering on one
                vertex_dict[vertex].draw_vertex(1, 0, 0) #if it is, draw it red
                end = vertex_dict[vertex] #set that vertex as the end/goal


    if start is not None and end is not None: #if there is both a start AND an end
        path = bfs(start, end) #return the path from bfs
        i = 0 #starting index at 0
        while i < len(path) - 1: #while index less than length of path - 1
            path[i].draw_edge(path[i + 1], 1, 0, 0) #draw the edge between the vertex at that index and the one ahead of it only
            path[i].draw_vertex(1, 0, 0) #change that vertex to red
            i += 1 #increment i


start_graphics(main, width=WIDTH, height=HEIGHT, mouse_press=mousePress, mouse_move=mouseMove)

