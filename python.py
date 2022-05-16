1.Tổng liên tiếp
# n = a + (a + 1) + ... + (a + l)
# n = a * (l + 1) + (1 + 2 + ... + l)
# n = a * (l + 1) + l * (l + 1) / 2
# a = [n - (l * (l + 1) / 2)] / (l + 1)
t = int(input())
while t > 0:
    n = int(input())
    l = 1; res = 0
    tmp = l * (l + 1)
    while(tmp < 2 * n):
        a = (1.0 * n - tmp / 2) / (l + 1)
        if(a - int(a) == 0.0): res += 1
        l += 1
        tmp = l * (l + 1)
    print(res)
    t -= 1

2.Tách đôi và tính tổng
n = int(input())
while(n > 9):
    s = str(n)
    n = int(s[0:int(len(s) / 2)]) + int(s[int(len(s) / 2):len(s)])
    print(n)

3.Số thuận nghịch
from collections import deque

def convertTo10(s):
    val = 0
    for i in range(len(s)):
        val += (ord(s[i]) - 48) * pow(2, i)
    return val

a = [int (a) for a in input().split()]
if a[2] > 3:
    if a[0] == 0 and a[1] == 0: print(1)
    elif a[0] == 0 and a[1] > 0: print(2)
    elif a[0] == 1: print(1)
    else: print(0)
elif a[2] == 3:
    res = 0
    if(a[0] == 0): res += 1
    if(a[1] >= 1 and a[0] <= 1): res += 1
    if(a[0] <= 6643 and a[1] >= 6643): res += 1
    if (a[0] <= 1422773 and a[1] >= 1422773): res += 1
    print(res)
else:
    res = 0
    if(a[0] == 0): res += 1
    q = deque()
    q.append("1")
    while(True):
        s = q.popleft()
        val = convertTo10(s)
        if(val >= a[0] and val <= a[1]): res+= 1
        elif val > a[1]: break
        tmp = "";
        if(len(s) % 2 == 1):
            for i in range(int(len(s) / 2)): tmp += s[i]
            tmp += s[int(len(s) / 2)];
            for i in range(int(len(s) / 2), len(s)): tmp += s[i]
            q.append(tmp)
        else:
            for i in range(int(len(s) / 2)): tmp += s[i]
            tmp += '0';
            for i in range(int(len(s) / 2), len(s)): tmp += s[i]
            q.append(tmp)
            tmp = ""
            for i in range(int(len(s) / 2)): tmp += s[i]
            tmp += '1';
            for i in range(int(len(s) / 2), len(s)): tmp += s[i]
            q.append(tmp)
    print(res)

 4.Mã hóa 3
 c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
t = int(input())
while t > 0:
    s = input()
    sl = ""; sr = ""
    for i in range(int(len(s) / 2)): sl += s[i]
    for i in range(int(len(s) / 2), len(s), 1): sr += s[i]
    valueRotateLeft = 0
    valueRotateRight = 0
    for i in sl: valueRotateLeft += ord(i) - 65
    for i in sr: valueRotateRight += ord(i) - 65
    tmp = ""
    for i in sl:
        if (ord(i) + valueRotateLeft > 90):
            tmp += c[((ord(i) + valueRotateLeft) - 91 ) % 26]
        else:
            tmp += c[ord(i) + valueRotateLeft - 65]
    sl = tmp
    tmp = ""
    for i in sr:
        if (ord(i) + valueRotateRight > 90):
            tmp += c[((ord(i) + valueRotateRight) - 91) % 26]
        else:
            tmp += c[ord(i) + valueRotateRight - 65]
    sr = tmp
    for i in range(len(sl)):
        value = ord(sr[i]) - 65
        if (ord(sl[i]) + value > 90):
            print(c[((ord(sl[i]) + value) - 91) % 26], end = "")
        else:
            print(c[ord(sl[i]) + value - 65], end = "")
    print()
    t -= 1

 5.Tách số và sắp xếp
 n = int(input())
a = []
for i in range(n):
    s = input()
    i = 0
    while i < len(s):
        if(s[i].isdigit()):
            val = ord(s[i]) - 48
            while(i < len(s) - 1):
                i += 1
                if(s[i].isdigit()): val = val * 10 + ord(s[i]) - 48
                else:
                    a.append(val)
                    break
            if (i == len(s) - 1 and s[i].isdigit()): a.append(val)
        i += 1
a.sort()
for i in a: print(i)

6.Đổi các chữ số
t = int(input())
while t > 0:
    s = input()
    a = []
    state = 0
    for i in s: a.append(i)
    for i in range(len(a) -1, 0, -1):
        if(a[i] < a[i - 1]):
            limit = a[i - 1]
            max = a[i]
            inDex = i
            state = 1
            for j in range(i, len(a)):
                if(a[j] < limit and a[j] > max):
                    max = a[j]
                    inDex = j
            tg = a[i - 1]
            a[i - 1] = a[inDex]
            a[inDex] = tg
            break
    if(a[0] == '0' or state == 0):print(-1)
    else:
        for i in a: print(i, end = "")
        print()
    t -= 1

 7.Ước số của gia thừa
 t = int(input())
while t > 0:
    a = input().split()
    n = int(a[0])
    k = int(a[1])
    res = 0
    while(n / k > 0):
        tmp = int(n / k)
        res += tmp
        n = tmp
    print(res)
    t -= 1

 8.Thống kê từ khác nhau ko chứa chữ số
import re

def cmpValue(x):
    return -x[1]

def isDigit(x):
    if(x >= '0' and x <='9'): return True
    return False

