# 파이썬 과제 2번

## 주어진 기간 : 1주일

## 문제 1: 행맨 기초

[행멘 게임이란](<http://en.wikipedia.org/wiki/Hangman_(game)>)

### A) 게임 시작

"hangman.py" 와 "words.txt" 가 같은 폴더 안에 있도록 한다.

### B) 행멘 게임 과제

1. 컴퓨터는 words.txt에서 랜덤 단어를 뽑는다.(**모두다 소문자 단어임**)
2. 사용자에게 주어지는 n번의 기회
3. 입력하는 알파벳에 따라
   1. 단어에 포함된 알파벳이면, 그 부분을 보여줌
   2. 사용자에게 불이익을 주고 남은 추측 수를 업데이트
4. 추측 수를 다 쓰거나, 단어를 다 맞히면 게임이 끝남



## 문제 2: 파트 1: 3개의 도우미 기능

시작 하기전, 하위 업무로 나누고 3개의 도우미 기능을 만들 것이다.

### 1. is_word_guessed(secret_word, letters_guessed)

> 알파벳이 이미 추측 되었는지(사용 되었는지)확인

`secret_word = string`

`letters_guessed = list of string`

Boolean을 반환한다. 즉 새로 입력한 알파벳이 이미 추측 되었으면 True, 아니라면 False.

예시)

```
>>> secret_word = 'apple'
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
>>> print(is_word_guessed(secret_word, letters_guessed)) 
False
```





### 2.get_guessed_word(secret_word,letters_guessed)

> 단어중 추정된 문자를 보여줌

`secret_word = string`

`letters_guessed = list of string`

"_ " 또는 추측 성공한 단어를 보여줌."_ "를 사용한 이유는 기본적으로 보기 간편하며 "___"와 같은 경우를 방지한다.usability라 불림.

힌트: 어떤 정보를 내보낼지 생각해봐라. 루프를 돌며 정보를 저장해야 할지. 정보를 이미 축적된 결과에 어떻게 더할지.

예시:

```
>>> secret_word = 'apple'  
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
>>> print(get_guessed_word(secret_word, letters_guessed)) 
'_ pp_ e' 
```





### 3. get_available_letters(letters_guessed)

`letters_guessed = a list of letters`

**예시:**

```
>>> letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
>>> print get_available_letters(letters_guessed) 
abcdfghjlmnoqtuvwxyz
```



## 문제3 / 파트2: 게임

hangman(secret_word)

세가지 기능을 잘 사용해 보아라.

### A) 게임 아키텍쳐

1. 컴퓨터가 단어를 고른다.
2. 유저는 6개의 추측으로 시작한다.
3. 몇개짜리 단어인지, 그리고 추측이 몇개 남았는지 보여준다
4. 여태까지 추측한 단어들과 "남은 추측수"를 보여준다.

예시>

```
Loading word list from file... 
55900 words loaded. 
Welcome to the game Hangman! 
I am thinking of a word that is 4 letters long.  
-------------  
You have 6 guesses left. 
Available letters: abcdefghijklmnopqrstuvwxyz 
```





### B) 유저 컴퓨터 상호작용

1. 각 게임전, 다음을 보여준다.
   1. 남은 추측수
   2. 아직 추측되지 않은 문자들
2. 한번에 하나의 문자만(상세 설명은 아래에)
3. 문자 입력과 함께, 맞았는지 틀렸는지 알려준다.
4. 추측 된 문자와 그렇지 않은 것을 보여준다 (a_ _ le)
5. -----를 출력하여 각 추측 게임을 구분한다.

예시>

```
You have 6 guesses left. 
Available letters: abcdefghijklmnopqrstuvwxyz 
Please guess a letter: a 
Good guess: _ a_ _ 
------------  
You have 6 guesses left. 
Available letters: bcdefghijklmnopqrstuvwxyz 
Please guess a letter: b 
Oops! That letter is not in my word: _ a_ _ 
```



### C) 입력값 제약사항

