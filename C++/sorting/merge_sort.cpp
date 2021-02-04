#include <iostream>
using namespace std;

void display_elements(int *a, int len)
{
    for (int i = 0; i < len; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

// int count_length(int *a){
//     int count = 0;
//     for (int i = 0; a[i] != '\0'; i++)
//     {
//         count++;
//     }
//     return count;

// }

void merge_sort(int *arr, int len)
{ // 12 8 20 7 10

    if (len > 1)
    {
        int size_of_left_array = len / 2;                   // 1
        int size_of_right_array = len - size_of_left_array; // 1
        int left_array[size_of_left_array];
        for (int i = 0; i < size_of_left_array; i++)
        {
            left_array[i] = arr[i];
        }
        int right_array[size_of_right_array];
        for (int i = 0; i < size_of_right_array; i++)
        {
            right_array[i] = arr[size_of_left_array + i];
        }

        merge_sort(left_array, size_of_left_array);
        merge_sort(right_array, size_of_right_array);

        // now merge two sub array in ascending order

        int i = 0;
        int j = 0;
        int k = 0;

        while (i < size_of_left_array && j < size_of_right_array)
        {

            if (left_array[i] < right_array[j])
            {
                arr[k] = left_array[i];
                k++;
                i++;
            }
            else
            {
                arr[k] = right_array[j];
                k++;
                j++;
            }
        }

        while (i < size_of_left_array)
        {
            arr[k] = left_array[i];
            k++;
            i++;
        }
        while (j < size_of_right_array)
        {
            arr[k] = right_array[j];
            k++;
            j++;
        }
    }
}

int main()
{

    int a[] = {90,50,30,20,19,16,15,10,3,2};
    int len = 10;
    merge_sort(a, len);
    display_elements(a, len);

    return 0;
}