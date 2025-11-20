import random, time

number_range=list(range(100))
s1=random.choices(number_range, k=50)
s2=random.choices(number_range, k=5000)
s3=random.choices(number_range, k=50000)
s4=random.choices(number_range, k=500000)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
    
def bubble_sort(arr):
    n=len(arr)
    for i in range(len(arr)):
        swap=False

        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap=True
        if(swap==False):
            break
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid=len(arr)//2
    arr_1=arr[:mid]
    arr_2=arr[mid:]

    arr_1=merge_sort(arr_1)
    arr_2=merge_sort(arr_2)

    return merge(arr_1, arr_2)

def merge(arr_a,arr_b):
    arr_c=[]

    while arr_a and arr_b:
        if(arr_a[0]>arr_b[0]):
            arr_c.append(arr_b[0])
            arr_b.pop(0)
        else:
            arr_c.append(arr_a[0])
            arr_a.pop(0)

    while arr_a:
        arr_c.append(arr_a[0])
        arr_a.pop(0)
    while arr_b:
        arr_c.append(arr_b[0])
        arr_b.pop(0)

    return arr_c
        
    
def quick_sort(arr,low,high):
    if(low<high):
        pivot_location=partition(arr,low,high)
        
        quick_sort(arr,low,pivot_location-1)
        quick_sort(arr,pivot_location+1,high)
    return arr
    
def partition(arr,low,high):
    pivot=arr[high]

    i=low-1

    for j in range(low,high):
        if(arr[j]<pivot):
            i+=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def timing(val, s):
    s_copy=s[:]
    start = time.time()
    if(val==1):
        arr=insertion_sort(s_copy)
        algo_text="Insertion sort"
    elif(val==2):
        arr=bubble_sort(s_copy)
        algo_text="Bubble sort"
    elif(val==3):
        arr=merge_sort(s_copy)
        algo_text="Merge sort"
    elif(val==4):
        quick_sort(s_copy,0,len(s_copy)-1)
        arr=s_copy
        algo_text="Quick sort"
    end = time.time()
    print(algo_text,"Time taken:", end - start, "seconds","for",len(s),"elements")
    
def main():
    #For 50 elements
    timing(1,s1),timing(2,s1),timing(3,s1),timing(4,s1)
    #For 5000 elements
    print("")
    timing(1,s2),timing(2,s2),timing(3,s2),timing(4,s2)
    #For 50000 elements
    print("")
    timing(1,s3),timing(2,s3),timing(3,s3),timing(4,s3)
    #For 500000 elements
    print("")
    timing(1,s4),timing(2,s4),timing(3,s4),timing(4,s4)

if __name__ == '__main__':
    main()
