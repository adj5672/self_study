# Numpy_Creation functions



### Arange

```python
print(np.arange(30))
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

print(np.arange(0, 5, 0.5))
# [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]

print(np.arange(30).reshape(5, 6))
# [[ 0  1  2  3  4  5]
   [ 6  7  8  9 10 11]
   [12 13 14 15 16 17]
   [18 19 20 21 22 23]
   [24 25 26 27 28 29]]
```



### Ones, Zeros and Empty



- zeros - 0 으로 가득찬 ndarray 생성
- np.zeros(shape, dtype, order)

```python
print(np.zeros(shape=(10,), dtype=np.int8)) # 10 - zero vector 생성
# [0 0 0 0 0 0 0 0 0 0]

print(np.zeros(2, 5)) # 2 by 5 - zero matrix 생성
# [[0. 0. 0. 0. 0.]
   [0. 0. 0. 0. 0.]]
```



- ones - 1 로 가득찬 ndarray 생성
- np.ones(shape, dtype, order)

```python
print(np.ones(shape=(10,), dtype=np.int8))
# [1 1 1 1 1 1 1 1 1 1]

print(np.ones((2, 5)))
# [[1. 1. 1. 1. 1.]
   [1. 1. 1. 1. 1.]]
```



- empty - shape 만 주어지고 비어있는 ndarray 생성
- (memory initialization 이 되지 않음)

```python
print(np.empty(shape=(10,), dtype=np.int8))
# [0 0 0 0 0 0 0 0 0 0]

print(np.empty((3, 5)))
# [[6.23042070e-307 4.67296746e-307 1.69121096e-306 1.15710631e-306
  1.89146896e-307]
 [7.56571288e-307 3.11525958e-307 1.24610723e-306 1.37962320e-306
  1.29060871e-306]
 [2.22518251e-306 1.33511969e-306 1.78022342e-306 1.05700345e-307
  2.76676762e-322]]
```



### Something_like

- 기존 ndarray 의 shape 크기 만큼 1, 0 또는 empty array 를 반환

```python
test_matrix = np.arange(30).reshape(5, 6)
print(np.ones_like(test_matrix))
# [[1 1 1 1 1 1]
   [1 1 1 1 1 1]
   [1 1 1 1 1 1]
   [1 1 1 1 1 1]
   [1 1 1 1 1 1]]
```



### Identity

- 단위 행렬(i 행렬)을 생성함
- n : number of rows

```python
print(np.identity(n=3, dtype=np.int8))
# [[1 0 0]
   [0 1 0]
   [0 0 1]]

print(np.identity(5))
# [[1. 0. 0. 0. 0.]
   [0. 1. 0. 0. 0.]
   [0. 0. 1. 0. 0.]
   [0. 0. 0. 1. 0.]
   [0. 0. 0. 0. 1.]]
```



### Eye

- 대각선인 1 인 행렬, k 값의 시작 index의 변경이 가능

```python
print(np.eye(N=3, M=5, dtype=np.int8))
# [[1 0 0 0 0]
   [0 1 0 0 0]
   [0 0 1 0 0]]

print(np.eye(3))
# [[1. 0. 0.]
   [0. 1. 0.]
   [0. 0. 1.]]

print(np.eye(3, 5, k=2)) # k -> start index
# [[0. 0. 1. 0. 0.]
   [0. 0. 0. 1. 0.]
   [0. 0. 0. 0. 1.]]
```



### Diag

- 대각 행렬의 값을 추출함

```python
matrix = np.arange(9).reshape(3, 3)
print(np.diag(matrix))
# [0 4 8]

print(np.diag(matrix, k=1))
# [1 5]
```



### Random Sampling

- 데이터 분포에 따른 sampling 으로 array 를 생성

```python
print(np.random.uniform(0, 1, 10).reshape(2, 5))
# uniform(최저값, 최고값, data의 갯수)
# [[0.30841147 0.09319815 0.38289644 0.90846888 0.29261764]
   [0.21551435 0.02814042 0.55807496 0.73554135 0.30552729]]

print(np.random.normal(0, 1, 10).reshape(2, 5))
# normal(평균값, 정규분포값, data의 갯수)
# [[ 0.26299882 -0.89533726  0.64413963 -0.28083774  0.46074825]
   [-1.66382924 -0.6088911  -0.82379425  1.13391423  0.19290565]]
```

