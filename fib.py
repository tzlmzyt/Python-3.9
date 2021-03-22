# 使用说明
#安装好 Python.exe 环境
#Windows 下 CMD 运行 py fib.py 10 
#计算 0 到 10 的斐波那契数列



#导入 sys 类库
import sys




print('打印输入的数组：',sys.argv)

#取到数组的第二个值 sys.argv[1]
#并强转 string 为 int 类型
#赋值给 n 
n = int(sys.argv[1])

print('打印需要的参数:',n )



def fib(n):
    a,b = 0 , 1
    while a < n :
        print(a , end = ',')
        a , b = b , a + b 
    print()
    
    
    
print('打印传递参数后的斐波那契数列:')
fib(n)