n = int(input())
words = []
d = dict()
while n >0:
    s = re.findall(r"[\w']+", input().lower())
    for i in s:
        word = ""
        for j in i:
            if(isDigit(j) == False): word += j
        if(len(word) != 0): words.append(word)
    n -= 1
for word in words:
    if word in d: d[word] = d[word] + 1
    else: d[word] = 1
res = []
for i in d: res.append([i, d[i]])
res.sort()
res.sort(key = cmpValue)
for i in range(len(res)):
    print(res[i][0], res[i][1])   

9.Thống kê từ khác nhau theo ngưỡng k
import re

def cmpValue(x):
    return -x[1]

s = input().split()
n = int(s[0]); k = int(s[1])
words = []
d = dict()
while n >0:
    s = re.findall(r"[\w']+", input().lower())
    for i in s: words.append(i)
    n -= 1
for word in words:
    if word in d: d[word] = d[word] + 1
    else: d[word] = 1
res = []
for i in d: res.append([i, d[i]])
res.sort()
res.sort(key = cmpValue)
for i in range(len(res)):
    if(res[i][1] >= k): print(res[i][0], res[i][1])    

 10.Thống kê từ khác nhau
 import re

def cmpValue(x):
    return -x[1]

n = int(input())
words = []
d = dict()
while n >0:
    s = re.findall(r"[\w']+", input().lower())
    for i in s: words.append(i)
    n -= 1
for word in words:
    if word in d: d[word] = d[word] + 1
    else: d[word] = 1
res = []
for i in d: res.append([i, d[i]])
res.sort()
res.sort(key = cmpValue)
for i in range(len(res)):
    print(res[i][0], res[i][1])

11.Đếm số trong xâu
def check(i, s, n):
    for j in range(len(n)):
        if(s[i + j] != n[j]): return False
    return True

t = int(input())
while t > 0:
    s = input()
    n = input()
    res = 0
    i = 0
    while (i <= len(s) - len(n)):
        if(check(i, s, n)):
            res += 1
            i += len(n)
        else: i += 1
    print(res)
    t -= 1

 12.Số may mắn trong ma trận
 s = input().split()
n = int(s[0]); m = int(s[1])
mat = []
for i in range(n):
    a = [int (a) for a in input().split()]
    mat.append(a)
res = []; max = 0; min = 10005
for i in range(n):
    for j in range(m):
        if(min > mat[i][j]): min = mat[i][j]
        if(max < mat[i][j]): max = mat[i][j]
dist = max - min
for i in range(n):
    for j in range(m):
        if(mat[i][j] == dist):
            res.append(i)
            res.append(j)
if(len(res) != 0):
    print(dist)
    for i in range(0, len(res) - 1, 2):
        print('Vi tri [' , res[i], '][', res[i + 1], ']', sep = "")
else: print('NOT FOUND')     

13.Só thuận nghịch lớn nhất trong ma trận
def isReversible(num):
    if(len(num) < 2): return False
    l = 0; r = len(num) - 1
    while(l < r):
        if(num[l] != num[r]): return False
        l += 1; r -= 1
    return True

s = input().split()
n = int(s[0]); m = int(s[1])
mat = []
for i in range(n):
    a = [int (a) for a in input().split()]
    mat.append(a)
res = []; max = 0
for i in range(n):
    for j in range(m):
        if(mat[i][j] > max and isReversible(str(mat[i][j]))):
            max = mat[i][j]
            res.clear()
            res.append(i)
            res.append(j)
        elif(mat[i][j] == max):
            res.append(i)
            res.append(j)
if(max != 0):
    print(max)
    for i in range(0, len(res) - 1, 2):
        print('Vi tri [' , res[i], '][', res[i + 1], ']', sep = "")
else: print('NOT FOUND')

14.Số nguyên tố lớn nhất trong ma trận
isprime = [0, 0]
def createPrimeNumber():
    for i in range(2, 1000): isprime.append(1)
    for i in range(2, 32):
        if isprime[i] == 1:
            for j in range(i * i, 1000, i):
                isprime[j] = 0

s = input().split()
n = int(s[0]); m = int(s[1])
mat = []
createPrimeNumber()
for i in range(n):
    a = [int (a) for a in input().split()]
    mat.append(a)
res = []; max = 0
for i in range(n):
    for j in range(m):
        if(mat[i][j] > max and isprime[mat[i][j]] == 1):
            max = mat[i][j]
            res.clear()
            res.append(i)
            res.append(j)
        elif(mat[i][j] == max):
            res.append(i)
            res.append(j)
if(max != 0):
    print(max)
    for i in range(0, len(res) - 1, 2):
        print('Vi tri [' , res[i], '][', res[i + 1], ']', sep = "")
else: print('NOT FOUND')

15.Biến đổi về ma trận vuông
s = input().split()
n = int(s[0]); m = int(s[1])
mat = []
for i in range(n):
    a = [int (a) for a in input().split()]
    mat.append(a)
if(n >= m):
    for i in range(1, (n - m) * 2, 2):
        for j in mat[i]:
            print(j, end = " ")
        print()
    for i in range((n - m) * 2, n):
        for j in mat[i]:
            print(j, end = " ")
        print()
else:
    for i in range(n):
        for j in range(0, (m - n) * 2, 2):
            print(mat[i][j], end = " ")
        for j in range((m - n) * 2, len(mat[i])):
            print(mat[i][j], end = " ")
        print()

 16.Tính cân đối của ma trận
 n = int(input())
