# '- BOJ 1111\n'
# > '- [BOJ 1111](../master/python/BOJ_1111.py)\n'
md_file = open('README.md', 'r')

# str_file = ""
# while True:
#     line = md_file.readline()
#     str_file += line
#     if not line: break
# print(str_file)

# 파일 읽기
list_file = md_file.readlines()

write_list = [] # 변환된 문장을 포함하여 저장될 list
for line in list_file:
    sp_line = line.split()
    # 특정 문자열 확인 및 변환
    if sp_line[0] == '-' and sp_line[1] == 'BOJ':
        temp = '- [BOJ ' + sp_line[2] + '](../master/python/BOJ_' + sp_line[2] + '.py)\n\n'
        write_list.append(temp)
    else:
        write_list.append(line)
md_file.close()

# 파일 쓰기
new_file = open('new_README.md', 'w')
for line in write_list:
    new_file.write(line)
new_file.close()