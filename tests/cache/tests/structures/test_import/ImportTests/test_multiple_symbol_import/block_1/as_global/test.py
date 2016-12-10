from example import some_method, other_method

print("Call some method...")
some_method()

print("Call another method...")
other_method()

try:
    print("But this will fail...")
    third_method()
except NameError:
    print("Which it does.")

print("Done.")