m = []
sumTop = 0; sumBot = 0
for i in range(n):
    a = [int (a) for a in input().split()]
    m.append(a)
for i in range(n):
    for j in range(n):
        if(j > i): sumTop += m[i][j]
        elif(j < i): sumBot += m[i][j]
k = int(input())
dist = abs(sumTop - sumBot)
if(dist <= k): print('YES')
else: print('NO')
print(dist)

17.Ngưỡng tối thiểu
s = input()
k = int(input())
a = []
used = []
for i in range(100): used.append(0)
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i] + s[i + 1])
    if(used[tmp] == 0):
        used[tmp] = 1
        a.append(tmp)
    else:
        used[tmp] += 1
state = 0
a.sort()
for i in a:
    if(used[i] >= k):
        print(i, used[i])
        state = 1
if state == 0: print('NOT FOUND')

18.Đếm số có 2 chữ số
s = input()
a = []
used = []
for i in range(100): used.append(0)
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i] + s[i + 1])
    if(used[tmp] == 0):
        used[tmp] = 1
        a.append(tmp)
    else: used[tmp] += 1
for i in a:
    print(i, used[i])

19.Liệt kê số có 2 chữ số theo thứ tự xuất hiện
s = input()
a = []
used = []
for i in range(100): used.append(0)
for i in range(0, len(s) - 1, 2):
    tmp = int(s[i] + s[i + 1])
    if(used[tmp] == 0):
        used[tmp] = 1
        a.append(tmp)
for i in a:
    print(i, end = " ")

 20.Liệt kê số có 2 chữ số tăng dần
 s = input()
a = []
for i in range(0, len(s) - 1, 2):
    a.append(int(s[i] + s[i + 1]))
a.sort()
for i in range(1, len(a)):
    if(a[i] != a[i - 1]): print(a[i - 1], end = " ")
print(a[len(a) - 1])

21.Phân chia nguyên tố
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

n = int(input())
used = []
b = []
s = 0
for i in range(1000): used.append(0)
a = [int (a) for a in input().split()]
for i in a:
    if(used[i] == 0):
        b.append(i)
        used[i] = 1
        s += i
sumLeft = 0; inDex = -1
for i in range(len(b)):
    sumLeft += b[i]
    if(isPrime(sumLeft) and isPrime(s - sumLeft)):
        inDex = i
        break
if(inDex != -1): print(inDex)
else: print('NOT FOUND')

22.Bầu cử
s = input().split()
n = int(s[0]); m = int(s[1])
a = [int (a) for a in input().split()]
used = []
cnt = -1
for i in range(m + 1): used.append(0)
for i in a:
    used[i] += 1
    if used[i] == 1: cnt += 1
reused = []
for i in used: reused.append(i)
reused.sort()
if(reused[len(reused) - 1] == reused[m - cnt]): print('NONE')
else:
    max = 0
    for i in range(len(reused) - 2, -1, -1):
        if(reused[i] != reused[len(reused) - 1]):
            max = reused[i]
            break
    for i in range(m + 1):
        if used[i] == max:
            print(i)
            break
23.Sắp xếp ngto
 n = int(input())
a = [int (a) for a in input().split()]
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
     101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
     197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307,
     311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
     431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547,
     557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659,
     661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
     809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929,
     937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
isPrime = []
prime = []
for i in range(1000): isPrime.append(0)
for i in range(len(P)): isPrime[P[i]] = 1
for i in a:
    if(isPrime[i] == 1): prime.append(i)
prime.sort()
inDex = 0
for i in a:
    if(isPrime[i] == 1):
        print(prime[inDex], end = " ")
        inDex += 1
    else: print(i, end = " ")

24.Biến đổi về dãy bằng nhau
n = int(input())
a = [int (a) for a in input().split()]
minCnt = 10000000; val = a[0]
for i in range(0, len(a)):
    cnt = 0
    for j in range (0, len(a)):
        cnt += abs(a[j] - a[i])
    if(cnt < minCnt):
        minCnt = cnt
        val = a[i]
print(minCnt, val)

25.Biến đổi nguyên tố
isprime = [0, 0]
def createPrimeNumber():
    for i in range(2, 10000): isprime.append(1)
    for i in range(2, 100):
        if isprime[i] == 1:
            for j in range(i * i, 10000, i):
                isprime[j] = 0

def minDist(n):
    cnt = 0
    while(True):
        cnt += 1
        if(isprime[n - cnt] == 1 or isprime[n + cnt] == 1): return cnt

n = int(input())
s = [int (s) for s in input().split()]
createPrimeNumber()
res = 0
for i in range(n):
    if(isprime[s[i]] == 0):
        dist = minDist(s[i])
        if(dist > res): res = dist
print(res)

26.Khôi phục dãy số
n = int(input())
m = []
for i in range(n):
    a = [int (a) for a in input().split()]
    m.append(a)
if n == 2: print(1, 1)
else:
    print(int((m[0][1] + m[0][2] - m[1][2]) / 2), end = " ")
    print(int((m[1][0] + m[1][2] - m[0][2]) / 2), end = " ")
    for i in range(2, n):
        print(int((m[i][0] + m[i][1] - m[0][1]) / 2), end = " ")

27.Tập hợp số bằng nhau
s = input()
usa = []; usb = []; a = []; b = []
for i in range(1000):
    usa.append(0)
    usb.append(0)
s = [int (s) for s in input().split()]
for i in s:
    if(usa[i] == 0):
        a.append(i)
        usa[i] = 1
s = [int (s) for s in input().split()]
for i in s:
    if(usb[i] == 0):
        b.append(i)
        usb[i] = 1
