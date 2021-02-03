
def partition(elements, start, end):
    pivot = elements[start]
    left = start + 1
    right = end

    while True:

        while left <= right and elements[left] <= pivot:
            left += 1
        while left <= right and elements[right] >= pivot:
            right -= 1

        if left <= right:
            elements[left], elements[right] = elements[right], elements[left]
        else:
            break
    elements[start], elements[right] = elements[right], elements[start]
    return right


def quick_sort(elements, start, end):
    if start >= end:
        return

    partition_index = partition(elements, start, end)
    quick_sort(elements, start, partition_index-1)  # sort left subarray
    quick_sort(elements, partition_index+1, end)  # sort right subarray


def display_elements(elements):
    for i in elements:
        print(i, end=" ")
    print("")


def main():
    elements = [87, 65, 34, 23, 12, 9]
    quick_sort(elements, 0, len(elements)-1)
    display_elements(elements)


if __name__ == "__main__":
    main()