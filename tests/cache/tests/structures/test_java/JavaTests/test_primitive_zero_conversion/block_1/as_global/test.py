from com.example import MyObject

obj = MyObject()

result = obj.method(0)
print('Result is', result)

result = obj.method(0.0)
print('Result is', result)

result = obj.method(False)
print('Result is', result)

print("Done.")