a.sort()
b.sort()
if a == b: print('YES')
else: print('NO')

28.Hiệu số nguyên lớn
x = int(input())
y = int(input())
print(x - y)

29.Tổng số nguyên lớn
x = int(input())
y = int(input())
print(x + y)

30.Số lộc phát đẹp
s = str(input())
state = 1
cnt = 0
if(s[0] != '6'): state = 0
for i in s:
    if(i != '6' and i  != '8'):
        state = 0
        break
    elif(i == '8'):
        cnt += 1
    else:
        if(cnt > 2):
            state = 0
            break
        else: cnt = 0
    if(cnt > 2): state = 0
if(state == 1): print('YES')
else: print('NO')

31.Sắp đặt lại xâu kí tự
t = int(input())
for test in range(1, t + 1):
    s = input()
    s1 = []
    for i in s: s1.append(i)
    s = input()
    s2 = []
    for i in s: s2.append(i)
    s1.sort()
    s2.sort()
    print('Test ', test, ': ', sep = "", end = "")
    if s1 == s2: print('YES')
    else: print('NO')

32.Lớn nhất nhỏ nhất
while True:
    n = int(input())
    if n == 0: break
    min = int(input())
    max = min
    for i in range(1, n):
        num = int(input())
        if num > max: max = num
        if num < min: min = num
    if min == max: print('BANG NHAU')
    else: print(min, max)

33.Hệ cơ số 8
s = input()
cnt = len(s) % 3
if(cnt == 0): cnt = 3
res = 0
for i in s:
    cnt -= 1
    res += (ord(i) - 48) * pow(2, cnt)
    if(cnt == 0):
        print(res, end = "")
        res = 0
        cnt = 3

34.Tập hợp số nguyên
s = input()
a = [int (a) for a in input().split()]
b = [int (b) for b in input().split()]
c = list(set(a) & set(b))
c.sort()
for i in c:
    print(i, end = " ")
print()
c = list(set(a) - set(b))
c.sort()
for i in c:
    print(i, end = " ")
print()
c = list(set(b) - set(a))
c.sort()
for i in c:
    print(i, end = " ")
print()

35.Sắp xếp chẵn lẻ
n = int(input())
a = []
even = []
odd = []
while n > 0:
    s = input().split()
    for i in s:
        a.append(int(i))
    n -= len(s)
for i in a:
    if(i % 2 == 0): even.append(i)
    else: odd.append(i)
even.sort()
odd.sort()
evenIndex = 0; oddIndex = len(odd) - 1
for i in a:
    if(i % 2 == 0):
        print(even[evenIndex], end = " ")
        evenIndex += 1
    else:
        print(odd[oddIndex], end = " ")
        oddIndex -= 1

36.Đổi cơ số
t = int(input())
while t > 0:
    s = input().split()
    n = int(s[0]); b = int(s[1])
    res = []
    while (n > 0):
        tmp = n % b
        if(tmp > 9): res.append(chr(65 + tmp - 10))
        else: res.append(tmp)
        n = int(n / b)
    for i in range(len(res) - 1, -1 , -1):
        print(res[i], end = "")
    print()
    t -= 1

37.Đếm cặp đồng xu
n = int(input())
m = []
for i in range(n):
    s = input()
    a = []
    for i in s: a.append(i)
    m.append(a)
res = 0
for i in range(n):
    cntRow = 0
    cntCol = 0
    for j in range(n):
        if(m[i][j] == 'C'): cntRow += 1
        if (m[j][i] == 'C'): cntCol += 1
    res += cntRow * (cntRow - 1) / 2
    res += cntCol * (cntCol - 1) / 2
print(int(res))

38.Tổng chữ số
s = str(input())
cnt = 0
while(len(s) > 1):
    sum = 0
    for i in s:
        sum += ord(i) - 48
    s = str(sum)
    cnt += 1
print(cnt)

39.Dãy con chung của 3 số
t = int(input())
while t > 0:
    t-=1
    s = input().split()
    n, m, k = int(s[0]), int(s[1]), int(s[2])
    a = list(map(int, input().strip().split()))[:n]
    b = list(map(int, input().strip().split()))[:m]
    c = list(map(int, input().strip().split()))[:k]
    check, i, j, p = 0, 0, 0, 0
    while i < n and j < m and p < k:
        if a[i] == b[j] and b[j] == c[p]:
            print(a[i], end=' ')
            check = 1
            i, j, p = i+1, j+1, p+1
        elif a[i] < b[j]:   i += 1
        elif b[j] < c[p]:   j += 1
        else: p += 1
    if(check == 0):
        print('NO', end='')
    print()

40.Tần suất lẻ
t = int(input())
while t > 0:
    n = int(input())
    a = [int (a) for a in input().split()]
    a.sort()
    cnt = 1
    inDex = -1
    for i in range(1, n):
        if(a[i] == a[i - 1]): cnt += 1
        else:
            if cnt % 2 == 1:
                inDex = a[i - 1]
                break
            else: cnt = 1
    if (inDex == -1 and cnt % 2 == 1): inDex = a[n - 1]
    print(inDex)
    t -= 1

41.Chèn xâu
s1 = input()
s2 = input()
p = int(input())
for i in range(p - 1):
    if(i < len(s1)): print(s1[i], end = "")
print(s2, end ="")
for i in range(p - 1, len(s1), 1):
    print(s1[i], end="")

