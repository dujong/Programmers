list_str = ['A','B','C','D']
list_int = list(map(ord, list_str)) # 정수로 변환
list_str2 = list(map(chr, list_int)) # 다시 문자열로 변환
print(list_int)
print(list_str2)