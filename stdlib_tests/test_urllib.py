from urllib.parse import urlparse

o = urlparse('http://127.0.0.1:8000')
print(o.port)
