import importlib.util

spec = importlib.util.spec_from_file_location(
    "20_word_frequency", "Code/20_word_frequency.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello world hello") == {"hello": 2, "world": 1}
assert module.word_frequency("Python is easy and Python is powerful") == {"python": 2, "is": 2, "easy": 1, "and": 1, "powerful": 1}
assert module.word_frequency("") == {}
assert module.word_frequency("Hello, hello!") == {"hello": 2}

print("All test cases passed.")
