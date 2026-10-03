import importlib.util

spec = importlib.util.spec_from_file_location(
    "05_fibonacci_series", "Code/05_fibonacci_series.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.fibonacci_series(0) == []
assert module.fibonacci_series(1) == [0]
assert module.fibonacci_series(5) == [0, 1, 1, 2, 3]
assert module.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]

print("All test cases passed.")
