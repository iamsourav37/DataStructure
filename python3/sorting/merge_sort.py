

def merge_sort(elements):
    if len(elements) > 1:
        mid = len(elements) // 2
        left_list = elements[:mid]
        right_list = elements[mid:]
        merge_sort(left_list)
        merge_sort(right_list)

        # merge

        i = 0
        j = 0
        k = 0

        while i < len(left_list) and j < len(right_list):

            if left_list[i] < right_list[j]:
                elements[k] = left_list[i]
                i += 1
                k += 1
            else:
                elements[k] = right_list[j]
                j += 1
                k += 1
        while i < len(left_list):
            elements[k] = left_list[i]
            i += 1
            k += 1
        while j < len(right_list):
            elements[k] = right_list[j]
            j += 1
            k += 1


def display_elements(elements):
    for i in elements:
        print(i, end=" ")
    print("")


def main():
    elements = [20, 12, 8, 10, 29, 7, 32, 23]
    merge_sort(elements)
    display_elements(elements)


if __name__ == "__main__":
    main()
