import importlib.util

spec = importlib.util.spec_from_file_location(
    "03_pos_neg_zero", "Code/03_pos_neg_zero.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_number(10) == "Positive"
assert module.check_number(-10) == "Negative"
assert module.check_number(0) == "Zero"

print("All test cases passed.")
