# AI Coding Agent Instructions

## Project Overview
This is a Python assignment focusing on object-oriented programming fundamentals. The project contains a `Rectangle` class that demonstrates:
- Class initialization with type hints
- Iterator protocol implementation (`__iter__` magic method)
- Yielding structured data (dictionaries) during iteration

## Key Implementation Details

### Rectangle Class Architecture
The `Rectangle` class in [rectangle.py](../rectangle.py) implements a simple geometric object with two core responsibilities:
1. **Data Storage**: Store `length` and `width` as instance attributes (must be `int` type)
2. **Iteration Protocol**: Yield length and width as separate dictionary objects in sequence

### Critical Bug to Fix
The current implementation has **name mangling issues**:
- `_init_` should be `__init__` (double underscore prefix/suffix for magic methods)
- `_iter_` should be `__iter__` (same issue)

Using single underscores breaks the iterator protocol - Python won't recognize these as magic methods.

### Expected Behavior
When iterating over a Rectangle instance, the output should be:
```python
rect = Rectangle(10, 5)
for attribute in rect:
    print(attribute)
# Output:
# {'length': 10}
# {'width': 5}
```

## Development Patterns

### Type Hints
The codebase uses type hints for clarity:
- Function parameters: `length: int`, `width: int`
- Use this pattern consistently for all new methods or modifications

### Iteration Implementation
When implementing `__iter__`, always:
1. Use `yield` (not `return`) to create a generator
2. Yield in the order specified by requirements
3. Return data as dictionaries with descriptive keys

## Common Issues to Watch For
1. **Magic Method Names**: Always use double underscores `__method__` for Python magic methods
2. **Unused Imports**: Current code imports `length_hint` and `width` from standard library but doesn't use them - remove unused imports
3. **Indentation**: Maintain consistent 4-space indentation (Python PEP 8)

## Testing Strategy
Test the Rectangle class by:
1. Creating an instance: `rect = Rectangle(10, 5)`
2. Iterating and collecting output
3. Verifying each yielded value matches the expected dictionary format
4. Validating only two iterations occur (length, then width)

## File References
- **Main Implementation**: [rectangle.py](../rectangle.py) - Contains the Rectangle class
- **Debug Configuration**: [.vscode/launch.json](.vscode/launch.json) - Python debugger setup available
