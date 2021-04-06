# Numpy_Operation Functions



### Sum

- ndarry의 elt들 간의 합을 구함, list의 sum 기능과 동일

  ```python
  test_array = np.arange(1,11)
  print(test_array)
  
  # [ 1  2  3  4  5  6  7  8  9 10]
  ```

  <br>

  ```python
  print(test_array.sum(dtype=np.float))
  
  # 55.0
  ```

<br>

### Axis

- 모든 operation function을 실행할 때, 기준이 되는 dimension 축

  ```python
  test_array = np.arange(1,13).reshape(3,4)
  print(test_array)
  
  ​```
  
  [[ 1  2  3  4]
   [ 5  6  7  8]
   [ 9 10 11 12]]
  
  ​```
  ```

  <br>

  ```python
  print(test_array.sum(axis=1))
  # [10 26 42]
  
  print(test_array.sum(axis=0))
  # [15 18 21 24]
  ```

  <br>

  ```python
  third_order_tensor = np.array([test_array, test_array, test_array])
  print(third_order_tensor)
  
  ​```
  
  [[[ 1  2  3  4]
    [ 5  6  7  8]
    [ 9 10 11 12]]
  
   [[ 1  2  3  4]
    [ 5  6  7  8]
    [ 9 10 11 12]]
  
   [[ 1  2  3  4]
    [ 5  6  7  8]
    [ 9 10 11 12]]]
  
  ​```
  ```

  <br>

  ```python
  print(third_order_tensor.sum(axis=2))
  ​```
  [[10 26 42]
   [10 26 42]
   [10 26 42]]
  ​```
  
  print(third_order_tensor.sum(axis=1))
  ​```
  [[15 18 21 24]
   [15 18 21 24]
   [15 18 21 24]]
  ​```
  
  print(third_order_tensor.sum(axis=0))
  ​```
  [[ 3  6  9 12]
   [15 18 21 24]
   [27 30 33 36]]
  ​```
  ```

<br>

### Mean & Std

- ndarray의 elt들 간의 평균 또는 표준 편차를 반환

  ```python
  test_array = np.arange(1,13).reshape(3,4)
  print(test_array)
  
  ​```
  [[ 1  2  3  4]
   [ 5  6  7  8]
   [ 9 10 11 12]]
  ​```
  ```

  <br>

  ```python
  print(test_array.mean())
  # 6.5
  
  print(test_array.mean(axis=0))
  # [5. 6. 7. 8.]
  ```

  <br>

  ```python
  print(test_array.std())
  # 3.452052529534663
  
  print(test_array.std(axis=0))
  # [3.26598632 3.26598632 3.26598632 3.26598632]
  ```

<br>

### Mathmatical Functions

- exponential

  exp, expml, exp2, log, log10, loglp, log2, power, sqrt

  <br>

- trigonometric

  sin, cos, tan, acsin, arccos, atctan

  <br>

- hyperbolic

  sinh, cosh, tanh, acsinh, arccosh, atctanh

  <br>

<br>

### Concatenate

- Numpy array를 합치는 함수

  ```python
  a = np.array([1, 2, 3])
  b = np.array([2, 3, 4])
  print(np.vstack((a, b)))
  
  ​```
  [[1 2 3]
   [2 3 4]]
  ​```
  
  a = np.array([[1], [2], [3]])
  b = np.array([[2], [3], [4]])
  print(np.hstack((a, b)))
  
  ​```
  [[1 2]
   [2 3]
   [3 4]]
  ​```
  ```

  <br>

  ```python
  a = np.array([[1, 2, 3]])
  b = np.array([[2, 3, 4]])
  print(np.concatenate((a, b), axis=0))
        
  ​```
  [[1 2 3]
   [2 3 4]]
  ​```
  
  a = np.array([[1, 2], [3, 4]])
  b = np.array([[5, 6]])
  print(np.concatenate((a, b.T), axis=1))
  
  ​```
  [[1 2 5]
   [3 4 6]]
  ​```
  ```

  