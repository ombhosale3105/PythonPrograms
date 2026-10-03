import importlib.util

spec = importlib.util.spec_from_file_location(
    "02_largest_of_three", "Code/02_largest_of_three.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(10, 20, 30) == 30
assert module.largest_of_three(50, 20, 10) == 50
assert module.largest_of_three(10, 40, 25) == 40
assert module.largest_of_three(-5, -2, -10) == -2

print("All test cases passed.")
