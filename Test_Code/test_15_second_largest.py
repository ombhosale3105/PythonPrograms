import importlib.util

spec = importlib.util.spec_from_file_location(
    "15_second_largest", "Code/15_second_largest.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.second_largest([10, 20, 30, 40]) == 30
assert module.second_largest([5, 1, 8, 3]) == 5
assert module.second_largest([10, 10, 5, 3]) == 5
assert module.second_largest([10]) is None

print("All test cases passed.")
