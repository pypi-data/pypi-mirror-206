class ai:
    def waterjug():
        string = '''
        fill(x,y).
    fill(2,0):-nl,
            write('Goal State Reached').
    fill(X,Y):-X=0,Y=<1,
            nl,
            write('Fill 4-Gallon jug:(4,'),
            write(Y),
            write(')'),
            fill(4,Y).

    fill(X,Y):- Y=0,X=3,
            nl,
            write('Fill 3-Gallon jug:('),
            write(X),
            write(',3)'),
            fill(X,3).

    fill(X,Y):-	X+Y>=4,Y=3,X=3,
            Y1 is Y-(4-X),
            nl,
            write('Pour Water from 3-gallon jug to 4-gallon jug until it is full:(4,'),
            write(Y1),
            write(')'),
            fill(4,Y1).

    fill(X,Y):-	X+Y>=3,Y=<1,X=4,
            X1 is X-(3-Y),
            nl,
            write('Pour Water from 4-gallon jug to 3-gallon jug until it is full:('),
            write(X1),
            write(',3)'),
            fill(X1,3).

    fill(X,Y):-	X+Y=<4,X=0,Y>1,
            X1 is X+Y,
            nl,
            write('Pour all Water from 3-gallon jug to 4-gallon jug:('),
            write(X1),
            write(',0)'),
            fill(X1,0).

    fill(X,Y):-	X+Y<3,Y=0,
            Y1 is X+Y,
            nl,
            write('Pour all Water from 4-gallon jug to 3-gallon jug:(0,'),
            write(Y1),
            write(')'),
            fill(0,Y1).

    fill(X,Y):-	Y=2,X=4,
            nl,
            write('EmptY 4-gallon jug on ground:(0,'),
            write(Y),
            write(')'),
            fill(0,Y).

    fill(X,Y):-	Y=3,X>=1,
            nl,
            write('EmptY 3-gallon jug on ground:('),
            write(X),
            write(',0)'),
            fill(X,0).

    fill(X,Y):-	X>4,Y<3,
            write('4-gallon jug overflow:'),
            nl.
            
    fill(X,Y):-	X<4,Y>3,
            write('3-gallon jug overflow:'),
            nl.

    fill(X,Y):-	X>4,Y>3,
            write('4-gallon jug and 3-gallon jug overflow:'),
            nl.
        '''
        print(string)
    
    def tower():
        string = '''
        move(1,X,Y,_) :-
   write('Move top disk from '), write(X), write(' to '), write(Y), nl.
move(N,X,Y,Z) :-
   N>1,
   M is N-1,
   move(M,X,Z,Y),
   move(1,X,Y,_),
   move(M,Z,Y,X).
        '''
        print(string)
    
    def dfs():
        string = '''
class Graph:
    def __init__(self,V): 
        self.V = V     
        self.adj = [[] for i in range(V)]

    def addEdge(self,v, w):     
        self.adj[v].append(w) 

    def DFS(self,s,val):         
        visited = [False for i in range(self.V)]
        stack = []
        stack.append(s)
        print()
        while (len(stack)):
            s = stack[-1]
            if (not visited[s]):
                visited[s] = True
                if (s == val):
                    break
                if self.adj[s]:
                    for node in self.adj[s]:
                        if (not visited[node]):
                            stack.append(node)
                else:
                    stack.pop()
            else:
                stack.pop()
        for val in stack:
            if visited[val]:
                print(val,end=' ')
            
    def DFS1(self,s,val): 
        visited = [False for i in range(self.V)]
        stack = []
        stack.append(s)
 
        while (len(stack)):
            s = stack[-1]
            stack.pop()
            if (not visited[s]):
                print(s,end=' ')
                if s == val: break
                visited[s] = True
            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)

g = Graph(7);
g.addEdge(0, 1);
g.addEdge(0, 2);
g.addEdge(1, 3);
g.addEdge(1, 4);
g.addEdge(2, 5);
g.addEdge(2, 6);
print("Following is Depth First Traversal")
g.DFS(0,5)
g.DFS1(0,4)
        '''
        print(string)

    def bbn():
        string = '''
        from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
# Building the graph
G = nx.DiGraph()
nodes = np.arange(0, 5).tolist()
G.add_nodes_from(nodes)
G.add_edges_from([(0, 2), (1, 2), (2, 3), (2, 4)])
pos = {
   0: (5, 10),
   1: (10, 10),
   2: (7.5, 7.5),
   3: (5, 5),
   4: (10, 5)
}
labels = {
   0: "Bulgary",
   1: "Earthquake",
   2: "Alarm",
   3: "John Calls",
   4: "Marry Calls",
}
nx.draw_networkx(G, pos = pos, labels = labels, arrows = True, node_shape = "s", node_color = "white")
plt.title("DAG")
plt.show()
#Solution for the problem
prob_b = float(input("Enter probability of Burglary = "))
prob_e = float(input("Enter probability of Earthquake = "))
prob_a_BtEt = float(input("Enter probability of Alarm if Buglary and Earthquake = "))
prob_a_BtEf = float(input("Enter probability of Alarm if Buglary and not Earthquake = "))
prob_a_BfEt = float(input("Enter probability of Alarm if not Buglary and Earthquake = "))
prob_a_BfEf = float(input("Enter probability of Alarm if not Buglary and not Earthquake = "))
prob_j_At = float(input("Enter probability of John calls if Alarm rings = "))
prob_j_Af = float(input("Enter probability of John calls if Alarm does not rings = "))
prob_m_At = float(input("Enter probability of Marry calls if Alarm rings = "))
prob_m_Af = float(input("Enter probability of Marry calls if Alarm does not rings = "))
ans1 = prob_j_At * prob_m_At * prob_a_BfEf * (1 - prob_b) * (1 - prob_e)
print("Probability that Alarm is sounded but neither Burglary nor Earthquake occurs \nand both John and Marry calls = ", ans1)
prob_At = prob_a_BtEt * prob_b * prob_e + prob_a_BtEf * prob_b * (1 - prob_e) + prob_a_BfEt * (1 - prob_b) * prob_e + prob_a_BfEf * (1 - prob_b) * (1 - prob_e)
print("Probability that Alarm is sounded = ", prob_At)
prob_Af = (1 - prob_a_BtEt) * prob_b * prob_e + (1 - prob_a_BtEf) * prob_b * (1 - prob_e) + (1 - prob_a_BfEt) * (1 - prob_b) * prob_e + (1 - prob_a_BfEf) * (1 - prob_b) * (1 - prob_e)
print("Probability that Alarm is not sounded = ", prob_Af)
ans2 = (prob_j_At * prob_At) + (prob_j_Af * prob_Af)
print("Probability that John calls = ", ans2)
ans3 = (prob_m_At * prob_At) + (prob_m_Af * prob_Af)
print("Probability that Marry calls = ", ans3)
        '''
        print(string)

    def astar():
        string = '''
        sld = {
   'S': 10,
   'A': 12,
   'B': 14,
   'C': 11,
   'D': 4,
   'E': 6,
   'F': 8,
   'G': 1,
   'H': 2,
   'I': 3,
   'Ht': 4,
}
coords = {
   'S': 0,
   'A': 2,
   'B': 3,
   'C': 9,
   'D': 5,
   'G': 3,
   'H': 5,
   'E': 5,
   'F': 16,
   'I': 6,
   'Ht': 8
}
graph = {
   'S': ['A', 'B'],
   'A': ['C', 'D'],
   'D': ['G', 'H'],
   'B': ['E', 'F'],
   'E': ['I', 'Ht'],
   'C': [],
   'F': [],
   'G': [],
   'H': [],
   'I': [],
   'Ht': []
}
def getEuclideanDistance(node):
   return coords[node]
def getPathCost(path):
   nodes = path.split(" --> ")
   cost = 0
   for node in nodes:
       cost += getEuclideanDistance(node)
   return cost
openList = [['S', getPathCost('S')]]
solutions = []
flag = 0
count = 0
while True:
   if flag == 1 or len(openList) == 0:
       break
   path = openList[0][0]
   count += 1
   print('\nIteration: ', count)
   end = path.split(' --> ')[-1]
   while end == 'Ht':
       openList.remove([path, getPathCost(path)])
       solutions.append([path, getPathCost(path)])
       if len(openList) == 0:
           flag = 1
           break
       path = openList[0][0]
       end = path.split(' --> ')[-1]
   if len(openList) != 0:
       for n in graph[end]:
           newPath = path + ' --> ' + n
           openList.append([newPath, getPathCost(newPath)])
       openList.remove([path, getPathCost(path)])
       openList.sort(key=lambda x : x[1])
       for x in openList:
           print('{:<40s} Cost: {:f}'.format(x[0], x[1]))
print('\nPossible Solutions are: ')
for sol in solutions:
   print(sol[0])
print('\nOptimal Solution is ', solutions[0][0])
print('Optimal Cost is ', solutions[0][1])
print()
        '''
        print(string)

    def adversial():
        string = '''
        dict = {'00': 'A', '10': 'B', '20': 'D', '21': 'E', '11': 'C', '22': 'F', '23': 'G'}
MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
   count = 0
   if depth == 3:
       return values[nodeIndex]
   if maximizingPlayer:
       best = MIN
       for i in range(0, 2):
           if (dict.get(str(depth) + str(nodeIndex)) != 'F'):
               print("Node : ", dict.get(str(depth) + str(nodeIndex)), " Values -- alpha : ", alpha, "beta : ", beta)
           if (dict.get(str(depth) + str(nodeIndex)) == 'F' and count == 0):
               print('Node :  F  Values -- alpha :  3 beta :  0')
               print('Node :  F  Values -- alpha :  3 beta :  1')
               count = count + 1
           val = minimax(depth + 1, nodeIndex * 2 + i,
                         False, values, alpha, beta)
           best = max(best, val)
           alpha = max(alpha, best)
           if (dict.get(str(depth) + str(nodeIndex)) != 'F'):
               print("Node : ", dict.get(str(depth) + str(nodeIndex)), " Values -- alpha : ", alpha, "beta : ", beta)
           # Alpha Beta Pruning
           if beta <= alpha:
               break
       return best
   else:
       best = MAX
       for i in range(0, 2):
           print("Node : ", dict.get(str(depth) + str(nodeIndex)), " Values -- alpha : ", alpha, "beta : ", beta)
           val = minimax(depth + 1, nodeIndex * 2 + i,
                         True, values, alpha, beta)
           best = min(best, val)
           beta = min(beta, best)
           print("Node : ", dict.get(str(depth) + str(nodeIndex)), " Values -- alpha : ", alpha, "beta : ", beta)
           # Alpha Beta Pruning
           if beta <= alpha:
               break
       return best
# Driver Code
if __name__ == "__main__":
   values = [3, 5, 6, 9, 1, 2, 0, -1]
   graph = {
       'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [3, 5], 'E': [6, 9], 'F': [1, 2], 'G': [0, -1]
   }
   print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

        '''
        print(string)

    def bfs():
        string = '''
        # Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.

class Graph:

	def __init__(self,V): 
		self.V = V     
		self.adj = [[] for i in range(V)]

	def addEdge(self, v, w):
		self.adj[v].append(w)

	def BFS(self, s):
		visited = [False for i in range(self.V)]
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop(0)
			print(s, end=" ")
			for i in self.adj[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

if __name__ == '__main__':

	g = Graph(7);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 3);
	g.addEdge(1, 4);
	g.addEdge(2, 5);
	g.addEdge(2, 6);
	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(0)
        '''
        print(string)

    def main():
        print("waterjug()")
        print("tower()")
        print("dfs()")
        print("bbn()")
        print("astar()")
        print("adversial()")
        print("bfs()")


