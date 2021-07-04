import math
from numpy import random
from time import time
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
        
            
    right_sum = -99999999999
    sum_ = 0
    right = 0
    for i in range((mid + 1), (high + 1)):
        sum_ = sum_ + a[i]
        if(sum_ > right_sum):                                  
            right_sum = sum_
            right = i
        
            
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
    

    

def max_subarray(l):
    max_ = -9999999999
    low = 0
    high = 0
    for i in range(len(l)-1):
        s = l[i]
        for j in range ((i+1),len(l)):
            s = s + l[j]
            if(s > max_):
                max_ = s
                low = i
                high = j
    return low, high, max_

    

"""
a=[]
for i in range(30000):
    a.append(random.randint(-100,100))
x = time()           
print(max_subarray_greedy(a,0,len(a)-1))
print("dc",time() - x)

x = time() 
print(max_subarray(a))
print("ndc",time() - x)
#print(a)
"""

def merge (left, right):
    a=[]
    n=0
    l=0
    r=0
    flag = 0
    marker = []
    
    limit = len(left) + len(right)
    while(n < limit ):   
      if(left[l] <= right[r] ):          
          a.append(left[l])
          if(l+1 != len(left)):
              l+=1
          else:
              flag = right
              marker = r
              break
      else:
          a.append(right[r])
          if(r+1 != len(right)):
              r+=1
          else:
              flag = left
              marker = l
              break
    if(len(a) != limit):
        for i in range (marker, len(flag)):
            a.append(flag[marker])
            marker +=1
    return a
        
        
        
          
            
            
        
        


    
            
    
def merge_sort(a, low, high):
    if (low >= high):
        c = [a[low]]        
        return c
    else:
        mid = math.floor((low + high)/2)              
    return merge(merge_sort (a, low, mid), merge_sort (a, mid + 1, high))

a = [10,9,8,7,6,5,4,4,3,2,1,0,-1]     
 
print (merge_sort(a, 0, len(a)-1))
#print(merge([1,2,3,4,5], [6,7,8,9,10]))


