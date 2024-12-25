class SelectionSort:
    def select(self, arr):
        for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

def main():
    n = int(input("Enter the number of elements: "))
    arr = list(map(int, input("Enter the elements separated by space: ").split()))

    c = SelectionSort()
    s = c.select(arr)

    print("Sorted array:", s)

if __name__ == "__main__":
    main()
