
ALL_FILES=\
	python/org/Python.class \
	python/org/python/PyObject.class \
	python/org/python/Callable.class \
	python/org/python/Function.class \
	python/org/python/InstanceMethod.class \
	python/org/python/Iterable.class \
	python/org/python/StaticMethod.class \
	python/org/python/PyConstructor.class \
	python/org/python/exceptions/ArithmeticError.class \
	python/org/python/exceptions/AssertionError.class \
	python/org/python/exceptions/AttributeError.class \
	python/org/python/exceptions/BaseException.class \
	python/org/python/exceptions/BufferError.class \
	python/org/python/exceptions/EnvironmentError.class \
	python/org/python/exceptions/EOFError.class \
	python/org/python/exceptions/FloatingPointError.class \
	python/org/python/exceptions/ImportError.class \
	python/org/python/exceptions/IndentationError.class \
	python/org/python/exceptions/IndexError.class \
	python/org/python/exceptions/IOError.class \
	python/org/python/exceptions/KeyError.class \
	python/org/python/exceptions/LookupError.class \
	python/org/python/exceptions/MemoryError.class \
	python/org/python/exceptions/NameError.class \
	python/org/python/exceptions/NotImplementedError.class \
	python/org/python/exceptions/OSError.class \
	python/org/python/exceptions/OverflowError.class \
	python/org/python/exceptions/PyException.class \
	python/org/python/exceptions/ReferenceError.class \
	python/org/python/exceptions/RuntimeError.class \
	python/org/python/exceptions/StandardError.class \
	python/org/python/exceptions/StopIteration.class \
	python/org/python/exceptions/SyntaxError.class \
	python/org/python/exceptions/SystemError.class \
	python/org/python/exceptions/TabError.class \
	python/org/python/exceptions/TypeError.class \
	python/org/python/exceptions/UnboundLocalError.class \
	python/org/python/exceptions/UnicodeDecodeError.class \
	python/org/python/exceptions/UnicodeEncodeError.class \
	python/org/python/exceptions/UnicodeError.class \
	python/org/python/exceptions/UnicodeTranslateError.class \
	python/org/python/exceptions/ValueError.class \
	python/org/python/exceptions/ZeroDivisionError.class

.PHONY: all clean

all: python.jar

clean:
	rm -rf python.jar
	find python -name "*.class" -exec rm {} \;

python.jar: $(ALL_FILES)
	cd python && jar -cf ../$@ $(subst python/org,org,$(ALL_FILES))

%.class: %.java
	javac -classpath python $<
