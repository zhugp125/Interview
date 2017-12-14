#include <stdio.h>

void swap(int a[], int i, int j)
{
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

/**
 * @brief bubbleSort 冒泡排序
 * @param a 数据结构：数组
 * @param n 数组大小
 * 最好时间复杂度：O(n)
 * 最差时间复杂度：O(n^2)
 * 平均时间复杂度：O(n^2)
 * 稳定性：稳定
 */
void bubbleSort(int a[], int n)
{
    for(int i = 0; i < n - 1; ++i)
    {
        for(int j = 0; j < n - 1 - i; ++j)
        {
            if(a[j] > a[j + 1])  //如果条件为a[j] >= a[j + 1]，则为不稳定排序
            {
                swap(a, j, j + 1);
            }
        }
    }
}

/**
 * @brief cocktailSort 定向冒泡排序--鸡尾酒法排序
 * @param a 数据结构：数组
 * @param n 数组大小
 * 最好时间复杂度：O(n)
 * 最差时间复杂度：O(n^2)
 * 平均时间复杂度：O(n^2)
 * 稳定性：稳定
 */
void cocktailSort(int a[], int n)
{
    int left = 0;
    int right = n - 1;
    while(left < right)
    {
        //首先把最大的数据放在数组末尾
        for(int i = left; i < right; ++i)
        {
            if(a[i] > a[i + 1])
            {
                swap(a, i, i + 1);
            }
        }
        --right;
        //最后把最小的数据放在数组头部
        for(int i = right; i > left; --i)
        {
            if(a[i - 1] > a[i])
            {
                swap(a, i - 1, i);
            }
        }
        ++left;
    }
}

/**
 * @brief selectSort 选择排序
 * @param a 数组
 * @param n 数组大小
 * 最好时间复杂度：O(n^2)
 * 最差时间复杂度：O(n^2)
 * 平均时间复杂度：O(n^2)
 * 稳定性：不稳定
 */
void selectSort(int a[], int n)
{
    //外层n-1次循环，依次记录每次插入值的位置
    for(int i = 0; i < n - 1; ++i)
    {
        int min = i;
        //内层循环，查找本次循环内的最小值的下标
        for(int j = i + 1; j < n; ++j)
        {
            if(a[min] > a[j])
            {
                min = j;
            }
        }
        //如果当前插入值的下标不是最小值的下标，那么进行替换
        if(min != i)
        {
            swap(a, min, i);
        }
    }
}

/**
 * @brief insertSort 插入排序
 * @param a 数组
 * @param n 数组大小
 * 最好时间复杂度：O(n)
 * 最差时间复杂度：O(n^2)
 * 平均时间复杂度：O(n^2)
 * 稳定性：稳定
 */
void insertSort(int a[], int n)
{
    for(int i = 1; i < n; ++i)
    {
        int cur = a[i]; //记录当前比较的值
        int j = i - 1;
        while(j >= 0 && cur < a[j]) //找到第一个比当前值小的值
        {
            a[j + 1] = a[j]; //每次后移一个相邻元素
            --j;
        }
        a[j + 1] = cur; //将当前值插入到指定位置
    }
}

/**
 * @brief insertSortDichotomy 二分插入排序
 * @param a 数组
 * @param n 数组大小
 * 最好时间复杂度：O(nlogn)
 * 最差时间复杂度：O(n^2)
 * 平均时间复杂度：O(n^2)
 * 稳定性：稳定
 */
void insertSortDichotomy(int a[], int n)
{
    for(int i = 1; i < n; ++i)
    {
        int cur = a[i]; //记录当前需要比较的值
        //将当前需要比较的值与左侧已经排好序的列表使用二分法进行查找
        int left = 0;
        int right = i - 1;
        while(left <= right)
        {
            int mid = (left + right) / 2;
            if(a[mid] > cur)
                right = mid - 1;
            else
                left = mid + 1;
        }
        for(int j = i - 1; j >= left; --j)
        {
            a[j + 1] = a[j];
        }
        a[left] = cur;
    }
}

void display(int a[], int n)
{
    for(int i = 0; i < n; ++i)
    {
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main()
{
    int a[] = {5, 4, 6, 2, 4, 8, 9, 3};
    int n = sizeof(a) / sizeof(int);
    //bubbleSort(a, n);
    //cocktailSort(a, n);
    //selectSort(a, n);
    //insertSort(a, n);
    insertSortDichotomy(a, n);

    display(a, n);

    printf("Hello World!\n");
    return 0;
}
