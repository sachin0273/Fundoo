import redis

r = redis.Redis("localhost")


def Set(username, token):
    """

    :param username: saving token
    :param token:this our actual token
    :return:in this function we save token in redis
    """
    r.set(username, token)


r


def Get(username):
    """

    :param username: key for get token
    :return:this function used for get token from redis

    """
    return r.get(username)


def Del(username):
    """

    :param username: kye for delete token
    :return: this function used for delete token from redis

    """
    r.delete(username)


def All_Delete():
    """

    :return: this function used for delete all token from redis

    """
    r.flushall()


def push(key, value):
    r.lpush(key, value)


def getrange(key):
    t = r.lrange(key, 0, -1)
    return t


# elements = r.lrange("7", 0, -1)
# print(elements)
