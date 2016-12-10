from com.example import OuterClass

print("Outer class is", OuterClass)
print("Outer constant is", OuterClass.OUTER_CONSTANT)

print("Inner class is", OuterClass.InnerClass)
print("Inner constant is", OuterClass.InnerClass.INNER_CONSTANT)

print("Done.")
