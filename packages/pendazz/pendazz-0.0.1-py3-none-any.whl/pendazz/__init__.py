def help():
    return '''
    dfs()
    bfs()
    waterjug()
    npuzzle_dfs()
    npuzzle_bfs()
    npuzzle_astar()
    factorial_prolog()
    boxsolver_prolog()
    list_prolog()
    sum_prolog()
    monkey_prolog()
    '''

def monkey_prolog():
    return '''
    move(state(middle,onbox,middle,hasnot),
        grasp,
        state(middle,onbox,middle,has)).
    move(state(P,onfloor,P,H),
        climb,
        state(P,onbox,P,H)).
    move(state(P,onfloor,P,H),
        drag(P,P1),
        state(P1,onfloor,P1,H)).
    move(state(P,onfloor,Z,H),
        walk(P,P1),
        state(P1,onfloor,Z,H)).

    canget(state(_,_,_,has)).
    canget(State1):-
        move(State1,_,State2),
        canget(State2).

    '''

def sum_prolog():
    return '''
    sum(0,0).
    sum(N,S):-
        N>0,
        N1 is N-1,
        sum(N1,S1),
        S is N+S1.

    '''

def list_prolog():
    return '''
    len([],0).
    len([_|T],R):-
        len(T,R1),
        R is R1+1.


    rev([],[]).
    rev([H|T],R):-
        rev(T,R1),
        append(R1,[H],R).

    '''

def boxsolver_prolog():
    return '''
    getbox(1).
    getbox(2).
    getbox(3).
    getbox(4).
    getbox(5).

    box(1,black,3).
    box(2,black,1).
    box(3,white,1).
    box(4,black,2).
    box(5,white,3).

    owners(A,B,C,D,E):-
        getbox(A),getbox(B),getbox(C),getbox(D),getbox(E),
        A\=B,A\=C,A\=D,A\=E,
        B\=C,B\=D,B\=E,
        C\=D,C\=E,
        D\=E,
    box(A,Acolor,_),box(B,Acolor,_),
    box(D,Dcolor,_),box(E,Dcolor,_),
    box(C,_,Csize),box(D,_,Csize),
    box(E,_,Esize),box(B,_,Bsize),
    Esize<Bsize.
    '''

def factorial_prolog():
    return '''
    factorial(0,1).
factorial(N,S):-
    N>0,
    N1 is N-1,
    factorial(N1,S1),
    S is N*S1.

    '''

def npuzzle_astar():
    return'''
    import numpy as np

    n = int(input("Enter the size of the matrix (nxn): "))

    print("Enter the start matrix: ")
    start_matrix = np.zeros((n,n))
    for i in range(n):
        start_matrix[i] = list(map(int, input().split()))

    print("Enter the end matrix: ")
    end_matrix = np.zeros((n,n))
    for i in range(n):
        end_matrix[i] = list(map(int, input().split()))

    visited = []
    open = []
    closed = []

    closed.append(start_matrix)

    def heuristic(matrix, end_matrix):
        res = matrix==end_matrix
        return n*n - np.count_nonzero(res)

    def possibleChildren(matrix, e_matrix):
        visited.append(matrix)
        [i],[j] = np.where(matrix == 0)
        direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
        children = []
        for dir in direction:
            ni = i + dir[0]
            nj = j + dir[1]
            newMatrix = matrix.copy()
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                newMatrix[i,j], newMatrix[ni, nj] = matrix[ni,nj], matrix[i, j]
                if not(any(np.array_equal(newMatrix, i) for i in visited)):
                    visited.append(newMatrix)
                    newMatrix_heu = heuristic(newMatrix, end_matrix)
                    children.append([newMatrix_heu, newMatrix])

        children = sorted(children, key = lambda x:x[0])
        for i in range(len(children)):
            children[i]=children[i][1]

        return children

    def main(start_matrix, end_matrix):
        start_heuristic = heuristic(start_matrix, end_matrix)
        if start_heuristic==0:
            for node in closed:
                print(node)
            return True
        else:
            children = possibleChildren(start_matrix, end_matrix)
            if(len(children)>0):
                for i in range(len(children)):
                    open.insert(i, children[i])

            if len(open)>0:
                newHeu = heuristic(open[0], end_matrix)
                newMatrix = open[0]
                closed.append(open[0])
                open.pop(0)

                if newHeu==0:
                    for node in closed:
                        print(node)
                    return True
                else:
                    main(newMatrix, end_matrix)
            else:
                return False

    main(start_matrix, end_matrix)
    print(len(visited))

    '''

def npuzzle_bfs():
    return '''
    import numpy as np

    n = int(input("Enter the size of the matrix (nxn): "))

    print("Enter the start matrix: ")
    start_matrix = np.zeros((n,n))
    for i in range(n):
        start_matrix[i] = list(map(int, input().split()))

    print("Enter the end matrix: ")
    end_matrix = np.zeros((n,n))
    for i in range(n):
        end_matrix[i] = list(map(int, input().split()))

    visited = []
    queue = []

    queue.append(start_matrix)
    visited.append(start_matrix)

    def possibleChildren(matrix, e_matrix):
        [i],[j] = np.where(matrix == 0)
        direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
        children = []
        for dir in direction:
            ni = i + dir[0]
            nj = j + dir[1]
            newMatrix = matrix.copy()
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                newMatrix[i,j], newMatrix[ni, nj] = matrix[ni,nj], matrix[i, j]
                if not(any(np.array_equal(newMatrix, i) for i in visited)):
                    visited.append(newMatrix)
                    children.append(newMatrix)

        return children

    def main(start_matrix, end_matrix):
        if np.array_equal(start_matrix, end_matrix):
            for node in visited:
                print(node)
            return True
        else:
            children = possibleChildren(start_matrix, end_matrix)
            if(len(children)>0):
                for child in children:
                    queue.append(child)

            if len(queue)>0:
                newMatrix = queue.pop(0)
                if np.array_equal(newMatrix, end_matrix):
                    for node in visited:
                        print(node)
                    return True
                else:
                    main(newMatrix, end_matrix)
            else:
                return False

    main(start_matrix, end_matrix)
    print(len(visited))

    '''

