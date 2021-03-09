# Numpy_Handling shape



### reshape

> `.reshape` : Array의 shape의 크기를 변경함 ( elt의 갯수는 동일 )
>
> 기존 array는 변형되지 않는다.
>
> Array의 size만 같다면 다차원으로 자유로이 변형 가능하다.
>
> ex) .reshape(-1, 2) : 열은 2개, 행은 size에 맞게 나머지 할당

```python
test_matrix = [[1, 2, 3, 4], [1, 2, 5, 8]]

print(np.array(test_matrix).shape)
# (2, 4)

print(np.array(test_matrix).reshape(8,))
# [1 2 3 4 1 2 5 8]

print(np.array(test_matrix).reshape(8,).shape)
# (8,)
```



### flatten

> `.flatten` : 다차원 array를 1차원 array로  변환

```python
test_matrix = [[[1, 2, 3, 4], [1, 2, 5, 8]], [[1, 2, 3, 4], [1, 2, 5, 8]]]

print(np.array(test_matrix).flatten())
# [1 2 3 4 1 2 5 8 1 2 3 4 1 2 5 8]
```

