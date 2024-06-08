heap = [0 for i in range(101)]  # our heap to be used
curr_size = len(heap)

def parent(i):
    # i is the index of the child node
    # i = 2p + 1 or i = 2p + 2 where p is the index of the parent node
    # p = (i - 1)/2 or p = (i - 2) / 2
    p = (i - 1) / 2

    if i % 2 == 0:
        p = (i - 2) / 2

    return int(p)


# auxiliar functon to heapify an unbalanced heap
def heapify(i):
    global curr_size
    current_index = i

    while current_index < curr_size:
        left_index = 2*current_index + 1
        right_index = 2*current_index + 2

        lowest = current_index

        if (left_index < curr_size) and (heap[left_index] < heap[lowest]):
            lowest = left_index

        if (right_index < curr_size) and (heap[right_index] < heap[lowest]):
            lowest = right_index
        # Heap property is followed, so we don't have anything more to do
        if lowest == current_index:
            break
        # Heap property was broken, then we have to swap items
        temp = heap[current_index]
        heap[current_index] = heap[lowest]
        heap[lowest] = temp

        current_index = lowest


def heapify_from_bottom_to_top(i):
    current_index = i

    # Checking heap property from i to the top and swapping items that break the property if needed
    while current_index > 0:
        parent_index = parent(current_index)

        if heap[parent_index] > heap[current_index]:
            temp = heap[parent_index]
            heap[parent_index] = heap[current_index]
            heap[current_index] = temp

            current_index = parent_index
            continue

        break


def remove_last_item():
    global curr_size
    # Removes the last element from the heap = set it to 0
    heap[curr_size - 1] = 0
    curr_size -= 1


#Function to insert a value in Heap.
def insertKey(x):
    global curr_size
    heap[curr_size] = x
    heapify_from_bottom_to_top(curr_size)
    curr_size += 1


#Function to extract minimum value in heap and then to store
#next minimum value at first index.
def extractMin():
    global curr_size
    if curr_size == 0:
        return -1

    if curr_size == 1:
        min_item = heap[0]
        remove_last_item()
        return min_item

    min_item = heap[0]
    heap[0] = heap[curr_size - 1]
    remove_last_item()

    heapify(0)

    return min_item


#Function to delete a key at ith index.
def deleteKey(i):
    global curr_size
    # The specified item is not on the heap
    if i >= curr_size:
        return

    # Putting an item with value lower than the possible values at position i
    heap[i] = -1
    heapify_from_bottom_to_top(i)
    # Here the -1 value is at the top and needs to be removed
    extractMin()