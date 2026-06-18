def two_sum(nums,target):
    d={}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]],i]
        d[nums[i]]=i
n=int(input())
a=list(map(int,input().split()))
target=int(input())
print(two_sum(a,target))