1. 1입력당 1문자. 대,소문자는 ok, 나머지는 NG.
2. 알파벳 이외는 3회까지 warning을 띄워준다. 더이상 warning이 남지 않았을때는 guess에서 하나 차감한다.

힌트 1:  `input`을 이용해서 입력값을 받는다.

1. 알파벳인지 확인
2. 알파벳 이외를 넣으면 warning에서 1차감.

힌트 2:  `str.isalpha('your string')` 과 `str.lowercase('your string')`을 사용하면 좋다.

힌트 3: words.txt안의 단어들은 다 소문자이다.

게임 예시

```
You have 3 warnings left. 
You have 6 guesses left. 
Available letters: bcdefghijklmnopqrstuvwxyz 
Please guess a letter: s
Oops! That letter is not in my word: _ a_ _  
------------  
You have 5 guesses left. 
Available letters: bcdefghijklmnopqrtuvwxyz 
Please guess a letter: $
Oops! That is not a valid letter. You have 2 warnings left:  _ a_ _  
```

​	

### D) 게임 규칙

1. 3 warnings 로 시작
2. 알파벳 이외를 넣으면, 경고 띄움
   1. 남은 경고수를 보여줌 -1 warnings
   2. 경고가 더이상 없으면 -1 guess
3. 이미 추정된 단어를 입력하면 경고 띄움
   1. 남은 경고수를 보여줌 -1 warnings
   2. 경고가 더이상 없으면 -1 guess 
4. 단어에 포함된 문자를 추측하면 guess 차감 없음
5. 만약 단어에 없지만 **모음**의 경우 -2 guess
6. **자음**의 경우 -1 guess

게임 예시

```
You have 5 guesses left. 
Available letters: bcdefghijklmnopqrtuvwxyz 
Please guess a letter: t
Good guess: ta_ t  
------------  
You have 5 guesses left. 
Available letters: bcdefghijklmnopqrtuvwxyz 
Please guess a letter: e
Oops! That letter is not in my word: ta_ t  
------------  
You have 3 guesses left. 
Available letters: bcdfghijklmnopqrtuvwxyz 
Please guess a letter: e
Oops! You've already guessed that letter. You now have 2 warnings:
ta_ t 

```

### E) 게임 종료

1. 다 맞히거나, guess 0이면

2. guess 0이 되면, lost 띄우기 + 단어 공개

3. 유저가 이기면 축하 그리고 점수 공개

4. 점수 식은 다음과 같음. 

   Total score = guesses_remaining* number unique letters in secret_word



이겼을때,

```
You have 3 guesses left. 
Available letters: bcdfghijklnopquvwxyz 
Please guess a letter: c
Good guess: tact  
------------  
Congratulations, you won! 
Your total score for this game is: 9 
```

```
You have 3 guesses left. 
Available letters: bcdfghijklnopquvwxyz 
Please guess a letter: n
Good guess: dolphin  
------------  
Congratulations, you won! 
Your total score for this game is: 21 
```

### F) 힌트

1. 필요하다면 기능 더 추가
2. 저장해야 할 4가지 정보들
   1. `secret_word`
   2. `letters_guessed` - 지금까지 추측된 문자들. 이미 추측된 문자를 사용하면 페널티 부여
   3. `guesses_remaining` 남은 추측 수
   4. `warnings_remaining` 남은 경고수.



### G) 나만의 기능

내가 필요한 기능들을 정의하고 써야겠다.

#### is_word_correct(user_input,secret_word)

> 입력한 문자와, 단어를 비교하여 입력한 문자가 제대로 추정했는지 보여줌.

`user_input = single character`

`secret_word = string`

1. `user_input` 과  `secret_word`의 각 letter와 비교한다
2. 만약 같은게 있다면 `return True`
3. 없다면 `return False`
4. 코드 흐름상 이미 사용된 문자인지 걸러내는 과정이 있기 때문에 바로 비교하면 된다.



#### win_or_lose(guessed_words)

> 게임의 승패를 결정한다. 

