def sort_arr(arr:list)->list:

    n = len(arr)

    for elem in range(0, n-1):


         for j in range(elem+1, n):

            if arr[elem] > arr[j]:

                arr[elem], arr[j]= arr[j], arr[elem]

    return arr

def main():

    unsorted = [6,3,5,2,1,7,4]

    result = sort_arr(unsorted)

    print(f'sorted array: {result}')

    return 0

    



if __name__ == '__main__':

    main()

    
