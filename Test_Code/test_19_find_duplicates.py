import importlib.util

spec = importlib.util.spec_from_file_location(
    "19_find_duplicates", "Code/19_find_duplicates.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]
assert module.find_duplicates([1, 1, 1, 2, 3]) == [1]
assert module.find_duplicates([1, 2, 3]) == []
assert module.find_duplicates([]) == []

print("All test cases passed.")
