
ALL_FILES=\
	python/org/Python.class \
	python/org/python/Callable.class \
	python/org/python/InstanceMethod.class \
	python/org/python/Iterable.class \
	python/org/python/StaticMethod.class \
	python/org/python/Constructor.class \
	python/org/python/exceptions/ArithmeticError.class \
	python/org/python/exceptions/AssertionError.class \
	python/org/python/exceptions/AttributeError.class \
	python/org/python/exceptions/BaseException.class \
	python/org/python/exceptions/BlockingIOError.java \
	python/org/python/exceptions/BrokenPipeError.java \
	python/org/python/exceptions/BufferError.class \
	python/org/python/exceptions/BytesWarning.java \
	python/org/python/exceptions/ChildProcessError.java \
	python/org/python/exceptions/ConnectionAbortedError.java \
	python/org/python/exceptions/ConnectionError.java \
	python/org/python/exceptions/ConnectionRefusedError.java \
	python/org/python/exceptions/ConnectionResetError.java \
	python/org/python/exceptions/DeprecationWarning.java \
	python/org/python/exceptions/EOFError.class \
	python/org/python/exceptions/Exception.class \
	python/org/python/exceptions/FileExistsError.java \
	python/org/python/exceptions/FileNotFoundError.java \
	python/org/python/exceptions/FloatingPointError.class \
	python/org/python/exceptions/FutureWarning.java \
	python/org/python/exceptions/GeneratorExit.java \
	python/org/python/exceptions/ImportError.class \
	python/org/python/exceptions/ImportWarning.java \
	python/org/python/exceptions/IndentationError.class \
	python/org/python/exceptions/IndexError.class \
	python/org/python/exceptions/InterruptedError.java \
	python/org/python/exceptions/IsADirectoryError.java \
	python/org/python/exceptions/KeyboardInterrupt.java \
	python/org/python/exceptions/KeyError.class \
	python/org/python/exceptions/LookupError.class \
	python/org/python/exceptions/MemoryError.class \
	python/org/python/exceptions/NameError.class \
	python/org/python/exceptions/NotADirectoryError.java \
	python/org/python/exceptions/NotImplementedError.class \
	python/org/python/exceptions/OSError.class \
	python/org/python/exceptions/OverflowError.class \
	python/org/python/exceptions/PendingDeprecationWarning.java \
	python/org/python/exceptions/PermissionError.java \
	python/org/python/exceptions/ProcessLookupError.java \
	python/org/python/exceptions/ReferenceError.class \
	python/org/python/exceptions/ResourceWarning.java \
	python/org/python/exceptions/RuntimeError.class \
	python/org/python/exceptions/RuntimeWarning.java \
	python/org/python/exceptions/StandardError.class \
	python/org/python/exceptions/StopIteration.class \
	python/org/python/exceptions/SyntaxError.class \
	python/org/python/exceptions/SyntaxWarning.java \
	python/org/python/exceptions/SystemError.class \
	python/org/python/exceptions/SystemExit.java \
	python/org/python/exceptions/TabError.class \
	python/org/python/exceptions/TimeoutError.java \
	python/org/python/exceptions/TypeError.class \
	python/org/python/exceptions/UnboundLocalError.class \
	python/org/python/exceptions/UnicodeDecodeError.class \
	python/org/python/exceptions/UnicodeEncodeError.class \
	python/org/python/exceptions/UnicodeError.class \
	python/org/python/exceptions/UnicodeTranslateError.class \
	python/org/python/exceptions/UnicodeWarning.java \
	python/org/python/exceptions/UserWarning.java \
	python/org/python/exceptions/ValueError.class \
	python/org/python/exceptions/Warning.java \
	python/org/python/exceptions/ZeroDivisionError.class \
	python/org/python/types/Bool.class \
	python/org/python/types/ByteArray.class \
	python/org/python/types/Bytes.class \
	python/org/python/types/Class.class \
	python/org/python/types/Complex.class \
	python/org/python/types/ContextManager.class \
	python/org/python/types/Dict.class \
	python/org/python/types/DictView.class \
	python/org/python/types/Ellipsis.class \
	python/org/python/types/Float.class \
	python/org/python/types/FrozenSet.class \
	python/org/python/types/Function.class \
	python/org/python/types/Int.class \
	python/org/python/types/List.class \
	python/org/python/types/MemoryView.class \
	python/org/python/types/Method.class \
	python/org/python/types/Module.class \
	python/org/python/types/NotImplemented.class \
	python/org/python/types/Null.class \
	python/org/python/types/Object.class \
	python/org/python/types/Range.class \
	python/org/python/types/Set.class \
	python/org/python/types/Str.class \
	python/org/python/types/Tuple.class \
	python/org/python/types/Type.class \

.PHONY: all clean

all: python.jar

clean:
	rm -rf python.jar
	find python -name "*.class" -exec rm {} \;

python.jar: $(ALL_FILES)
	cd python && jar -cf ../$@ $(subst python/org,org,$(ALL_FILES))

%.class: %.java
	javac  -Xlint:unchecked -classpath python $<
