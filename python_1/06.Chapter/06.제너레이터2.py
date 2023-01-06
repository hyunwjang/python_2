#제너레이터 표현식

double_generater = (i*2 for i in range(1,10))

for i in double_generater:
    print(i)

#3. 메모리 사용을 효율적으로 하기위해서 사용
# ex) 숫자 1 - 100000 3배로 만든 결과 리스트 vs 제너레이터

import sys

list_data = [i*3 for i in range(1, 10000 +1)]
generate_data = (i*3 for i in range(1, 10000 +1))

print(sys.getsizeof(list_data))
print(sys.getsizeof(generate_data))