from django.shortcuts import render
from django.core.exceptions import BadRequest


def partition(l: int, r: int, arr: list) -> int:
    pivot, swap_ind = arr[r], l
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[i], arr[swap_ind] = arr[swap_ind], arr[i]
            swap_ind += 1
    arr[swap_ind], arr[r] = arr[r], arr[swap_ind]
    return swap_ind

def quick_sort(l: int, r: int, arr: list) -> None:
    if len(arr) > 1 and l < r:
        pivot = partition(l, r, arr)
        quick_sort(l, pivot - 1, arr)
        quick_sort(pivot + 1, r, arr)


def index(request):
    array = request.GET.get('array', None)

    if array is None:
        raise BadRequest("'array' parameter is required")
    
    nums = []
    for sym in array.split(','):
        try:
            formatted_sym = int(sym)
        except Exception:
            formatted_sym = sym
        nums.append(str(formatted_sym))

    quick_sort(0, len(nums) - 1, nums)

    return render(request, "sort.html", {
        'input': array,
        'output': nums,
    })
