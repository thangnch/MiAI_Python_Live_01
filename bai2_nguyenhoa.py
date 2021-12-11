# Viết một chương trình thực hiện các thao tác sau đây: Sinh ra ngẫu nhiên một dãy gồm 20
# số nguyên trong khoảng [-10,10].
# (a) Tìm ra 3 số có giá trị tuyệt đối lớn nhất trong dãy.
# (b) Tìm dãy con gồm các số tăng liên tiếp có độ dài lớn nhất

import numpy
import random

# Dinh nghia tham so
N = 20
MIN = -10
MAX = 10

# Sinh ra 1 day 20 so nguyen
arr = numpy.random.randint(MIN,MAX + 1, N)
print("Day so la: ", arr)

# Tim 3 so co gia tri tuyet doi lon nhat
sorted_arr = sorted(abs(arr))
print("Ba so co gia tri tuyet doi lon nha la: ", sorted_arr[-3:])

# Tim day con tang lien tiep dai nhat
start = 0
end = 0
curr_length = 1

max_start = 0
max_end = 0
max_length = 1

for i in range(1, len(arr)):
    if arr[i] > arr[i-1]:
        curr_length = curr_length + 1
        end = i
    else:
        if curr_length > max_length:
            max_length = curr_length
            max_start = start
            max_end = end
        start = i
        curr_length = 1

print("Max length  = ", max_length)
print("Start = ", max_start)
print("End = ", max_end)

for i in range(max_start, max_end  + 1):
    print(arr[i])