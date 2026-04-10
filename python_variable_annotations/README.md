# Python Variable Annotations

This project covers Python 3 type annotations, using the `typing` module for complex types.

## Requirements

- Python 3.9+
- All files use `#!/usr/bin/env python3`
- Code follows `pycodestyle` (2.5)

## Tasks

### 0. Basic annotations - add
**File:** `0-add.py`

Type-annotated function `add(a: float, b: float) -> float` that returns the sum of two floats.

### 1. Basic annotations - concat
**File:** `1-concat.py`

Type-annotated function `concat(str1: str, str2: str) -> str` that returns the concatenation of two strings.

### 2. Basic annotations - floor
**File:** `2-floor.py`

Type-annotated function `floor(n: float) -> int` that returns the floor of a float using `math.floor`.

### 3. Basic annotations - to string
**File:** `3-to_str.py`

Type-annotated function `to_str(n: float) -> str` that returns the string representation of a float.

### 4. Define variables
**File:** `4-define_variables.py`

Annotated module-level variables:
- `a: int = 1`
- `pi: float = 3.14`
- `i_understand_annotations: bool = True`
- `school: str = "Holberton"`

### 5. Complex types - list of floats
**File:** `5-sum_list.py`

Type-annotated function `sum_list(input_list: List[float]) -> float` that returns the sum of a list of floats.

### 6. Complex types - mixed list
**File:** `6-sum_mixed_list.py`

Type-annotated function `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float` that returns the sum of a mixed list of integers and floats.

### 7. Complex types - string and int/float to tuple
**File:** `7-to_kv.py`

Type-annotated function `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]` that returns a tuple where the second element is `v²` as a float.

### 8. Complex types - functions
**File:** `8-make_multiplier.py`

Type-annotated function `make_multiplier(multiplier: float) -> Callable[[float], float]` that returns a multiplier function.

### 9. Let's duck type an iterable object
**File:** `9-element_length.py`

Annotated function `element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]` that returns each element paired with its length.

## Author

Holberton School - Web Back End
