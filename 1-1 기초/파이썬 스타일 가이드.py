# Correct:
# easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
          



==== 임포트 ====

import 우선순위:

	Standard library imports.
	Related third party imports.
	Local application/library specific imports.
	You should put a blank line between each group of imports.

		# Correct:
			import os
			import sys

		# Wrong:
			import sys, os

Module level “dunders” (i.e. names with two leading and two trailing underscores) 
such as __all__, __author__, __version__, etc. 
should be placed after the module docstring but before any import statements except from __future__ imports. 

	"""This is the example module.

	This module does stuff.
	"""

	from __future__ import barry_as_FLUFL

	__all__ = ['a', 'b', 'c']
	__version__ = '0.1'
	__author__ = 'Cardinal Biggles'

	import os
	import sys
			
절대경로로 Import 하는걸 권장합니다.

	import mypkg.sibling
	from mypkg import sibling
	from mypkg.sibling import example
	
Wildcard imports (from <module> import *) should be avoided

 
==== 네이밍 컨벤션 ====

0. 
모듈 이름은 모두 소문자로 쓰고 가급적 짧게 짓습니다. 

1.
클래스 이름은 CapWords = CamelCase (CapitalizedWords == CapWords != mixedCase) 를 씁니다. 

	클래스가 포함된 모듈에서 클래스를 가져올 때 일반적으로 다음과 같이 철자를 쓰는 것이 좋습니다.

		from myclass import MyClass
		from foo.bar.yourclass import YourClass
	

2.	
변수 이름(클래스의 인스턴스 변수 포함), 
함수이름(클래스의 메서드 포함)은 
모두 소문자로 쓰며 필요에 따라 언더스코어를 쓸 수 있습니다. 
(mixedCase는 이미 그렇게 쓰여서 일관성을 유지해야 하는 경우에만 쓰입니다.)

	_name 은 (외부에서  import 된 객체가 아닌) 해당 모듈 내부에서만 사용되는 함수라는 걸 가리킵니다.
	
	name_ 은 파이썬 키워드와 충돌을 피하기 위해 씁니다.  ex)  class_
	
	단일 이름 변수를 쓸 때 대문자 i 소문자 l 대문자 o 는 쓰지 않습니다 

3.
언더스코어를 쓰면 모두 소문자로 쓰든지 모두 대문자로 씁니다.
lower_case_with_underscores

UPPER_CASE_WITH_UNDERSCORES

	상수는 모두 대문자로 씁니다. 

	약어의 모든 문자를 대문자로 표시하십시오. 따라서 HTTPServerError는 HttpServerError보다 낫습니다.


==== 공백 ====

1. 
최상위 함수 및 클래스 정의를 두 개의 빈 줄로 묶습니다.

2.
클래스 내부의 메서드 정의는 단일 빈 줄로 둘러싸여 있습니다.

3.
 불필요한 공백을 피하세요.

	괄호, 대괄호 또는 중괄호 바로 안에:
		# Correct:
		spam(ham[1], {eggs: 2})
		# Wrong:
		spam( ham[ 1 ], { eggs: 2 } )

	후행 쉼표와 다음의 닫는 괄호 사이:
		# Correct:
		foo = (0,)
		# Wrong:
		bar = (0, )

	쉼표, 세미콜론 또는 콜론 바로 앞:
		# Correct:
		if x == 4: print(x, y); x, y = y, x
		# Wrong:
		if x == 4 : print(x , y) ; x , y = y , x


4. 
우선순위가 다른 연산자를 사용하는 경우 
우선순위가 가장 낮은 연산자 주위에 공백을 추가하는 것이 좋습니다. 
그러나 공백을 두 개 이상 사용하지 말고 이항 연산자의 양쪽에 항상 같은 양의 공백을 두십시오.

	# Correct:
		i = i + 1
		submitted += 1
		x = x*2 - 1
		hypot2 = x*x + y*y
		c = (a+b) * (a-b)

	# Wrong:
		i=i+1
		submitted +=1
		x = x * 2 - 1
		hypot2 = x * x + y * y
		c = (a + b) * (a - b)

5.
모듈 수준 변수, 
클래스 및 인스턴스 변수, 
지역 변수에 대한 주석은 콜론 뒤에 단일 공백이 있어야 합니다.

콜론 앞에는 공백이 없어야 합니다.
할당에 오른쪽이 있는 경우 등호 기호 양쪽에 정확히 하나의 공백이 있어야 합니다.
	# Correct:

		code: int

		class Point:
		    coords: Tuple[int, int]
		    label: str = '<unknown>'
	# Wrong:

		code:int  # No space after colon
		code : int  # Space before colon

		class Test:
		    result: int=0  # No spaces around equality sign
   
