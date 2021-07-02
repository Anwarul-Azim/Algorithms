def insertion_sort (l):    
    for i in range(1, len(l)):
        key = l[i]
        j = i-1
        while(j>=0 and l[j]>key):
            l[j+1] = l[j]
            j -= 1
        l[j+1] = key
    return l                

def selection_sort(l):    
    for i in range (len(l)):  
        min_ = i
        for j in range (i,len(l)):            
            if(l[j] < l[i]):
                min_ = j 
    
        print("before",i,l)
        temp = l[min_]
        l[min_] = l[i]
        l[i] = temp
        print("after ",i,l)
        print()
    return l

def bubble_sort(l):
    for i in range(len(l)):
        swap = False
        for j in range (len(l)-1):            
            if(l[j] > l[j+1]):
                swap = True
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp
        if(swap == False):
            break
    return l

            
a=[2,1,3,4,5,6] 
a = bubble_sort(a)  
print(a)