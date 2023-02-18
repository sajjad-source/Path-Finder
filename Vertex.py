#Author: Sajjad
#Date: 11.12.2022
#Purpose: Vertex class
from cs1lib import *


class Vertex:
    def __init__(self, name, x, y): #initialize
        self.name = name #string name
        self.x = int(x) #convert x coord to int
        self.y = int(y) #convert y coord to int
        self.adj_list = [] #adj vertices
        self.radius = 7 #radius of vertices
        self.width = 3 #width of edges


    def __str__(self):
        names = '' #initialize empty adjacent vertices string
        for adj in self.adj_list: #for every adj in the adj list
            if adj != self.adj_list[-1]: #if it is not the first one
                names += adj.name + ', ' #add the str of the adj to the name list with a ','
            else: #else if it is first
                names += adj.name  #exclude the comma

        return f"{self.name}; Location: {self.x}, {self.y}; Adjacent vertices: {names}" #return this formatted string


    def draw_vertex(self, r, g, b): #draw vertex with rgb colors parameter
        disable_stroke() #disable circle stroke
        set_fill_color(r, g, b) #set fill color
        draw_circle(self.x, self.y, self.radius) #draw circle of vertex at its x, y coord


    def draw_edge(self, other, r, g, b): #draw edges between self and other vertex
        enable_stroke() #enable line stroke
        set_stroke_width(self.width) #line width
        set_stroke_color(r, g, b) #line color
        draw_line(self.x, self.y, int(other.x), int(other.y)) #draw line between self vertex and other vertex passed


    def draw_all_edges(self, r, g, b): #draw all edges in path
        for adj in self.adj_list: #for all adj vertices
            self.draw_edge(adj, r, g, b) #draw the edges between each one


    def onVertex(self, x, y): #onVertex method to determine if mouse on vertex. Takes mouse coord as parameters
        #if the x and y of the mouse is that in the area of the vertex
        if self.x - self.radius < x < self.x + self.radius and self.y - self.radius < y < self.y + self.radius:
            return True #return True
        else: #else mouse not in the area
            return False #return False


