#example反向输出
strs = input('请输入一段文本')
i = len(strs)-1
while i >= 0:
    print(strs[i],end = '')
    i =i-1
