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
        class Graph:

	def __init__(self,V): 
		self.V = V     
		self.adj = [[] for i in range(V)]

	def addEdge(self, v, w):
		self.adj[v].append(w)

	def BFS(self, s, goal):
		visited = [False for i in range(self.V)]
		queue = []
		queue.append(s)
		visited[s] = True

		while queue:
			s = queue.pop(0)
			print(s, end=" ")
			if s == goal:
				return True
			
			for i in self.adj[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True
		
		return False

if __name__ == '__main__':

	g = Graph(7);
	g.addEdge(0, 1);
	g.addEdge(0, 2);
	g.addEdge(1, 3);
	g.addEdge(1, 4);
	g.addEdge(2, 5);
	g.addEdge(2, 6);
	print("Following is Breadth First Traversal")
	val = g.BFS(0,8)
	if val == False:
		print("Not Found")
        '''
        print(string)

    def minimax():
        string = '''
        nodes = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': None,
    'D': ['G', 'H'],
    'E': None,
    'F': None,
    'G': ['I'],
    'H': None,
    'I': None,
}

costs = {
    'A': None,
    'B': None,
    'C': 1,
    'D': None,
    'E': -1,
    'F': -1,
    'G': None,
    'H': -1,
    'I': 1,
}

minmax = {
    'A': 'max',
    'B': 'min',
    'C': 'min',
    'D': 'min',
    'E': 'max',
    'F': 'max',
    'G': 'max',
    'H': 'max',
    'I': 'min',
}


def get_child_cost(x):
    ans = []
    if nodes[x] == None:
        print(f'{x} -> {costs[x]}')
        return costs[x]
    else:
        for i in nodes[x]:
            ans.append(get_child_cost(i))
        if minmax[x] == 'min':
            ans = min(ans)
            costs[x] = ans
        else:
            ans = max(ans)
            costs[x] = ans
        print(f'{x} -> {costs[x]}')
        return ans
temp = get_child_cost(list(nodes.keys())[0])
print(f'Final Answer: {temp}')
        '''
        print(string)

    def bfs2():
        string = '''
        class Node:
	def __init__(self, value):
		self.value = value
		self.children = []

def bfs(start_node, goal_node):
	visited = set()
	queue = [(start_node, [start_node.value], 0)]  # add path cost to the queue
	while queue:
		(node, path, cost) = queue.pop(0)
		if node.value == goal_node:
			return (path, cost)  # return both path and cost
		visited.add(node)
		for child in node.children:
			if child not in visited:
				queue.append((child, path + [child.value], cost + 1))  # update path cost
	return (None, None)

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')

a.children = [b, c]
b.children = [d, e]
c.children = [f, g]
g.children = [h]

optimal_path, path_cost = bfs(a, 'H')  # unpack both path and cost
if optimal_path is not None:
    print(f'Optimal path: {optimal_path}')
    print(f'Path cost: {path_cost}')
else:
    print('Path not found')
        '''
        print(string)

    def fol():
        string = '''
        Prolog Code:
    Facts:
John is a person.
Diabetes is a disease.
John has a glucose level of 110.
John has a blood pressure of 110/80
A person has hypertension if their systolic blood pressure is greater than or equal to 140 and their diastolic blood pressure is greater than or equal to 90.
A person has prediabetes if their glucose level is greater than or equal to 100 and less than or equal to 125.
A person is at risk if they have either pre-diabetes or hypertension.

To Prove:
               John has the risk of diabetes

Code:
% Facts
person(john). % John is a person
glucose_level(john, 110). % John has a glucose level of 110.
blood_pressure(john, 110, 80). % John has a blood pressure of 110/80.

% Rules
hypertension(Patient) :-
    blood_pressure(Patient, Systolic, Diastolic),
    Systolic >= 140,
    Diastolic >= 90.
prediabetes(Patient) :-
    glucose_level(Patient, Glucose),
    Glucose >= 100,
    Glucose =< 125.
