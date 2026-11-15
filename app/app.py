import os
import socket
import redis
from flask import Flask, jsonify

app = Flask(__name__)

# قراءة إعدادات الاتصال من متغيرات البيئة (Linux Environment Variables)
redis_host = os.getenv("REDIS_HOST", "redis-db")
redis_port = int(os.getenv("REDIS_PORT", 6379))
cache = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def index():
    try:
        visits = cache.incr("hits")
    except redis.exceptions.ConnectionError:
        visits = "Redis Connection Error!"
    
    return jsonify({
        "status": "running",
        "container_hostname": socket.gethostname(),
        "total_visits": visits
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
