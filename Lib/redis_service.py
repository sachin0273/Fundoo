import redis


redis_object = redis.Redis("localhost")


def Set(username, token):
    """

    :param username: saving token
    :param token:this our actual token
    :return:in this function we save token in redis
    """
    try:
        redis_object.set(username, token)
    except Exception:
        return False


def Get(username):
    """

    :param username: key for get token
    :return:this function used for get token from redis

    """
    try:
        return redis_object.get(username)
    except Exception:
        return False


def Del(username):
    """

    :param username: kye for delete token
    :return: this function used for delete token from redis

    """
    try:

        redis_object.delete(username)

    except Exception:
        return False


def All_Delete():
    """

    :return: this function used for delete all token from redis

    """
    try:
        redis_object.flushall()
    except Exception:
        return False


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.connect = self.connect()

    def connect(self):
        self.redis_obj = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

        return self.redis_obj

    def set(self, key, value):
        self.redis_obj.set(key, value)

    def get(self, key):
        return self.redis_obj.get(key)

    def delete(self, key):
        self.redis_obj.delete(key)


cache_obj = Cache()

