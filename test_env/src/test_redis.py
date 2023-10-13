import redis

r = redis.Redis(host="redis",port=6379)

r.set("hoge","moge")

print(r.get("hoge"))