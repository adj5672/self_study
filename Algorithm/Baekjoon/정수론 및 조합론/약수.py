N = int(input())
nums = list(map(int, input().split()))
nums.sort()

def gcd(a, b):
    return a if not b else gcd(b, a % b)

lcm = 1
for i in range(N):
    c_gcd = gcd(lcm, nums[i])
    lcm = lcm * nums[i] / c_gcd
if lcm not in nums:
    print(int(lcm))
else:
    print(int(lcm * nums[0]))