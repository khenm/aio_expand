class Sorting:
    def bubble_sort(self, input: list[int], reverse: bool = False) -> list[int]:
        """Sort the list by bubble sort algorithm. 
        If there are swapped elements in the array. 
        Args:
            input (list[int]): _description_

        Returns:
            list[int]: _description_
        """
        n: int = len(input)
        for i in range(n - 1):
            swapped: bool = False
            for j in range(0, n - i - 1):
                if input[j] > input[j + 1]:
                    swapped = True
                    input[j], input[j + 1] = input[j + 1], input[j]
            if not swapped:
                return input if reverse else input[::-1] 

def main():
    arr: list[int] = [2, 3, 1, 4, 5, 8, 7, 9]
    print(f"Original array: {arr}")
    sort = Sorting()
    sort.bubble_sort(arr, reverse = True)
    print(f"Sorted array: {arr}")
    
if __name__ == '__main__':
    main()