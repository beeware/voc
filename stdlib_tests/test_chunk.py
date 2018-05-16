import chunk


class fake_file():
    def read(self, n=0):
        return b"some initial binary data:"


testChunk = chunk.Chunk(fake_file())

print("Name = ", testChunk.getname())
print("Size = ", testChunk.getsize())
print("IsAtty = ", testChunk.isatty())
print("Read0 = ", testChunk.read(5))
print("Tell = ", testChunk.tell())