at_risk(Patient) :- % A person is at risk if they have either pre-diabetes or hypertension.
    (prediabetes(Patient); hypertension(Patient)).
        '''
        print(string)

    def astar2():
        string = '''
        def aStarAlgo(start_node, stop_node):
	open_set= set(start_node)
	closed_set = set()
	g = {}
	parents ={}
	g[start_node] = 0
	parents[start_node] = 0
	counter = 0
	print(f'\nIteration {counter}:')
	print(f'Open:', open_set)
	print(f'Close:', closed_set)
	while len(open_set) > 0:
		n = None
		for v in open_set:
			if n ==None or g[v] + heuristic(v) < g[n] +heuristic(n):
				n=v
			print(f'{v} --> {g[v] + heuristic(v)}')
			pathCost= g[n] + heuristic(n)
		if n == stop_node or Graph_nodes[n] == None:
			pass
		else:
			for (m, weight) in get_neighbors(n):
				if m not in open_set and m not in closed_set:
					open_set.add(m)
					parents[m] = n
					g[m] = g[n] + weight
				else:
					if g[m] > g[n] + weight:
						g[m] = g[n] + weight
						parents[m] = n
						if m in closed_set:
							closed_set.remove(m)
							open_set.add(m)
		if n == None:
			print('Path does not exist')
			return None
		if n == stop_node:
			path = []
			while n in parents and parents[n] != n:
				path.append(n)
				n=parents[n]
			path.append(start_node)
			path.reverse()
			path.remove(start_node)
			counter += 1
			print(f'\nIteration {counter}:')
			print('Path found: {}'.format(path))
			print('Path Cost: {}\n\n'.format(pathCost))
			return path
		open_set.remove(n)
		closed_set.add(n)
		counter += 1
		print(f'\nIteration {counter}:')
		print(f'Open:', open_set)
		print(f'Close:', closed_set)
	print('Path does not exist')
	return None

def get_neighbors(v):
	if v in Graph_nodes:
		return Graph_nodes[v]
	else:
		return None

def heuristic(n):
	H_dist = {
		'S':5,
		'A':3,
		'B':4,
		'C':2,
		'D':6,
		'G':0
	}
	return H_dist[n]
Graph_nodes = {
	'S':[('A',1), ('G',10)],
	'A':[('B',2), ('C',1)],
	'C':[('D',3), ('G',4)],
	'B':[('D',5)],
	'D':[('G',2)]
}
aStarAlgo('S', 'G')
        '''
        print(string)

    def wumpus():
        string = '''
        % NOTE:
%	- To run the program, execute the following query:
%				start; printResult.
%
%	- To see the status of each move the agent makes,
%	  uncomment the first line of the first occurrence of
%	  the predicate start_searching.
%

:- dynamic([
  world_size/1,	% Size of the board as [X, Y]
  position/2,		% position as (A, [X, Y]) implying location of A is [X, Y]
  wumpus/1,		% Possible position of Wumpus to be inferred from smell
  noPit/1,		% noPit([X, Y]) means agent is sure there is no pit on [X, Y] cell, inferred from no breeze on adjacent cell(s)
  noWumpus/1,		% noWumpus([X, Y]) means agent is sure there is no Wumpus on [X, Y] cell, inferred from no smell on adjacent cell(s)
  maybeVisitLater/2,	% if no adjacent cell to go to, add the current cell as a probable point to visit later and backtrack
  goldPath/1		% agent stores each path from [1, 1] cell to the Gold retrieved
]).

%% The starting point for execution
start:-
  % make sure to clear any previous facts stored
  retractall(wumpus(_)),
  retractall(noPit(_)),
  retractall(noWumpus(_)),
  retractall(maybeVisitLater(_,_)),
  retractall(goldPath(_)),

  % initializations
  init_board,
  init_agent,
  init_wumpus,

  % agent starts searching from [1, 1] cell
  start_searching([1, 1], []),

  % if any paths stored as possible to visit later, do so
  maybeVisitLater(PausedCell, LeadingPath),
  retract(maybeVisitLater(PausedCell, _)),
  start_searching(PausedCell, LeadingPath).

%% INITIALIZING THE BOARD WITH PITS & GOLD
init_board:-
  retractall(world_size(_)),
  assert(world_size([5, 5])),		% dimensions of the board

  retractall(position(_, _)),
  assert(position(gold, [2, 3])),		% position of gold

  % positions of pits
  assert(position(pit, [3, 1])),
  assert(position(pit, [5, 1])),
  assert(position(pit, [3, 3])),
  assert(position(pit, [4, 4])),
  assert(position(pit, [2, 5])),

  assert(noPit([1, 1])).		% There cannot be pit at [1, 1] where agent starts.

