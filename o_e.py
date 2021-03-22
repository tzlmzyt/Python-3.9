#使用说明
#安装好 Python.exe 环境
#Windows 下 CMD 运行 py o_e.py 
#求 2-50 内的奇数与偶数


for num in range(2,50):
	if num % 2 == 0 :
		print('Found an even number ====',num)
		continue
	print('Found an odd number -- ', num)
	