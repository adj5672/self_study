# Numpy_ndarray



### Import

```python
import numpy as np
```

> numpy 호출 방법
>
> 일반적으로 np라는 alias 이용해서 호출



### Array creation

```python
test_array = np.array([1, 4, 5, 8], float)

print(test_arry)
# [1. 4. 5. 8.]

print(type(test_array[3]))
# <class 'numpy.float64'>

print(type(test_array))
# <class 'numpy.ndarray'>
```

> np.array 함수를 활용하여 배열 생성 => ndarry
>
> 하나의 데이터 type (ex. float, int, ...) 만 배열에 넣을 수 있음 = `Dynamic typing not supprted`
>
> C의 Array를 사용하여 배열 생성
>
> `.dtype` : Array 전체의 data type을 반환



```python
test_array = np.array([1, 4, 5, '8'], float)
# str data를 입력해도 float으로 자동 형변환 실시

print(test_array.shape)
# (4,)

print(test_array.dtype)
# float64

print(test_array.ndim)
# 1

print(test_array.size)
# 4
```

> `.shape` : numpy array의 object의 dimension 구성을 반환함 ( tuple type )
>
> ex) (a_1, a_2, ... , a_n)  =>  n차원 a_1 * a_2 * ... * a_n 배열
>
> 
>
> `.dtype` : numpy array의 데이터 type을 반환함
>
> 1차원 : vector, 2차원 : matrix, 3차원 : 3rd order tensor
>
>  
>
> `.ndim` : number of dimension
>
>  
>
> `.size` : data의 갯수



### Array dtype

> Ndarray의 single element가 가지는 data type
>
> 각 elt가 차지하는 memory의 크기가 결정됨

```python
np.array([[1, 2, 3], [4.5, 5, 6]], dtype=int)
```

> int - 4 byte, float32 - 4 byte, float64 - 8 byte ...
>
> 
>
> `.nbytes` : ndarray object의 메모리 크기를 반환함



