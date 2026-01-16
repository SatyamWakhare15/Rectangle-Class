# Rectangle-Class
Python trainee assignment implementing an iterable Rectangle class with custom __init__ and __iter__ methods


# Django Trainee Assignment

A Python programming assignment focused on implementing custom classes with iterator functionality.

## Overview
This repository contains a [Rectangle](cci:2://file:///c:/Users/Admin/Desktop/Assignment/Django_Trainee_Assignment/rectangle.py:7:0-26:35) class implementation that demonstrates:
- Object-oriented programming principles
- Python's iterator protocol
- Type hints and documentation best practices

## Features
- **Custom Initialization**: Rectangle instances require `length` and `width` (both integers)
- **Iterable Interface**: Implements [__iter__()](cci:1://file:///c:/Users/Admin/Desktop/Assignment/Django_Trainee_Assignment/rectangle.py:16:4-26:35) to allow iteration over rectangle attributes
- **Dictionary Output**: Returns attributes as dictionaries: `{'length': value}` and `{'width': value}`

## Usage
```python
rect = Rectangle(10, 5)

for attribute in rect:
    print(attribute)
# Output:
# {'length': 10}
# {'width': 5}
