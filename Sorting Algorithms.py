import math
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

def max_subarray(l):
    for i in range(len(l)-1):
        s =str(l[i])
        for j in range ((i+1),len(l)):
            s = s + " "+str(l[j])
            print(s)
         
a=[2,1,3,4,5,6,7] 
#a = max_subarray(a)  
#print(a)

def max_crossing_subarray(a,low,high,mid):
    left_sum = -99999999999
    sum_ = 0
    left = 0
    for i in range(mid, low - 1, -1):
        sum_ = sum_ + a[i]
        if(sum_ > left_sum):                                
            left_sum = sum_
            left = i
        else:
            break
            
    right_sum = -99999999999
    sum_ = 0
    right = 0
    for i in range((mid + 1), (high + 1)):
        sum_ = sum_ + a[i]
        if(sum_ > right_sum):                                  
            right_sum = sum_
            right = i
        else:
            break
            
    return left,right, (left_sum + right_sum)
    

def max_subarray_greedy (a, low, high):
    if(low == high):
        return low,high,a[0]
    else:
        
        mid = math.floor((low + high)/2)
        
        left_low, left_high, left_sum    =  max_subarray_greedy(a, low, mid)
        right_low, right_high, right_sum =  max_subarray_greedy(a, mid+1, high)
        cross_low, cross_high, cross_sum =  max_crossing_subarray(a, low, high, mid)
        
        if(left_sum >= right_sum and left_sum > cross_sum):
            return (left_low, left_high, left_sum)
        elif(right_sum >= left_sum and right_sum > cross_sum):
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
    

a=[1,2,3,4]           
print(max_subarray_greedy(a,0,len(a)-1)       )
    

    
    










