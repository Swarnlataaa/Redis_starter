import redis

r = redis.Redis(host='localhost', port=6379)
r.bgsave()  # Create an RDB snapshot
r.bgrewriteaof()  # Rewrite the AOF log
