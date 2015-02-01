sec, n = map(int, input().split()) # sec = section length
nums = tuple(int(input()) for i in range(n))
# to avoid out-of-range, subtract sec from n
# use slice to get sums of sec successive numbers
sums = tuple(sum(nums[i:i + sec]) for i in range(n - sec + 1))
print(max(sums))
