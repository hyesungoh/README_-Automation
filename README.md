# README_linker
### for AA_Algorithm's readme
---
- AA_Algorithm 레포의 readme를 하나하나 수정하기 귀찮아서 만들었습니다.

```md
#### 20.06.17
- BOJ 1330
  문제 풀이 설명 및 느낀점
- BOJ 2753
  문제 풀이 설명 및 느낀점
#### 20.06.22
- BOJ 14681
  문제 풀이 설명 및 느낀점
- BOJ 2884
  문제 풀이 설명 및 느낀점
```
##### 이렇게 되어 있는 것을
```md
#### 20.06.17
- [BOJ 1330](../master/python/BOJ_1330.py)

  문제 풀이 설명 및 느낀점
- [BOJ 2753](../master/python/BOJ_2753.py)

  문제 풀이 설명 및 느낀점
#### 20.06.22
- [BOJ 14681](../master/python/BOJ_14681.py)

  문제 풀이 설명 및 느낀점
- [BOJ 2884](../master/python/BOJ_2884.py)

  문제 풀이 설명 및 느낀점
```
##### 이렇게 줄바꿈 + 해당 문제 파일에 linking
---

```python
md_file = open('README.md', 'r')

list_file = md_file.readlines()
# ['line1', 'line2', ...]
```
- 파일을 읽기 모드로 열고 readlines()를 사용하여 저장


```python
write_list = [] # 변환된 문장을 포함하여 저장될 list
for line in list_file:
    sp_line = line.split()
    # 특정 문자열 확인 및 변환
    if sp_line[0] == '-' and sp_line[1] == 'BOJ':
        temp = '- [BOJ ' + sp_line[2] + '](../master/python/BOJ_' + sp_line[2] + '.py)\n\n'
        write_list.append(temp)
    else:
        write_list.append(line)
```
- 변환된 문장을 포함하여 저장될 `wirte_list`
- readlines() 결과인 list_file을 이용하여 for문 반복
- 각 문장을 split()한 후 첫번째와 두번째 값이 '-', 'BOJ'인 지 확인
- 내가 원하는 포맷으로 temp 변수에 문자열을 저장 후 `write_list`에 append
- 변환이 필요하지 않은 문장일 때는 기존 문장을 append

```python
new_file = open('new_README.md', 'w')
for line in write_list:
    new_file.write(line)
```
- 새로 저장될 파일을 쓰기 모드로 엶
- `write_list`를 이용하여 for문 반복 후 각 줄을 `write()`
