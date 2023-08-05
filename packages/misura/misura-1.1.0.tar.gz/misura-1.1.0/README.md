![PyPI](https://img.shields.io/pypi/v/misura)
![GitHub last commit](https://img.shields.io/github/last-commit/diantonioandrea/misura)
![GitHub Release Date](https://img.shields.io/github/release-date/diantonioandrea/misura)

# misura

Python library for easy unit handling and conversion for scientific & engineering applications.  

**misura** is a Python library designed to simplify the *handling of units of measure* for scientific and engineering applications. It provides a unified interface for *dealing with different units and their conversions*, allowing for quick and accurate calculations without the need for complex manual conversions.  

Make sure to take a look at the [documentation](https://github.com/diantonioandrea/misura/blob/main/docs/docs.md), at the [contributing guidelines](https://github.com/diantonioandrea/misura/blob/main/.github/CONTRIBUTING.md) and at the [examples](#examples).

### Features

* Mathematical and logic perations between units: [Example](#mathematical-operations), [example](#comparisons).
* Manual conversions: [Example](#manual-and-automatic-conversion).
* Automatic conversions on operations: [Example](#manual-and-automatic-conversion).
* Large compatibility with other libraries: [Example](#working-with-other-libraries).
* Custom exceptions: [Example](#comparisons).

## Installation

### Installing misura

**misura** can be installed from [PyPI](https://pypi.org) by:

	python3 -m pip install --upgrade misura

### Importing misura

**misura** can be imported by:

	import misura

## Examples

These are some examples of operations between units of measure.  
Note that, by enabling `misura.style.unitHighlighting`, **misura** uses colorama to highlight units of measure. by disabling it, the output is in the form of `num [unit]`

### Creating a number with unit of measure:

``` python
from misura import unit

num = unit(2, "m s-1")

print(num)
```

The output is:

	2 m / s

### Mathematical operations

``` python
from misura import unit

num1 = unit(2, "m s-1")
num2 = unit(4, "m s-1")
num3 = unit(2, "s")

print(num1 + num2)
print(num1 * num2)
print(num1 / num3)
print(num3 ** 2)
```

The output is:

	6 m / s
	8 m(2) / s(2)
	1.0 m / s(2)
	4 s(2)

### Working with other libraries

``` python
from misura import unit, convert
from decimal import Decimal, getcontext
import numpy

getcontext().prec = 40

arr1 = numpy.array([unit(2, "m"), unit(50, "m s-1"), unit(2, "kg")])
arr2 = unit(numpy.array([1, 2, 3]), "J")
num2 = unit(numpy.sqrt(Decimal(5)), "kg")

print(arr1 * 3)
print(arr2 ** 2)
print(num2)
```

The output is:

	[6 m 150 m / s 6 kg]
	[1 4 9] J(2)
	2.236067977499789696409173668731276235441 kg

Unit highlighting helps distinguish between different numbers.

### Manual and automatic conversion

``` python
from misura import unit, convert

num1 = unit(2, "m2")
num2 = unit(4, "kg")
num3 = unit(400, "m s-1")

print(convert(num1, "cm2"))
print(num2 + unit(5, "g"))
print(convert(num3, "km", partial=True))
```

The output is:

	20000.0 cm(2)
	4.005 kg
	0.4 km / s

### Comparisons

``` python
from misura import unit

num1 = unit(2, "m s-1")
num2 = unit(4, "m s-1")
num3 = unit(2, "s")

print(num1 > num2)
print(num2 < 6)
print(num1 > num3)
```

The output is:

	False
	True
	misura.units.SymbolError: unsupported operand symbol(s) for >: 'm s-1.0' and 's'

### Unary operators and functions

``` python
from misura import unit
from misura import style
from math import trunc

style.unitHighlighting = False

num1 = unit(2, "m s-1")
num2 = unit(4.5, "m s-1")
num3 = unit(-2, "s")

print(-num1)
print(trunc(num2))
print(abs(num3))
```

The output is:

	-2 [m / s]
	4 [m / s]
	2 [s]

### Formatting

``` python
from misura import unit

num1 = unit(2000, "m s-1")

print("Exponential notation: {:.2e}".format(num1))
```

The output is:

	Exponential notation: 2.00e+00 m / s