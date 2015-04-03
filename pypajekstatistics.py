# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
 


# from igraph import *
import igraph   

print "Hello World"

idx = 2;
degree = [2,4,6,8]
size = [20, 50, 100, 1000, 10000, 100000]


g = igraph.read('net/S'+str(size[idx])+'-D'+str(degree[idx])+'.net')

print g


#  
g.summary()
#'IGRAPH U--- 50 250 -- \n+ attr: id (v)'
g.get_edgelist()
#[(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10)]
g.vs['id'] # vertex
#['l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l11', 'l12', 'l13', 'l14']...
g.es  # edges
#
g.attributes() # retorna una llista de params
g.vs[0]
# ... acceder como un array object
g.degree()
#"[28, 30, 26, 30, 25, 28, 31, 26, 25, 27, 7, 7, 9, 6, 12, ... ]"
g.betweenness()
g.edge_betweenness()
g.pagerank() #  google page rank
g.evcent() # eigenvector centrality

## maximum and minimum degree
print "A parte 1"
print "maximum degree :kmax:"
degMax =  max(g.degree())
print degMax
print "minimum degree :kmin:"
degMin = min(g.degree())
print degMin

print "A parte 2"
# g.vs.select(_degree)
for idx in range(degMin, degMax+1):
    print idx,  len(g.vs.select(_degree_eq = idx )),  ()


## connections witht the highest betweeness
ebs = g.edge_betweenness()
max_eb = max(ebs)
print "maximum betweeness"
print [g.es[idx].tuple for idx,  eb in enumerate(ebs) if eb == max_eb]


# Querying vertices and edges based on attributes

print "node with maximum degree"
print g.vs.select(_degree = g.maxdegree())['id']
print 'node with minimum degree is'
print degree,  idx

# Querying odd vertices ... // lambda tipo map-reduce


only_odd_vertices = g.vs.select(lambda vertex: vertex.index % 2 == 1)
print len(only_odd_vertices)


# Layout and Plotting
# something called cairo librari REQUIRED 
 

print "END OF SCRIPT..."
    
    # basic graph analysis...
    
    
    
    
    
