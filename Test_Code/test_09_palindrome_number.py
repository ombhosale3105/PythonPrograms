import importlib.util

spec = importlib.util.spec_from_file_location(
    "09_palindrome_number", "Code/09_palindrome_number.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_number(121) is True
assert module.is_palindrome_number(1331) is True
assert module.is_palindrome_number(123) is False
assert module.is_palindrome_number(0) is True

print("All test cases passed.")