def npuzzle_dfs():
    return '''
    import numpy as np
    import time

    start = time.time()
    n = int(input("Enter the size of the matrix (nxn): "))

    print("Enter the start matrix: ")
    start_matrix = np.zeros((n,n))
    for i in range(n):
        start_matrix[i] = list(map(int, input().split()))

    print("Enter the end matrix: ")
    end_matrix = np.zeros((n,n))
    for i in range(n):
        end_matrix[i] = list(map(int, input().split()))

    visited = []

    mid1 = time.time()
    def possibleChildren(matrix, e_matrix):
        [i],[j] = np.where(matrix == 0)
        direction = [[-1, 0], [0, -1], [1, 0],[0, 1]]
        children = []
        for dir in direction:
            ni = i + dir[0]
            nj = j + dir[1]
            newMatrix = matrix.copy()
            if(ni>=0 and ni<n and nj>=0 and nj<n):
                newMatrix[i,j], newMatrix[ni, nj] = matrix[ni,nj], matrix[i, j]
                if not(any(np.array_equal(newMatrix, i) for i in visited)):
                    children.append(newMatrix)

        return children



    mid2 = time.time()
    def dfs(start_matrix, end_matrix):
        visited = []
        stack = [start_matrix]

        while stack:
            matrix = stack.pop()
            visited.append(matrix)
            if np.array_equal(matrix, end_matrix):
                for node in visited:
                    print(node)
                return True
            else:
                children = possibleChildren(matrix, end_matrix)
                for child in children:
                    stack.append(child)
        print(len(visited))
        return False

    dfs(start_matrix, end_matrix)
    end = time.time()

    print(f"mid1 time = {mid1 - start}")
    print(f"mid2 time = {mid2 - start}")
    print(f"overall time = {end - start}")
    '''

def dfs():
    return '''
    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


    def all_shortest_path(graph, start, goal, all_paths):
        path= []
        path.append(start)
        dfs(graph, start, goal, path, all_paths)
        print("LIST OF ALL PATHS: ", all_paths)

        shortest_path = min(all_paths, key = lambda i: len(i))
        print("SHORTEST PATH: ", shortest_path)

    def dfs(graph, current, goal, path,all_paths):
        if current == goal:
            all_paths.append(path.copy())
            return all_paths
        else:
            for neighbor in graph[current]:
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(graph, neighbor, goal, path, all_paths)
                    path.pop(len(path)-1) 

    all_paths=[]
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")

    if ((start_node in graph) and (goal_node in graph)) :
        all_shortest_path(graph, start_node, goal_node, all_paths)
    else:
        print("ENTER THE CORRECT NODE!")

    '''

def bfs():
    return'''
    graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']
        }

    def bfs_shortest_path(graph, start, goal):
        visited = []
        queue = [[start]]
        if start == goal:
            return [start]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                neighbours = graph[node]
                for neighbour in neighbours:
                    new_path = list(path)
                    new_path.append(neighbour)
                    print("CURRENT PATH: ", new_path)
                    queue.append(new_path)
                    print("LIST: ", queue)
                    if neighbour == goal:
                        return new_path
                visited.append(node)
                print("VISITED LIST: ", visited)
        return "Path doesn't exist!"

    start_node = input('enter the start node: ')
    goal_node = input('enter the goal node: ')
    print("FINAL PATH: ", bfs_shortest_path(graph, start_node, goal_node))  

    '''

def waterjug():
    return'''
    from collections import deque

    def BFS(jug1, jug2, target):
        m = {}
        isSolvable = False
        path = []

        q = deque()
        q.append((0,0))

        while(len(q) > 0):
            # print("Q ", q)
            u = q.popleft()
            
            if((u[0],u[1]) in m): #Alreadyin visited
                continue

            if((u[0] > jug1 or u[1] > jug2 or u[0] < 0 or u[1] < 0)):
                continue

            path.append([u[0], u[1]])
            print("path ", path)
            m[(u[0], u[1])] = 1
            if (u[0] == target or u[1] == target):
                isSolvable = True

                if (u[0] == target):
                    if (u[1] != 0):
                        path.append([u[0], 0])
                else:
                    if (u[0] != 0):
                        path.append([0, u[1]])
        
                path_len = len(path)
                for i in range(path_len):
                    print(path[i][0], path[i][1])
                break

            q.append([u[0], jug2])
            q.append([jug1, u[1]])

            for amount in range((max(jug1, jug2)) + 1):
                a = u[0] + amount
                b = u[1] - amount

                if ((a == jug1)  or (b == 0 and b >= 0)):
                    q.append([a, b])

                a = u[0] - amount
                b = u[1] + amount

                if ((a == 0 and a >= 0) or (b == jug2)):
                    q.append([a, b])

            q.append([jug1, 0])
            q.append([0, jug2])

        if (not isSolvable):
                print("No solution")


    x = int(input("Enter the capacity of jug 1: "))
    y = int(input("Enter the capacity of jug 2: "))
    d = int(input("Enter the quantity you want: "))

    BFS(x, y, d)
    '''