42.Tính tổng các chữ số
t = int(input())
while t >0:
    s = input()
    sum = 0
    c = []
    for i in s:
        if(i.isalpha()): c.append(i)
        else: sum += ord(i) - 48
    c.sort()
    for i in c: print(i, end = "")
    print(sum)
    t -= 1

43.Lớp Rectangle
class Rectangle:

    def __init__(self, long, width, cl):
        self.long = long
        self.width = width
        self.cl = cl

    def color(self):
        ans = ""
        ans += self.cl[0:1].upper()
        ans += self.cl[1:len(self.cl)].lower()
        return ans

    def perimeter(self):
        return (self.long + self.width) * 2

    def area(self):
        return self.long * self.width


arr = input().split()
if (int(arr[0]) <= 0 or int(arr[1]) <= 0):
    print("INVALID")
else:
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))

44.Lớp Point
import math
from decimal import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return "%.4f" % math.sqrt((p.y - self.y) * (p.y - self.y) + (p.x - self.x) * (p.x - self.x))


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1

45.Tính cân đối của ma trận 2
n = int(input())
m = []
sumTop = 0; sumBot = 0
for i in range(n):
    a = [int (a) for a in input().split()]
    m.append(a)
for i in range(n):
    for j in range(n):
        if(j < n - i - 1): sumTop += m[i][j]
        elif(j >= n - i): sumBot += m[i][j]
k = int(input())
dist = abs(sumTop - sumBot)
if(dist <= k): print('YES')
else: print('NO')
print(dist)

46.Tính điểm trung bình
n = int(input())
min = 10; max = 0; res = 0; cnt = 0
a = [float (a) for a in input().split()]
for i in a:
    if i < min: min = i
    if max < i: max = i
for i in a:
    if(i != min and i != max):
        res += i
        cnt += 1
res /= cnt
print(round(res, 2))

47.Tính tổng phân thức
t = int(input())
while t > 0:
    n = int(input())
    i = 1; res = 0
    if(n % 2 == 0): i = 2
    for i in range(i, n + 1, 2):
        res += 1 / i
    print('%6f' % res)
    t -= 1

 48.Bộ 3 ngto cùng nhau
 def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

s = input().split()
l = int(s[0]); r = int(s[1])
m = []
for i in range(l): m.append([])
for i in range(l, r):
    a = []
    for j in range(i + 1, r + 1):
        if(gcd(i, j) == 1): a.append(j)
    m.append(a)
m.append([])
for i in range(l, r - 1):
    for j in range(len(m[i])):
        for k in m[m[i][j]]:
            if(gcd(i, k) == 1): print('('  , i , ', ' , m[i][j] , ', ' , k , ')', sep = "")

49.Ngto cùng nhau
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

s = input().split()
n = int(s[0]); k = int(s[1])
res = []
for i in range(pow(10, k - 1), pow(10, k)):
    if(gcd(n, i) == 1): res.append(i)
for i in range(0, len(res), 10):
    end = i + 10
    if(end > len(res)): end = len(res)
    for j in range(i, end):
        print(res[j], end = " ")
    print()

50.Số đảo ngto cùng nhau
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

t = int(input())
while t > 0:
    s = input()
    reS = ""
    for i in range(len(s) - 1, -1, -1): reS += s[i]
    if(gcd(int(s), int(reS)) == 1): print('YES')
    else: print('NO')
    t -= 1

51.Ưu thế ngto
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
while t > 0:
    s = input()
    cnt = 0
    for i in s:
        if(i == '2' or i == '3' or i == '5' or i == '7'): cnt += 1
    if(cnt > len(s) - cnt and isPrime(len(s))): print('YES')
    else: print('NO')
    t -= 1

52.Đầu cuối ngto
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
while t > 0:
    s = input()
    f = (ord(s[0]) - 48) * 100 + (ord(s[1]) - 48) * 10 + ord(s[2]) - 48
    l = (ord(s[len(s) - 3]) - 48) * 100 + (ord(s[len(s) - 2]) - 48) * 10 + ord(s[len(s) - 1]) - 48
    if(isPrime(f) and isPrime(l)): print('YES')
    else: print('NO')
    t -= 1

53.Tích chữ số-tổng chữ số
t = int(input())
while t > 0:
    s = input()
    sum = 0; product = 1; state = 0
    for i in range(len(s)):
        if i % 2 == 1: sum += ord(s[i]) - 48
        else:
            if(s[i] != '0'):
                state = 1
                product *= ord(s[i]) -48
    if(state): print(product, sum)
    else: print(0, sum)
    t -= 1

54.Tổng chữ số-tích chữ số
t = int(input())
while t > 0:
    s = input()
    sum = 0; product = 1; state = 0
    for i in range(len(s)):
        if i % 2 == 0: sum += ord(s[i]) - 48
        else:
            if(s[i] != '0'):
                state = 1
                product *= ord(s[i]) -48
    if(state): print(sum, product)
    else: print(sum, 0)
    t -= 1

55.Đoạn cuối ngto
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
while t > 0:
    s = input()
    n = (ord(s[len(s) - 4]) - 48) * 1000 + (ord(s[len(s) - 3]) - 48) * 100 + \
        (ord(s[len(s) - 2]) - 48) * 10 + ord(s[len(s) - 1]) - 48
    if isPrime(n): print('YES')
    else: print('NO')
    t -= 1        

56.Vị trí ngto
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
while t > 0:
    s = input()
    state = 1
    for i in range(len(s)):
        if(isPrime(i) != isPrime(ord(s[i]) - 48)):
            state = 0
            break
    if(state == 1): print('YES')
    else: print('NO')
    t -= 1

