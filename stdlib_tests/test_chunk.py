import chunk
import io

fakeFile= io.BytesIO(b"some initial binary data: \x00\x01")
testChunk = chunk.Chunk(fakeFile)

print("Name = ", testChunk.getname())
print("Size = ", testChunk.getsize())
print("IsAtty = ", testChunk.isatty())
print("Read0 = ", testChunk.read(5))
print("Tell = ", testChunk.tell())
testChunk.skip()

