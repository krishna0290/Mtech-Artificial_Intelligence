#include<stdio.h>

void swap(int *a, int *b);
void heapify(int *A, int n, int i);

void heapsort(int A[], int n){
    for(int i=n/2 -1; i>=0; i--){
        heapify(A,n,i);
    }
     for (int i = n - 1; i > 0; i--)
    {
        swap(&A[0], &A[i]);
        heapify(A, i, 0);
    }
}
void heapify(int A[],int n,int i){
    int max = i;
    int l = 2*i+1;
    int r = (2*i)+2;
    if(l<n && A[l] > A[max]){
        max = l;
    }
    if(r<n && A[r] > A[max]){
        max = r;
    }
    if(max != i){
        swap(&A[max],&A[i]);
        heapify(A,n,max);
    }
}
void swap(int*a, int*b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main(){
    int n;
    scanf("%d", &n);
    int A[n];
    for(int i=0; i<n; i++){
        scanf("%d", &A[i]);
    }
    heapsort(A,n);
    for(int i=0; i<n; i++){
        printf("%d" , A[i]);
        printf("%s" , " ");
    }
    return 0;
}