%% INITIALIZING THE AGENT IN THE BOARD
init_agent:-
  assert(position(agent, [1, 1])).

%% INITIALIZING THE WUMPUS IN THE BOARD
init_wumpus:-
  assert(position(wumpus, [1, 3])),
  assert(noWumpus([1, 1])).


%% DEFINING THE PERCEPTORS

% Helper predicate to check if cell position given is valid in the board.
valid_position([X, Y]):- X>0, Y>0, world_size([P, Q]), X@=<P, Y@=<Q.

% Generate adjacent positions of a given position.
adjacent([X, Y], Z):- Left is X-1, valid_position([Left, Y]), Z=[Left, Y].
adjacent([X, Y], Z):- Right is X+1, valid_position([Right, Y]), Z=[Right, Y].
adjacent([X, Y], Z):- Above is Y+1, valid_position([X, Above]), Z=[X, Above].
adjacent([X, Y], Z):- Below is Y-1, valid_position([X, Below]), Z=[X, Below].

% A position is smelly if a cell with Wumpus is adjacent to it. There has to be at least one wumpus first.
is_smelly([X, Y]):-
  position(wumpus, Z), \+ noWumpus(Z),
  adjacent([X, Y], Z).

% A position is breezy if a cell adjacent to it contains pit.
is_breezy([X, Y]):- adjacent([X, Y], Z), position(pit, Z).

% A position is glittery if the cell contains gold.
is_glittery([X, Y]):- position(gold, Z), Z==[X, Y].



%% TAKING THE ACTIONS

% Utility predicate checking if two different matches can be found to ascertain Wumpus' location.
moreThanOneWumpus:-
  wumpus(X), wumpus(Y), X\=Y.

% Confirming there are no more than one possible recordings of Wumpus based on smell perceived,
% then killing Wumpus from a cell that aligns in a straight line with the Wumpus' cell.
killWumpusIfPossible(AgentCell):-
  wumpus([Xw, Yw]), \+ moreThanOneWumpus,	% ascertain Wumpus' cell
  AgentCell=[Xa, Ya],
  (Xw==Xa; Yw==Ya),			% check Agent is in a cell that's in a straight line as Wumpus' cell
  assert(noWumpus([Xw, Yw])),		% record that Wumpus is not in the board anymore as it is considered killed
  format('~nAgent confirmed Wumpus cell to be ~w and shot an arrow from cell ~w.~nThe WUMPUS has been killed!~n', [[Xw, Yw], AgentCell]),
  retractall(wumpus(_)).


%% Searching takes place as a series of checkings. If and when the first predicate fails,
%  or completes, the second predicate of the same name is tried.

% Check if the cell contains gold
start_searching(Cell, LeadingPath):-
  % printStatus(Cell, LeadingPath),		% remove comment to print status at each move
  is_glittery(Cell),
  append(LeadingPath, [Cell], CurrentPath),
  % record the gold path if it's not already done
  \+ goldPath(CurrentPath), assert(goldPath(CurrentPath)).

% Check if the agent can perceive breeze in the cell
start_searching(Cell, _):-
  is_breezy(Cell).
  % format('BREEZE detected!~n').

% Check if the agent cannot perceive breeze.
% This is important as it gives CERTAINTY that adjacent cells do not have pit.
start_searching(Cell, _):-
  \+ is_breezy(Cell),
  adjacent(Cell, X),
  \+ noPit(X), assert(noPit(X)).

% Check if the agent can perceive smell at this cell.
% If smelly, record that adjacent cells may have Wumpus.
start_searching(Cell, _):-
  is_smelly(Cell),
  adjacent(Cell, X),
  \+ noWumpus(X), assert(wumpus(X)).

% If the cell doesn't have smell, record that the adjacent cells certainly do NOT have Wumpus.
start_searching(Cell, _):-
  \+ is_smelly(Cell),
  adjacent(Cell, X),
  \+ noWumpus(X), assert(noWumpus(X)),
  wumpus(Y), X==Y, retract(wumpus(Y)).