6.		    
함수 주석은 콜론에 대한 일반적인 규칙을 사용해야 하며 
화살표가 ->있는 경우 항상 화살표 주위에 공백이 있어야 합니다. 

	# Correct:
		def munge(input: AnyStr): ...
		def munge() -> PosInt: ...

	# Wrong:
		def munge(input:AnyStr): ...
		def munge()->PosInt: ...

7.
키워드 인수를 표시하는 데 사용되는 = 기호 주위에 공백을 사용하지 마세요 .

	# Correct:
		def complex(real, imag=0.0):
		    return magic(r=real, i=imag)
		    
	# Wrong:
		def complex(real, imag = 0.0):
		    return magic(r = real, i = imag)
    
8. 
그러나 "주석이 있는" 함수 매개변수의 기본값을 표시하는 데 사용되는 = 기호 주위에는 공백을 사용하십시오.

# Correct:
	def munge(sep: AnyStr = None): ...
	def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

==== 주석 ====

1.
비영어권 국가의 Python 코더: 귀하의 언어를 사용하지 않는 사람들이 코드를 절대 읽지 않을 것이라고 120% 확신하지 않는 한 
영어로 코멘트(주석)를 작성하십시오.
코멘트의 첫 번째 단어는 소문자로 시작하는 식별자가 아닌 한 대문자로 시작해야 합니다(식별자의 대소문자를 변경하지 마세요!).


2.
Block comments generally apply to some (or all) code that follows them, 
and are indented to the same level as that code. 
Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).

3.
Paragraphs inside a block comment are separated by a line containing a single #.

	# Correct:
		# blah
		# blah
		# blah
		# 
		# blah
		# blah
4
.
inline comment는 가급적 쓰지 않습니다
굳이 써야 한다면 코드의 기능(작동방식)이 아니라 목적(역할)을 밝히는데 쓸 순 있습니다.
block comments와 마찬가지로 

	# blah 식으로 작성합니다

5.
documentation string (docstring)

Docstring이란 무엇입니까?
독스트링(Docstring)은 모듈, 함수, 클래스 또는 메소드 정의에서 
첫 번째 명령문으로 나타나는 문자열 리터럴입니다. 
그러한 독스트링은 해당 객체의 특별한 속성 __doc__이 됩니다.

모든 모듈에는 일반적으로 독스트링이 있어야 하며, 모듈에서 내보낸 모든 함수와 클래스에도 독스트링이 있어야 합니다. 
생성자(__init__)를 포함한 공개 메소드에도 독스트링이 있어야 합니다. 
패키지는 패키지 디렉터리에 있는 __init__.py 파일의 모듈 독스트링에 문서화될 수 있습니다.

6.
There are two forms of docstrings: one-liners and multi-line docstrings.

원 라이너는 정말 명백한 경우에 사용됩니다. 정말 한 줄에 맞아야 합니다. 예를 들어:

	def kos_root():
	    """Return the pathname of the KOS root directory."""
	    global _kos_root
	    if _kos_root: return _kos_root
	    ...
	노트:

문자열이 한 줄에 들어가더라도 삼중 따옴표가 사용됩니다. 이렇게 하면 나중에 확장하기가 쉽습니다.

닫는 따옴표는 시작 따옴표와 같은 줄에 있습니다. 이것은 단일 라이너에 더 좋아 보입니다.

독스트링 앞이나 뒤에 빈 줄이 없습니다.
(클래스 메서드의 독스트링은 def line 바로 뒤에 쓰고 바디와는 한줄 띄웁니다.)

독스트링은 마침표로 끝나는 문구입니다. 이는 설명이 아닌 명령("Do this", "Return that")으로 함수나 메서드의 효과를 규정합니다.

def function(a, b):
    """Do X and return a list."""

7.
Write docstrings for all public modules, functions, classes, and methods. 
Docstrings are not necessary for non-public methods, but you should have a comment that describes what the method does. 

8.
The docstring for a function or method should summarize its behavior 
and document its arguments, return value(s), side effects, exceptions raised, and restrictions on when it can be called (all if applicable). 
Optional arguments should be indicated. 
It should be documented whether keyword arguments are part of the interface.

9.
클래스의 독스트링은 해당 동작을 요약하고 공개 메서드와 인스턴스 변수를 나열해야 합니다. 
클래스가 하위 클래스로 지정되고 하위 클래스에 대한 추가 인터페이스가 있는 경우 
이 인터페이스는 별도로 (docstring에) 나열되어야 합니다. 
클래스 생성자는 해당 __init__ 메소드에 대한 독스트링에 문서화되어야 합니다. 
개별 메소드는 자체 독스트링으로 문서화되어야 합니다.

10.
클래스가 다른 클래스를 서브클래싱하고 그 동작이 대부분 해당 클래스에서 상속되는 경우 
해당 독스트링은 이를 언급하고 차이점을 요약해야 합니다. 

