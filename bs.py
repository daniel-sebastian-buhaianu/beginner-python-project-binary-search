# implementation of binary search algorithm

def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0

    if high is None:
        high = len(list) - 1

    if high < low: # target not found
        return -1

    midpoint = (low + high) // 2
    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binary_search(list, target, low, midpoint-1)
    else:
        return binary_search(list, target, midpoint+1, high)  
    

def switch(ind, list):
    if ind == 1:
        return "st"
    elif ind == 2:
        return "nd"
    elif ind == 3:
        return "rd"
    elif ind == len(list):
        return "last"
    else:
        return "th"

    
if __name__ == "__main__":
    list = [1, 3, 5, 10, 12]
    target = 10
    target_index = binary_search(list, target) + 1
    target_index_text = switch(target_index, list)

    if target_index_text == "last":
        target_index = ""

    print(f"{target} is the {target_index}{target_index_text} element in the list")