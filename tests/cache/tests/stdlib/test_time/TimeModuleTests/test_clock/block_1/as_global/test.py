import time
start = time.clock()
time.sleep(1)
end = time.clock()
diff = end - start - 0
print(type(diff))
print(diff < 0.1)
print('Done.')
