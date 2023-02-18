# Author: Sajjad
# Date: 11.12.2022
# Purpose: Load graph
from Vertex import Vertex


def parse_line(line):
    section_split = line.split(";") #split the sections by ;
    vertex_name = section_split[0].strip() #the vertex name is the first index of the 3 sections

    adjacent_vertices = section_split[1].strip().split(",") #adjecent vertices is the 2nd index

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    coordinates = section_split[2].strip().split(',') #coordinates is the 3rd index
    x = coordinates[0].strip() #the x coordinate is the 1st value in the coordinates list
    y = coordinates[1].strip() #the y coordinate is the 2nd value in the coordinates list

    return vertex_name, adjacent, x, y #return


def load_graph(file):
    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    files = open(file, "r")

    for l in files:

        # if this is a line in the correct format:
        if len(l.split(";")) == 3:
            vertex_name, adjacent_vertices, x, y = parse_line(l) #call parse line func
            v = Vertex(vertex_name, x, y) #create vertex Object with the name and coordinates
            vertex_dict[vertex_name] = v #assign to vertex dict with name as key and object as value

    files.close()

    files = open(file, "r") #read into file again
    for l in files: #for each line in the file

        if len(l.split(';')) == 3: #if the line is in correct format
            vertex_name, adjacent_vertices, x, y = parse_line(l) #call parse line func and return the name, adj, coord
            v_obj = vertex_dict[vertex_name] #get reference to vertex object

            for adj_name in adjacent_vertices: #for each adj vertex in the adj vertices
                adj_obj = vertex_dict[adj_name] #get the adj object from the vertex dict
                v_obj.adj_list.append(adj_obj) #append that adj object

    files.close()
    return vertex_dict #return vertex dict


graph_dict = load_graph('dartmouth_graph.txt')