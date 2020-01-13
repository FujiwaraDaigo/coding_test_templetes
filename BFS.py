def Maze_Breadth(Maze,start_goal):
    
    h=len(Maze)
    w=len(Maze[0])
    #ここに距離も格納
    footprints=[[-1 for i in range(w)] for j in range(h)]

    que=[start_goal[0]]

    distance=0
    while True:
        Que=[]

        for pos in que:
            
            footprints[pos[0]][pos[1]]=distance

            if pos[0]==start_goal[1][0] and pos[1]==start_goal[1][1]:
                
                break

            if not pos[0]==0:
                if Maze[pos[0]-1][pos[1]]=="." and footprints[pos[0]-1][pos[1]]==-1:
                    Que.append([pos[0]-1,pos[1]])
            
            if not pos[0]==h-1:
                if Maze[pos[0]+1][pos[1]]=="." and footprints[pos[0]+1][pos[1]]==-1:
                    Que.append([pos[0]+1,pos[1]])

            if not pos[1]==0:
                if Maze[pos[0]][pos[1]-1]=="." and footprints[pos[0]][pos[1]-1]==-1:
                    Que.append([pos[0],pos[1]-1])
            
            if not pos[1]==w-1:
                if Maze[pos[0]][pos[1]+1]=="." and footprints[pos[0]][pos[1]+1]==-1:
                    Que.append([pos[0],pos[1]+1])
        que=Que
        distance+=1

        if len(Que)==0:
            break
    return footprints[start_goal[1][0]][start_goal[1][1]]

print("message:input the size of maze matrix,H*W")

N,M=input().split(" ")

N=int(N)
M=int(M)

H,W=N,M

Ss=[]

print("message:input maze matrix, as \".\" or \"#\" ")


for i in range(H):
    S=input()
    Ss.append([S[i] for i in range(len(S))])

print("message:input the start and goal cell (i,j)")


start=input().split(",")
goal=input().split(",")

start=[int(s) for s in start]
goal=[int(s) for s in goal]

start_goal=[start,goal]

print()

print("distance:",Maze_Breadth(Ss,start_goal))