from collections import deque

def sliding_window_maximum(nums, k):
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  

    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

print("Test Case 1:")
print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

print("\nTest Case 2:")
print(sliding_window_maximum([4, 2, 12, 3], 1))


print("\nTest Case 3:")
print(sliding_window_maximum([5, 5, 5, 5, 5], 2))

