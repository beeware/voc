#placeholder while list()s etc aren't fully implemented
class ListLike:
    x = [3.14, 2.17, 1.0]
    index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index > len(self.x):
            raise StopIteration
        return self.x[self.index]

def testish(x):
    return x > 1

print(filter(testish, ListLike()))
mylist = ListLike()
print(filter(testish, mylist).__next__())
print(filter(testish, mylist).__next__())
print(filter(testish, mylist).__next__())
try:
    print(filter(testish, mylist).__next__())
except StopIteration:
    pass
