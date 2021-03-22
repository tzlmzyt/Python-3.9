#使用说明
#安装好 Python.exe 环境
#Windows 下 CMD 运行 py p_num.py 
#求出 2-99 内所有的素数



for a in range(2,100):
    for b in range(2,a):
            if a % b == 0:
                    print(a, 'equals', b, '*', a//b)
                    break
    else:
        print(a, 'is a prime number')
        
        
   
#range(2,100)
#    2 <= a < 100


#a = 2
#b = list(range(2,2)) = null 
#b = null
#a % b == null
#else: a = 2 is a prime number



#a = 3
#b = list(range(2,3)) = 2
#a % b = 3 % 2 = 1
#else:3 is prime number




#a = 4
#b = list(range(2,4)) = 2,3
#if b = 2
#a % b = 4 % 2 = 0
#print:4 equals 2 * 2
#break: 跳出 b 的 for 循环, 后面代码全部取消执行
#这是素数的性质: 只要被一个小的数字相除余数等于零,后面大的数字就不算了
#不会执行下面的代码:
#if b = 3
#a % b = 4 % 3 = 1
#else: print something









