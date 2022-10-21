# KorToBraille_Python

한글을 점자로 번역할 수 있는 KorToBraille 파이썬 패키지입니다.

KorToBraille Python package that translates Korean to braille string.

## Quick Start

```shell
$ pip install KorToBraille
```

## Usage Example

```python
from KorToBraille.KorToBraille import KorToBraille

b = KorToBraille()
print(b.korTranslate("안녕하세요. 점자 번역 패키지입니다."))
```

### print 결과

```python
⠣⠒⠉⠻⠚⠠⠝⠬⠲⠀⠨⠎⠢⠨⠀⠘⠾⠱⠁⠀⠙⠗⠋⠕⠨⠕⠕⠃⠉⠕⠊⠲⠀
```
