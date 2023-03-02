# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    
    # Write this function
    
    finder = [[] for _ in range(n)]
    root = None
    #max_height = 0
    
    # Your code here
    
    for g, parent in enumerate(parents):
        if parent == -1:
            root = g
           
        else:
            finder[parent].append(g)

    def max_height(vuzol):
        height = 1
        
        if not finder[vuzol]:
            return height
        else:
            for child in finder[vuzol]:
                height = max(height, max_height(child))

            return height + 1
    return max_height(root)

def main():
    
    # implement input form keyboard and from files
    
    Input = input()
    if "I" in Input:
        
        # input number of elements
        
        n = int(input())
        
        # input values in one variable, separate with space, split these values in an array
        
        parents = list(map(int, input().split()))
    elif "F" in Input:

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision 
    
        path = './test/'  
        file = input()
        folder = path + file
        
        if "a" not in file:
            try:
                with open(folder) as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
            except Exception as e:
                print("Error:(", str(e))
                return
            
        else:
            print("Error")
            return
        
    else:
        print("Input 'I' or 'F': ")
        return
            
    # call the function and output it's result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()