57.Chẵn lẻ ngto
def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
while t > 0:
    s = input()
    sum = 0
    state = 1
    for i in range(len(s)):
        if(i % 2 != ord(s[i]) % 2):
            state = 0
            break
        sum += ord(s[i]) - 48
    if(state == 1 and isPrime(sum)): print('YES')
    else: print('NO')
    t -= 1

58.Số xen kẽ
t = int(input())
while t > 0:
    s = input()
    state = 1
    if(len(s) % 2 == 0 or s[0] == s[1]): state = 0
    else:
        for i in range(0, len(s) - 1 , 2):
            if(s[i] != s[i + 2]):
                state = 0
                break
    if(state): print('YES')
    else: print('NO')
    t -= 1

59.Tích chữ số
t = int(input())
while t > 0:
    s = input()
    res = 1
    for i in s:
        if(ord(i) != 48): res *= ord(i) - 48
    print(res)
    t -= 1

60.Số chia hết cho 3
t = int(input())
while t > 0:
    s = input()
    sum = 0
    for i in s: sum += ord(i) - 48
    if(sum % 3 == 0): print('YES')
    else: print('NO')
    t -= 1

61.Tổng chữ số ngto
def isPrime(n):
    if n <= 1: return False
    if n <= 3: return True
    if (n % 2 == 0 or n % 3 == 0): return False
    i = 5
    while i * i <= n:
        if(n % i == 0 or n % (i + 2) == 0): return False
        i += 6
    return True

t = int(input())
while t > 0:
    s = input()
    sum = 0
    for i in s: sum += ord(i) - 48
    if(isPrime(sum)): print('YES')
    else: print('NO')
    t -= 1

62.Tổng chữ số thuận nghịch
def isReversible(s):
    if len(s) == 1: return False
    l = 0; r = len(s) - 1
    while l < r:
        if(s[l] != s[r]): return False
        l += 1
        r -= 1
    return True

t = int(input())
while t > 0:
    s = input()
    sum = 0
    for i in s: sum += ord(i) - 48
    if(isReversible(str(sum))): print('YES')
    else: print('NO')
    t -= 1

 63.Sx theo tích chữ số
 def cmp(s):
    sumOfS = 1
    for i in s:
        sumOfS *= ord(i) - 48
    return sumOfS

t = int(input())
while t > 0:
    n = int(input())
    a = input().split()
    res = []
    for i in a: res.append([cmp(i), int(i)])
    res.sort()
    for i in res: print(i[1], end = " ")
    print()
    t -= 1

64.Sx theo tổng chữ số
def cmp(s):
    sumOfS = 0
    for i in s:
        sumOfS += ord(i) - 48
    return sumOfS

t = int(input())
while t > 0:
    n = int(input())
    a = input().split()
    res = []
    for i in a: res.append([cmp(i), int(i)])
    res.sort()
    for i in res: print(i[1], end = " ")
    print()
    t -= 1

65.Dãy số nhị phân
n = int(input())
a = [int (a) for a in input().split()]
res = 0
for i in range(1, n):
    if(a[i] != a[i - 1]): res += 1
print(res)

66.Số nhỏ nhất còn thiếu
n = int(input())
a = [int (a) for a in input().split()]
a.sort()
res = a[n - 1] + 1
for i in range(1, n):
    if  a[i] != a[i - 1] + 1:
        res = a[i -1] + 1
        break;
print(res)

67.Trúng thưởng
n = int(input())
a = [int (a) for a in input().split()]
a.sort()
res = a[n - 1] + 1
for i in range(1, n):
    if  a[i] != a[i - 1] + 1:
        res = a[i -1] + 1
        break;
print(res)

68.Biến đổi về 1
while True:
    n = int(input())
    if n == 0: break
    res = 1
    while n != 1:
        if n % 2 == 0: n /= 2
        else: n = n * 3 + 1
        res += 1
    print(res)

69.Chia dư cho 42
a = []
while len(a) < 10:
    s = input().split()
    for i in s:
        a.append(int(i))
used = []
for i in range(42):
    used.append(-1)
for i in range(10):
    a[i] %= 42
    used[a[i]] += 1
res = 10
for i in range(42):
    if(used[i] > 0): res -= used[i]
print(res)

70.Lãi suất ngân hàng
t = int(input())
while t > 0:
    a = [float (a) for a in input().split()]
    n = a[0]; x = a[1]; m = a[2]
    res = 0
    while n < m:
        n *= (100 + x) / 100
        res += 1
    print(res)
    t -= 1

71.Chèn dấu phẩy
s = input()
if len(s) <= 3: print(s)
else:
    start = len(s) % 3
    for i in range(start):
        print(s[i], end = "")
    if len(s) % 3 != 0: print(',', end = "")
    for i in range(start, len(s) - 3, 3):
        print(s[i], s[i + 1], s[i + 2], sep ="", end =",")
    print(s[len(s) - 3], s[len(s) - 2], s[len(s) - 1], sep ="", end ="")

72.Chẵn lẻ
t = int(input())
while(t > 0):
    s = str(input())
    S = 0
    state = 1
    for i in range(len(s)):
        if(i > 0 and abs((ord(s[i])-ord(s[i-1]))) != 2):
            state = 0
            break
        S += ord(s[i]) - 48
    if(state == 1 and S % 10 == 0): print('YES')
    else: print('NO')
    t -= 1

