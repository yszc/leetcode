nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
print(tuple(zip(*map(sorted,nums))))

print(sum(map(max, zip(*map(sorted,nums)))))