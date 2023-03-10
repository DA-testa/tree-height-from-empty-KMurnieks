# python3 #Kristaps Murnieks 221RDB173

import sys
import threading
import numpy

#The fun begind
def compute_height(n, parents):
    
    # Write this function
    
    finder = [[] for _ in range(n)]
    root = None
    
    # Your code here
    
    for g, parent in enumerate(parents):   #Seeing if parent == -1
        if parent == -1:
            root = g
           
        else:
            finder[parent].append(g)

    def max_height(Z):  #Defining things zzz
        height = 1
        
        if not finder[Z]:
            return height
        else:
            for child in finder[Z]:
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
    
        filepath = './test/'  #Setting up the filepath / file etc.
        file = input()
        folder = filepath + file
        
        if "a" not in file: # Checks if a is in the file or not.
            try:
                with open(folder) as x:
                    
                    n = int(x.readline())
                    parents = list(map(int, x.readline().split()))    #makes teh variable partents int othe list 
                    
            except Exception as ex:
                print("Error:(", str(ex))   # More error printers
                return
            
        else:
            print("Error") #Prints and error if it doesn't work
            return
        
    else:
        print("Input 'I' or 'F': ")    #Returns back to input
        return
            
    # call the function and output it's result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()