11.
서브클래스 메서드가 슈퍼클래스 메서드를 대체하고 
슈퍼클래스 메서드를 호출하지 않음을 나타내려면 "override"라는 동사를 사용하세요. 
하위 클래스 메서드가 자체 동작 외에도 상위 클래스 메서드를 호출함을 나타내려면 "extend"이라는 동사를 사용합니다.



12.
Note that most importantly, the """ that ends a multiline docstring should be on a line by itself:
	"""Return a foobang

	Optional plotz says to frobnicate the bizbaz first.
	"""

13.
For one liner docstrings, please keep the closing """ on the same line:
"""Return an ex-parrot."""

14.
여러 줄 독스트링은 한 줄 독스트링과 마찬가지로 요약 줄, 빈 줄, 더 자세한 설명으로 구성됩니다. 
요약이 한 줄에 들어가고 빈 줄로 독스트링의 나머지 부분과 분리되는 것이 중요합니다. 

	def complex(real=0.0, imag=0.0):
	    """Form a complex number.

	    Keyword arguments:
	    real -- the real part (default 0.0)
	    imag -- the imaginary part (default 0.0)
	    """
	    if imag == 0.0 and real == 0.0:
		return complex_zero
	    ... 
	
==== 후행 쉼표 ====	

1.
후행 쉼표는 일반적으로 선택 사항이지만 한 요소의 튜플을 만들 때 필수입니다. 
명확성을 위해 후자를 (기술적으로 중복되는) 괄호로 묶는 것이 좋습니다.

	# Correct:
		FILES = ('setup.cfg',)

	# Wrong:
		FILES = 'setup.cfg',

2.
후행 쉼표가 중복되는 경우 버전 제어 시스템을 사용할 때, 값 목록, 인수 또는
 가져온 항목이 시간이 지남에 따라 확장될 것으로 예상되는 경우 종종 도움이 됩니다. 
 패턴은 각 값(등)을 한 줄에 단독으로 입력하고 항상 뒤에 쉼표를 추가하고 
 다음 줄에 닫는 괄호/대괄호/중괄호를 추가하는 것입니다. 
 그러나 닫는 구분 기호와 같은 줄에 후행 쉼표를 두는 것은 의미가 없습니다(위의 단일 튜플의 경우는 제외).

	# Correct:
		FILES = [
		    'setup.cfg',
		    'tox.ini',
		    ]
		initialize(FILES,
			   error=True,
			   )
		   
	# Wrong:
		FILES = ['setup.cfg', 'tox.ini',]
		initialize(FILES, error=True,)


    
    
==== 기타==== 
 
1. 
==을 사용하여 부울 값을 True 또는 False와 비교하지 마세요.

	# Correct:
		if greeting:

	# Wrong:
		if greeting == True:

	더 나쁜:

	# Wrong:
	
	if greeting is True:

2. 
객체 유형 비교에서는 유형을 직접 비교하는 대신 항상 isinstance()를 사용해야 합니다.

	# Correct:
		if isinstance(obj, int):
		
	# Wrong:
		if type(obj) is type(1):

3.
문자열 슬라이싱 대신 ''.startswith() 및 ''.endswith() 를 사용하여 접두사 또는 접미사를 확인하세요.
startwith() 및 endwith()는 더 깔끔하고 오류 발생 가능성이 적습니다.

	# Correct:
		if foo.startswith('bar'):
		
	# Wrong:
		if foo[:3] == 'bar':

4.
Comparisons to singletons like None should always be done with "is" or "is not", never the equality operators "==".


5.
람다 식을 식별자에 직접 바인딩하는 할당 문 대신 
항상 def 문을 사용하세요.

	# Correct:
		def f(x): return 2*x
		
	# Wrong:
		f = lambda x: 2*x
첫 번째 형식은 결과 함수 객체의 이름이 일반 '<lambda>' 대신 구체적으로 'f'임을 의미합니다. 
이는 일반적으로 역추적 및 문자열 표현에 더 유용합니다. 
대입문을 사용하면 람다 식이 명시적 def 문에 비해 제공할 수 있는 유일한 이점(즉, 더 큰 표현식 내에 포함될 수 있음)이 제거됩니다. ??????????????


==== 인코딩 ====

코드는 항상 UTF-8을 사용해야 하며 인코딩 선언이 있어서는 안 됩니다.
	표준 라이브러리에서는 UTF-8이 아닌 인코딩을 테스트 목적으로만 사용해야 합니다. 비ASCII 문자는 되도록이면 장소와 사람 이름을 표시할 때만 사용하십시오

Python 표준 라이브러리의 모든 식별자는 ASCII 전용 식별자를 사용해야 하며, 가능할 때마다 영어 단어를 사용해야 합니다



