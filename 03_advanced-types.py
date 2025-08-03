# Python typing module provides more advanced type Hints, such as List, Tuple, Dict, and Union.

# You can import List, Tuple, Dict types from the typing module like this:

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person: Tuple[str, int] = ("Sanju", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Rishi": 22, "Virat": 18}

# Union types for variables that can  hold multiple types

identifier: Union[int, str] = "24AI048"
identifier = 123456 # Also Valid