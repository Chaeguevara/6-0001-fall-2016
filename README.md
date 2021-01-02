# 6-0001-fall-2016

> 이 프로젝트는 다음의 링크를 참고하여, 과제부분만 올리고 있습니다.  
>
> 원 강의 제목은 : Introduction to Computer Science and Programming in Python 입니다.
>
> https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/



# Lecture 4

> Decomposition, Abstraction and Functions



만약 엄청나게 많은 코드를 써야 한다면? 내용이 어지럽고, 하나 고칠때 하나하나 찾아 다녀야 한다. 더 많은 기능들을 더해라.

길이가 아니라 기능위주로 해야한다.



## Function

> Decomposition and Abstraction

프로젝터 예시

- 케이스
- 렌즈
- 환기시설

 이런 각각을 주어졌을때 프로젝트를 만들 수 있을까?



만약 그냥 완성품을 준다면 한시간 안에 어떻게 작동하는지 알아 낼 수 있는가.



블랙박스를 이용하기 위해 어떻게 작동하는지 알 필요는 없음. 블랙박스라고 생각하면 됨. 

Abstraction 어떻게 작동하는지 알 필요 없음.

## Decomposition

> 최종목표를 위해 다른 장비들이 함께 작동하는 것.

큰 이미지를 만들때, 작은 프로젝트를 여러개 합쳐서 하나의 이미지로 만드는 것. 

위 개념들을 프로그래밍에도 적용할 수 있음.

코드를 모듈로 나누는 것

- 재사용 가능함.

Class를 이용할 예정.



## Abstraction

> 코드 조각을 블랙박스로 생각하는것
>
> 프로젝터 예시에선 프로젝터를 사용하기 위해 작동원리를 알아야 할 필요는 없었던 것과 같음.

- 세부사항을 알 필요가 없음
- 세부사항을 알기 원할 필요가 없음.



## Function

> Function을 만드는 사람 vs Function을 사용하는 사람

재사용 가능한 코드를 만드는 것이 Functions

Called 또는 invoked 되기 전까지 Functions은 실행되지 않음

Function의 특징

- 이름을 가짐
- Parameter(변수)를 가짐
- docstring(설명서)을 가짐
- Body를 가짐
- 무언가 return 함.



## Function 정의와 사용

### Function 정의

```python
def is_even(i):
    """
    input : ~
    returns : ~
    """
    print("inside is_even")
    return i% == 0
    
is_even(3)
```

키워드,이름,인풋, 바디

`def`키워드

`is_even`이름

바디는 코드가 쓰인 부분

### Scope

Environment와 같다. Function의 Scope는 메인 프로그램과 완전히 별개다.

formal paramter = 인풋과 같음. `def f(x)`에서 `x`.

종이를 가지고 따라해보면 도움이 많이 된다.

#### 파이썬의 sequence

1. Global scope를 확인한다.
2. Def가 있으면 그냥 넘어간다.
3. function call이 있으면, new scope로 이동함
4. parameter를 mapping 한다.
   1. x가 특정 값을 받는다.
   2. 계산한다
   3. 계산한 값을 return한다
5. Global scope에서 받는다.



### Return이 없다면?

None이 return 됨. None이 string이 아님.



## Function as Arguments

파이썬의 모든 것은 Object이다. -> Integer, string, function도 

function을 function의 input으로 할 수 있음

```python
def func_a():
    print 'inside func_a'
def func_b(y):
    print 'inside func_b'
    return y
def func_c(z):
    print 'inside func_c'
    return z()

print func_a()
print 5 + func_b(2)
print func_c(func_a)
```

글로벌 스코프, 각자 스코프 왔다갔다 매핑을 하며 값을 계산한다.



## 다른 Scope에 있는 같은 이름의 variable

```python
def f(y):
    x = 1
    x +=1
    print(x)
x = 5
f(x)
print(x)

-> 2
```

globla scope의 x는 그대로임.



```python
def g(y):
    print(x)
    print(x+1)
    
x = 5
g(x)
print(x)
```

에러는 나지 않음. 잠시 스코프를 나가서, `x`를 찾아서 그 값을 내보냄. 문제는 안됨

```python
def h(y): 
    x += 1
    
x = 5
h(x)
print(h(x))
```

파이썬에서 허락되지 않은 방법. 에러가 나올 것이다.



## 더 어려운 Scope 관련된 것

www.pythontutor.com

요지는 local scope에서 global scope의 값을 가져올 수는 있지만 update는 할 수 없음.