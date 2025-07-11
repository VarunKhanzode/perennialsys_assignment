import time
from collections import defaultdict

class SimpleRateLimiter:
    def __init__(self, limit=10, window=60):
        self.limit = limit       
        self.window = window       
        self.requests = defaultdict(list) 

    def is_allowed(self, key):
        now = time.time()
        self.requests[key] = [t for t in self.requests[key] if now - t < self.window]
        if len(self.requests[key]) < self.limit:
            self.requests[key].append(now)
            return True
        return False

rate_limiter = SimpleRateLimiter()
