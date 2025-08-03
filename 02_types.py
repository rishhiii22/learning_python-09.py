# Type hint are added using a colon(:) sybtax for variables and the -> syntax for function return types.

# Variable type Hint
age: int = 5 

# Function type hints

def greeting(name: str) -> str:
    return f"Hello, {name}!"

# Usage 

print(greeting("Alice"))

# Output: Hello, Alice