#include <stdio.h>

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = low;
    int j = high - 1;

    while (i <= j)
    {
        while (i <= j && arr[i] <= pivot)
        {
            i++;
        }
        while (i <= j && arr[j] > pivot)
        {
            j--;
        }

        if (i < j)
        {
            swap(&arr[i], &arr[j]);
        }
    }

    swap(&arr[i], &arr[high]);

    return i;
}

void qs(int arr[], int low, int high)
{
    if (low < high)
    {
        int partIndex = partition(arr, low, high);

        qs(arr, low, partIndex - 1);
        qs(arr, partIndex + 1, high);
    }
}

void quickSort(int arr[], int n)
{
    qs(arr, 0, n - 1);
}

int main()
{
    int n;
    scanf("%d", &n);
    int arr[n];
    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    quickSort(arr, n);

    printf("Sorted array: ");

    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}