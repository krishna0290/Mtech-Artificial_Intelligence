#include <stdio.h>

void merge(int A[], int low, int mid, int high)
{
    int i = low;
    int j = mid + 1;
    int k = 0;

    int temp[high - low + 1];

    while (i <= mid && j <= high)
    {
        if (A[i] <= A[j])
        {
            temp[k] = A[i];
            i++;
        }
        else
        {
            temp[k] = A[j];
            j++;
        }

        k++;
    }
    while (i <= mid)
    {
        temp[k] = A[i];
        i++;
        k++;
    }
    while (j <= high)
    {
        temp[k] = A[j];
        j++;
        k++;
    }

    for (i = low, k = 0; i <= high; i++, k++)
    {
        A[i] = temp[k];
    }
}

void mergeSort(int A[], int low, int high)
{
    if (low < high)
    {
        int mid = low + (high - low) / 2;
        mergeSort(A, low, mid);
        mergeSort(A, mid + 1, high);
        merge(A, low, mid, high);
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    int A[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &A[i]);
    }
    mergeSort(A, 0, n - 1);
    for (int i = 0; i < n; i++)
    {
        printf("%d ", A[i]);
    }
    return 0;
}