73.Phân tích thừa số ngto
t = int(input())
while(t > 0):
    n = int(input())
    print('1 * ', end="")
    i = 2; cnt = 0
    while(n > 1):
        if(n % i ==0):
            cnt += 1
            n /= i
        else:
            if(cnt > 0):
                print(i , "^" , cnt , " * ", sep = "", end = "")
                cnt = 0
            else: i += 1
    print(i , "^" , cnt, sep = "")
    t -= 1

74.Ước số chung ngto
def gcd(a, b):
    if b == 0: return a
    else: return gcd(b, a % b)


def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while(i * i <= n):
        if(n % i == 0):
            return False
        i = i + 1
    return True

t = int(input())
while(t > 0):
    s = str(input())
    arr = s.split()
    a = int(arr[0])
    b = int(arr[1])
    GCD = gcd(a, b)
    S = 0
    while(GCD > 0):
        S += GCD % 10
        GCD = int(GCD / 10)
    if(isPrime(S)): print('YES')
    else: print('NO')
    t -= 1

75.Số may mắn 2
t = int(input())
while(t > 0):
    s = str(input())
    state = 1
    for i in s:
        if(i != '4' and i != '7'):
            state = 0
            break
    if(state == 1): print('YES')
    else: print('NO')
    t -= 1

76.Số thuận nghịch chẵn
t = int(input())
a = ['2', '4', '6', '8', '20', '22', '24', '26', '28', '40', '42', '44', '46', '48', '60', '62', '64', '66',
     '68', '80', '82', '84', '86', '88', '200', '202', '204', '206', '208', '220', '222', '224', '226', '228',
     '240', '242', '244', '246', '248', '260', '262', '264', '266', '268', '280', '282', '284', '286', '288',
     '400', '402', '404', '406', '408', '420', '422', '424', '426', '428', '440', '442', '444', '446', '448',
     '460', '462', '464', '466', '468', '480', '482', '484', '486', '488', '600', '602', '604', '606', '608',
     '620', '622', '624', '626', '628', '640', '642', '644', '646', '648', '660', '662', '664', '666', '668',
     '680', '682', '684', '686', '688', '800', '802', '804', '806', '808', '820', '822', '824', '826', '828',
     '840', '842', '844', '846', '848', '860', '862', '864', '866', '868', '880', '882', '884', '886', '888']
s = []
for i in a:
    tmp = list(i)
    tmp.reverse()
    s.append(str(i) + (''.join(tmp)))
while t > 0:
    n = int(input())
    for i in s:
        if(int(i) < n): print(i, end = " ")
        else: break
    print()
    t -= 1

77.Liệt kê số fibo
t = int(input())
F = [0, 1, 1]
for i in range(3, 93):
    F.append(F[i - 2] + F[i - 1])
while t > 0:
    s = str(input())
    arr = s.split()
    a = int(arr[0])
    b = int(arr[1]) + 1
    for i in range(a, b):
        print(F[i], end = " ")
    print()
    t -= 1

78.Số may mắn
s = str(input())
cnt = 0
for i in s:
    if(i == '4' or i == '7'): cnt += 1
if(cnt ==4 or cnt == 7): print('YES')
else: print('NO')

79.Ngto
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True

t = int(input())
while(t > 0):
    n = int(input())
    k = 0
    for i in range (1, n):
         if gcd(i, n) == 1: k += 1
    if isPrime(k): print('YES')
    else: print('NO')
    t -= 1

80.Làm tròn số
t = int(input())
while(t > 0):
    num = input()
    if(len(num) == 1): print(num)
    else:
        state = ord(num[len(num) - 1]) - 48
        for i in range(len(num) - 2, 0, -1):
            if state >= 5: state = ord(num[i]) - 47
            else: state = ord(num[i]) - 48
        if(state >= 5): print(ord(num[0]) - 47, end = "")
        else: print(num[0], end = "")
        for i in range(1, len(num)):
            print(0, end ="")
        print()
    t -= 1

81.hello
name = input()
print("Hello ",name,'!', sep ='')

82.Chia hết cho k
s = str(input())
arr = s.split()
a = int(arr[0])
k = int(arr[1])
n = int(arr[2])
first = a + (k - a % k)
last = n - (n % k)
res = int((last - first)/ k) + 1
if res < 1: print(-1)
else:
    for i in range(first, last + k, k):
        print(i - a, end = " ")

83.Liệt kê số ngto trong dãy
F = [0, 0]
def createPrimeNumber():
    for i in range(2, 1000000): F.append(1)
    for i in range(2, 1000):
        if F[i] == 1:
            for j in range(i * i, 1000000, i):
                F[j] = 0

n = int(input())
createPrimeNumber()
used = []
for i in range (1000000):
    used.append(0)
a = [int (a) for a in input().split()]
for i in range(n):
    if(F[a[i]] == 1): used[a[i]] += 1
for i in range(n):
    if(used[a[i]] > 0):
        print(a[i], used[a[i]])
        used[a[i]] = 0

84.Khoảng cách ngto
isprime = [0, 0]
F = []
def createPrimeNumber(n, cnt):
    for i in range(2, 1000000): isprime.append(1)
    for i in range(2, 1000):
        if isprime[i] == 1:
            F.append(i)
            cnt += 1
            if cnt == n: break
            for j in range(i * i, 1000000, i):
                isprime[j] = 0

s = input().split()
n = int(s[0])
x = int(s[1])
cnt = 0
createPrimeNumber(n, cnt)
for i in range(1001, 1000000, 2):
    if cnt == n: break
    if(isprime[i] == 1):
        F.append(i)
        cnt += 1
print(x, end = " ")
for i in range(n):
    x += F[i]
    print(x , end = " ")

