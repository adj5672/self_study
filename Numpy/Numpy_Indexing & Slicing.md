# Numpy_Indexing & Slicing



### Indexing

```python
import numpy as np

a = np.array([[1, 2, 3], [4.5, 5, 6]], int)

print(a)
print(a[0, 0]) # Two dimensional array represenation #1
print(a[0][0]) # Two dimensional array represenation #2
```

- List와 달리 이차원 배열에서 [0, 0] 과 같은 표기법을 제공
- Matrix 일 경우 앞은 row 뒤는 column



### Slicing

```python
a = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], int)

a[:,2:] # 전체 row의 2열 이상
a[1,1:3] # 1 row의 1열 ~ 2열
a[1:3] # 1 row ~ 2 row의 전체
a[:,::2] # 전체 row의 짝수 index 열
```

- List와 달리 행과 열 부분을 나눠서 slicing이 가능함
- Matrix의 부분 집합을 추출할 때 유용함