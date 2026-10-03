import importlib.util

spec = importlib.util.spec_from_file_location(
    "12_reverse_string", "Code/12_reverse_string.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_string("hello") == "olleh"
assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("12345") == "54321"
assert module.reverse_string("") == ""

print("All test cases passed.")
