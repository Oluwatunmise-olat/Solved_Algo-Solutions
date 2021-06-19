# Selection sort

# O(n**2), omega(n**2)

def sort_arr(arr:list)->list:

    n = len(arr)

    smallest = 0

    for element in range(0, n):

        smallest = arr[element]

        for j in range(element+1, n):

            if arr[j] < smallest:

                smallest = arr[j]

                arr[j], arr[element] = arr[element], smallest

    return arr

def main():

    unsorted = [5,7,3,1,6,4,2]

    res = sort_arr(unsorted)

    print(res)

    return 0

if __name__ == '__main__':

    main()
