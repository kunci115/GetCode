# -*- coding: utf-8 -*-

# 2 water jugs capacity -> (x,y) where x>y
# initial state (4,3)
# final state (2,0)

capacity = (4,3)
# Maximum capacities of 2 jugs -> x,y
x = capacity[0]
y = capacity[1]

# to mark visited states
memory = {}

# store solution path
ans = []

def get_all_states(state):
    # Let the 2 jugs be called a,b
    a = state[0]
    b = state[1]

    # if current state is already visited earlier
    if((a,b) in memory):
        return False

    memory[(a,b)] = 1
    
    if(b == 2 and a == 0):
        # rule 11
        ans.append(state)
        return True

    #empty jug a
    if(a>0):
        #empty a into b
        if(a+b<=y):
          # rule 10
            if( get_all_states((0,a+b)) ):
                ans.append(state)
                return True
        else:
            # rule 8
            if( get_all_states((a-(y-b), y)) ):
                ans.append(state)
                return True

    #empty jug b
    if(b>0):
        #empty b into a
        if(a+b<=x):
            # rule 9
            if( get_all_states((a+b, 0)) ):
                ans.append(state)
                return True
        else:
            # rule 7
            if( get_all_states((x, b-(x-a))) ):
                ans.append(state)
                return True
                
    if a > 0 and b == 2:
        get_all_states((0,b))
        ans.append(state)
        return True
        
    if b < y:
        # if a and b are empty
        # rule 2
        get_all_states((a,y))
        ans.append(state)
        return True
            
    return False

initial_state = (0,0)
print("Starting work...\n")
get_all_states(initial_state)
ans.reverse()

# append the last move
state = (2,0)
ans.append(state)
        
for i in ans:
  print(i)
