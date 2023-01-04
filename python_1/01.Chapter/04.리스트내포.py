#리스트 내포
#for 사용
nums =  [ i for i in range(5)]
print(nums)
nums = [1000,100002,100523]

double_nums = [i*2 for i in nums]
print(double_nums)

#if 사용
nums = [i for i in range(10) if i%2 ==0]
print(nums)

nums = [1000,2000,3000,4000,5000]
double_nums = [i*2 for i in nums if i >= 3000]
print(double_nums)