1. 지금까지 추정한 단어를 받는다 `app_ _ e` (`apple`)
2. 각 문자를 확인한다
3. 만약 모든 문자가 알파벳이라면, 이긴것 `True` 아니면 `False`로 한다.

### H) 게임 예시

최대한 보기와 비슷하게 할 것!

이기는 경우

```
Loading word list from file... 
55900 words loaded. 
Welcome to the game Hangman! 
I am thinking of a word that is 4 letters long.  
You have 3 warnings left. 
-------------  
You have 6 guesses left. 
Available letters: abcdefghijklmnopqrstuvwxyz 
Please guess a letter: a
Good guess: _ a_ _  
------------  
You have 6 guesses left. 
Available letters: bcdefghijklmnopqrstuvwxyz 
Please guess a letter: a
Oops! You've already guessed that letter. You have 2 warnings left:  
_ a_ _  
------------  
You have 6 guesses left. 
Available letters: bcdefghijklmnopqrstuvwxyz 
Please guess a letter: s
Oops! That letter is not in my word. 
Please guess a letter: _ a_ _ 
------------  
You have 5 guesses left. 
Available letters: bcdefghijklmnopqrtuvwxyz 
Please guess a letter: $
Oops! That is not a valid letter. You have 1 warnings left: _ a_ _  
------------
You have 5 guesses left. 
Available letters: bcdefghijklmnopqrtuvwxyz 
Please guess a letter: t
Good guess: ta_ t  
------------  
You have 5 guesses left. 
Available letters: bcdefghijklmnopqrtuvwxyz 
Please guess a letter: e
Oops! That letter is not in my word: ta_ t 
------------  
You have 3 guesses left. 
Available letters: bcdfghijklmnopqrtuvwxyz 
Please guess a letter: e
Oops! You've already guessed that letter. You have 0 warnings left:
ta_ t  
------------  
You have 3 guesses left. 
Available letters: bcdfghijklmnopqrtuvwxyz 
Please guess a letter: e
Oops! You've already guessed that letter. You have no warnings left   
so you lose one guess: ta_ t  
------------  
You have 2 guesses left. 
Available letters: bcdfghijklnopquvwxyz 
Please guess a letter: c
Good guess: tact  
------------  
Congratulations, you won! 
Your total score for this game is: 6 
```



지는 경우

``` 
Loading word list from file... 
55900 words loaded. 
Welcome to the game Hangman! 
I am thinking of a word that is 4 letters long 
You have 3 warnings left. 
-----------  
You have 6 guesses left 
Available Letters: abcdefghijklmnopqrstuvwxyz 
Please guess a letter: a
Oops! That letter is not in my word: _ _ _ _ 
-----------  
You have 4 guesses left 
Available Letters: bcdefghijklmnopqrstuvwxyz 
Please guess a letter: b
Oops! That letter is not in my word: _ _ _ _ 
-----------  
You have 3 guesses left 
Available Letters: cdefghijklmnopqrstuvwxyz 
Please guess a letter: c
Oops! That letter is not in my word: _ _ _ _ 
-----------  
You have 2 guesses left 
Available Letters: defghijklmnopqrstuvwxyz 
Please guess a letter: 2
     Oops! That is not a valid letter. You have 2 warnings left: _ _ _ _  
-----------  
You have 2 guesses left 
Available Letters: defghijklmnopqrstuvwxyz 
Please guess a letter: d
Oops! That letter is not in my word: _ _ _ _ 
-----------  
You have 1 guesses left 
Available Letters: efghijklmnopqrstuvwxyz 
Please guess a letter: e
Good guess: e_ _ e 
-----------  
You have 1 guesses left 
Available Letters: fghijklmnopqrstuvwxyz 
Please guess a letter: f
Oops! That letter is not in my word: e_ _ e 
-----------  
Sorry, you ran out of guesses. The word was else.  
```

실행하고 싶을 땐 다음 부분을 연다

```python
 if __name__ == “__main__”:
#secret_word = choose_word(wordlist) 
#hangman(secret_word)
```



## 문제 4 / 파트 3 : 힌트와 함께