85.Đầu cuối
t = int(input())
while(t > 0):
    s = input()
    n = len(s)
    if( s[0] == s[len(s) - 2] and s[1] == s[len(s) - 1]): print('YES')
    else: print('NO')
    t -= 1

86.Ngto cùng nhau
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
n = int(input())
a = [int (a) for a in input().split()]
a.sort()
for i in range(n - 1):
    for j in range(i + 1, n):
        if(gcd(a[i], a[j]) == 1):
            print(a[i], a[j])

87.Ktra ngto
import math

def isPrime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if( n % i == 0): return False
    return True

s = input()
arr = s.split()
n = int(arr[0])
m = int(arr[1])
P = []
for i in range(0, 1005):
    if (isPrime(i)): P.append(1)
    else: P.append(0)
res = []
for i in range(n):
    a = [int (a) for a in input().split()]
    for j in range(m):
        res.append(P[a[j]])
inDex = 0
for i in range(n):
    for j in range(m):
        print(res[inDex], end = " ")
        inDex += 1
    print()

88.Chữ hoa chữ thường
s = str(input())
cnt = 0
for i in s:
    if(i.islower()): cnt -= 1
    else: cnt += 1
if(cnt <= 0): print(s.lower())
else: print(s.upper())

89.Xâu thăng bằng
t = int(input())
while(t > 0):
    s = str(input())
    state = 1
    if(len(s) > 2):
        for i in range(0,int(len(s) / 2)):
            if(abs(ord(s[i]) - ord(s[i + 1])) != abs(ord(s[len(s) - i - 1]) - ord(s[len(s) - i - 2]))):
                state = 0
                break
    if(state == 1): print('YES')
    else: print('NO')
    t -= 1

90.Mã hóa 2
P = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
while(True):
    s = input().split()
    if(s[0] == "0"): break
    k = int(s[0])
    for i in range(len(s[1]) - 1, -1, -1):
        if(s[1][i] == '.'): print(P[k -1], end = "")
        elif(s[1][i] == '_'): print(P[k - 2], end = "")
        else: print(P[(ord(s[1][i]) - 65 + k) % 28], end = "")
    print()

91.Mã hóa 1
t = int(input())
while t > 0:
    s = input()
    if(len(s) == 1): print(1, s, sep = "")
    else:
        cnt = 1
        for i in range(1, len(s)):
            if(s[i] == s[i - 1]): cnt += 1
            else:
                print(cnt, s[i - 1], sep = "", end = "")
                cnt = 1
        print(cnt, s[len(s) - 1], sep = "")
    t -= 1

92.Biến đổi dãy số
while(True):
    a = [int (a) for a in input().split()]
    if(a[0] == a[1] and a[1] == a[2] and a[2] == a[3] and a[3] == 0): break
    cnt = 0
    while(True):
        if (a[0] == a[1] and a[1] == a[2] and a[2] == a[3]): break;
        tmp = a[0]
        for i in range(4):
            if(i == 3): a[i] = abs(a[3] - tmp)
            else: a[i] = abs(a[i] - a[i + 1])
        cnt += 1
    print(cnt)

93.Số phát lộc
t = int(input())
while t >0:
    s = str(input())
    tmp = int(s[len(s)-2]) * 10 + int(s[len(s)-1])
    if(tmp == 86): print('YES')
    else: print('NO')
    t -= 1

94.Giải mã
t = int(input())
while(t>0):
    s = str(input())
    for i in range(len(s)):
        if(i%2==1):
            for j in range (int(s[i])): print(s[i-1],end='')
    print()
    t -= 1

95.Dãy số phù hợp
t = int(input())
while t > 0:
    n = int(input())
    a = [int (a) for a in input().split()]
    b = [int (b) for b in input().split()]
    a.sort()
    b.sort()
    state = 1
    for i in range(n):
        if(b[i] < a[i]):
            state = 0
            break
    if state == 1: print('YES')
    else: print('NO')
    t -= 1

 96.Xuất hiện nhiều lần nhất
 t = int(input())
while t > 0:
    n = int(input())
    a = [int (a) for a in input().split()]
    a.sort()
    res = 0; val = a[0]; cnt = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            if cnt > res:
                res = cnt
                val = a[i - 1]
            elif cnt == res:
                if a[i - 1] < val: val = a[i - 1]
            cnt = 1
        else: cnt += 1
    if cnt > res:
        res = cnt
        val = a[n - 1]
    elif cnt == res:
        if a[n - 1] < val: val = a[n - 1]
    if res > int(n / 2): print(val)
    else: print('NO')
    t -= 1

 97.Cặp nghịch thể 
 n = int(input())
a = [int(a) for a in input().split()]
res = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if(a[i] > a[j]): res += 1
print(res)

98.Số không giảm
t = int(input())
while t > 0:
    num = input()
    state = 1
    for i in range(len(num)-1):
        if (num[i]>num[i+1]):
            state =0
            break
    if(state == 1): print('YES')
    else: print('NO')
    t = t - 1

 99.Tách từ 
 s = str(input())
for i in range(len(s)):
    if(s[i]!=' '): print(s[i],end='')
    else:
        if(i>0 and s[i-1]!=' '): print(s[i])

100.Phép cộng
 s = str(input())
if(int(s[0]) + int(s[4]) == int(s[8])): print('YES')
else: print('NO')

101.Kiểm tra chẵn lẻ
num = int(input()) % 2
if num == 0: print('CHAN')
else: print('LE')

102.Chuyển thành chữ hoa
S = input()
print(S.upper())                    







