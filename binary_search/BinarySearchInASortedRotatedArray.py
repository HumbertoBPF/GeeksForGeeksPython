def Search(arr,n,k):
    # Trivial case
    if n == 1:
        return 0

    lower_bound = 0
    upper_bound = n - 1
    # Checking the upper and lower bounds before starting binary search
    if arr[lower_bound] == k:
        return lower_bound

    if arr[upper_bound] == k:
        return upper_bound

    while upper_bound - lower_bound > 1:
        mid = (lower_bound + upper_bound) // 2

        if arr[mid] == k:
            return mid
        # If the item at mid is greater than the one at the lower bound, all the elements in [lower_bound, mid] are in
        # the range [arr[lower_bound], arr[mid]]
        if arr[mid] > arr[lower_bound]:
            # If k is in [arr[lower_bound], arr[mid]], we have to continue the search in [lower_bound, mid]
            if arr[lower_bound] <= k <= arr[mid]:
                upper_bound = mid
                continue

            lower_bound = mid
            continue
        # If the item at mid is lower than the one at the upper bound, all the elements in [mid, upper_bound] are in
        # the range [arr[mid], arr[upper_bound]]

        # If k is in [arr[mid], arr[upper_bound]], we have to continue the search in [mid, upper_bound]
        if arr[mid] <= k <= arr[upper_bound]:
            lower_bound = mid
            continue

        upper_bound = mid

    return -1
