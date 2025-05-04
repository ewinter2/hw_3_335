#!/usr/bin/env python3

import random

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result_array = []
    i = j = 0

    # Merge the two halves while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_array.append(left[i])
            i += 1
        else:
            result_array.append(right[j])
            j += 1

    # Append any remaining elements in the left or right half
    result_array.extend(left[i:])
    result_array.extend(right[j:])
    return result_array

# Quick Sort Implementation
def quick_sort(V, s=0, e=None):
    if e is None:
        e = len(V)
    if (e - s) >= 2:
        lte, eqe = inplace_partition(V, s, e)
        quick_sort(V, s, lte)
        quick_sort(V, eqe, e)
    return V

def inplace_partition(V, s, e):
    pivot = V[random.randint(s, e-1)]
    lte = s
    ges = e - 1
    while lte <= ges:
        if V[lte] < pivot:
            lte += 1
        elif V[ges] > pivot:
            ges -= 1
        else:
            V[lte], V[ges-1] = V[ges], V[lte]
            lte += 1
            ges -= 1
    '''
    eqe = ges
    for i in range(ges, e):
        if V[i] == pivot:
            V[eqe], V[i] = V[i], V[eqe]
            eqe += 1
    return lte, eqe'''
    return ges + 1, lte

# Main function to demonstrate sorting
def main():
    input_text = "SORTINGEXAMPLE"
    
    input_arr1 = list(input_text)
    sorted_arr1 = merge_sort(input_arr1)
    sorted_string1 = ''.join(sorted_arr1)
    print("Sorted string uisng merge sort :", sorted_string1)

    input_arr2 = list(input_text)
    sorted_arr2 = quick_sort(input_arr2)
    sorted_string2 = ''.join(sorted_arr2)
    print("Sorted string using quick sort :", sorted_string2)



if __name__ == "__main__":
    main()