% Otherwise, try to see and do if it is feasible to kill Wumpus from this cell,
% then find neighboring cells that are safe and visit recursively.
start_searching(CurrentCell, LeadingPath):-
  (killWumpusIfPossible(CurrentCell); format('')),	% Kill Wumpus if possible, else do nothing.

  append(LeadingPath, [CurrentCell], CurrentPath),

  \+ is_glittery(CurrentCell),	% We don't wanna explore further if we reach the gold.

  % get adjacent cells
  adjacent(CurrentCell, X), \+ member(X, LeadingPath),

  % if the adjacent cells are not safe, marked as maybe Wumpus or maybe Pit,
  % put these to maybeVisitLater, so if inferred later to be safe, we will visit later.
  (( noWumpus(X), noPit(X)) -> write('');
    (\+ maybeVisitLater(CurrentCell, _) -> assert(maybeVisitLater(CurrentCell, LeadingPath)); write(''))
  ),

  % Of those that the agent knows to be safe (no Wumpus/pit), start searching from them.
  noWumpus(X), noPit(X),
  start_searching(X, CurrentPath).



%% OUTPUTTING THE STATUS & RESULTS

% The first result type is NO gold paths found and print result accordingly.
printResult:-
  \+ goldPath(_), write("==> Actually, no possible paths found! :(").

% The second result type is gold paths found, print the paths.
printResult:-
  goldPath(_), !, format('The following paths to the Gold are found: ~n'),
  forall(goldPath(X), writeln(X)).

% Print the status of any given cell from during the search.
printStatus(Cell, LeadingPath):-
  format('~n--------------- STATUS ---------------~nCurrently in ~w~nLeading path: ~w~n', [Cell, LeadingPath]),
  write('WUMPUS: '),
  forall(wumpus(X), writeln(X)),nl,
  write('NO PIT: '),
  forall(noPit(Y), writeln(Y)),
  write('NO WUMPUS: '),
  forall(noWumpus(Z), writeln(Z)),
  write('MAYBE VISIT LATER: '),
  forall(maybeVisitLater(M, _), writeln(M)),
  format('~n-----------------------~n~n').
        '''
        print(string)

    def dls():
        string = '''
        class Node:
    def __init__(self, state, parent, move):
        self.state = state
        self.parent = parent
        self.move = move
        
    def __str__(self):
        return str(self.state)

def depth_limited_search(start_state, goal_state, limit):
    start_node = Node(start_state, None, None)

    if start_state == goal_state:
        return start_node

    frontier = [start_node]
    explored = []
    depth = 0

    while frontier:
        if depth > limit:
            return None

        node = frontier.pop(0)
        explored.append(node)
        for move, new_state in get_successors(node.state):
            if new_state == goal_state:
                return Node(new_state, node, move)
            if not any(new_state == n.state for n in explored) and not any(new_state == n.state for n in frontier):
                child_node = Node(new_state, node, move)
                frontier.append(child_node)
                print(child_node)

        if not frontier:
            return None
        depth = node_depth(frontier[0])
    return None

def get_successors(state):
    successors = []
    blank_index = state.index(0)
    if blank_index not in [0, 1, 2]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
        successors.append(('UP', new_state))
    if blank_index not in [6, 7, 8]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
        successors.append(('DOWN', new_state))
    if blank_index not in [0, 3, 6]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        successors.append(('LEFT', new_state))
    if blank_index not in [2, 5, 8]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        successors.append(('RIGHT', new_state))

    return successors

def node_depth(node):
    depth = 0
    while node.parent:
        depth += 1
        node = node.parent
    return depth

def print_tree(node):
    if node.parent:
        print_tree(node.parent)
    print(node)

if __name__ == '__main__':
    start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    depth_limit = int(input("Enter depth limit: "))
    solution = depth_limited_search(start_state, goal_state, depth_limit)
    if solution:
        print("Solution found at depth:", node_depth(solution))
        print_tree(solution)
    else:
        print("Solution not found within depth limit.")
        '''
        print(string)

    def main():
        print("waterjug()")
        print("tower()")
        print("dfs()")
        print("bbn()")
        print("astar()")
        print("astar2()")
        print("adversial()")
        print("bfs()")
        print("bfs2()")
        print("minimax()")
        print("fol()")
        print("wumpus()")
        print("dls()")


