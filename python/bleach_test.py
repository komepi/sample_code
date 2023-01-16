import bleach

b="test group<script>alert('test')</script><h2>test</h2>"

test = bleach.clean(b,tags=["h2"],strip=False)
print(test)
print(test.strip())