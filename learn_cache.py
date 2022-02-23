# import time
#
#
# CACHE = {}
#
# # def query(sql):
# #     try:
# #         result = CACHE[sql]
# #     except KeyError:
# #         time.sleep(1)
# #         result = 'execute %s' % sql
# #         CACHE[sql] = result
# #     return result
# # # 被动缓存，当有请求时才缓存数据，即第一次请求还需要执行，数据量大时，较慢。
#
# def query(sql):
#     result = CACHE.get(sql)
#     if not result:
#         time.sleep(1)
#         result = 'execute %s' % sql
#         CACHE[sql] = result
#     return result
# # 主动缓存，1、系统启动时，自动把所有接口刷一遍；2、在数据写入时同步更新或写入缓存。
#
# if __name__ == '__main__':
#     start = time.time()
#     query('SELECT * FROM blog_post')
#     print(time.time() - start)
#
#     start = time.time()
#     query('SELECT * FROM blog_post')
#     print(time.time() - start)
#
#
# # 缓存装饰器，重构缓存。
# from functools import wraps
# import time
#
#
# CACHE = {}
#
# def cache_it(func):
#     @wraps(func)
#     def inner(*args, **kwargs):
#         key = repr(*args, **kwargs)  # repr():将对象转化为供解释器读取的string形式。。
#         try:
#             result = CACHE[key]
#         except KeyError:
#             result = func(*args, **kwargs)
#             CACHE[key] = result
#         return result
#     return inner
#
# @cache_it
# def query(sql):
#     time.sleep(1)
#     result = 'execute %s' % sql
#     return result
#
# if __name__ == '__main__':
#     start = time.time()
#     query('SELECT * FROM blog_post')
#     print(time.time() - start)
#
#     start = time.time()
#     query('SELECT * FROM blog_post')
#     print(time.time() - start)


from my_lrucache import LRUCacheDict
from functools import wraps
import time


CACHE = {}


def cache_it(max_size=1024, expiration=60):
    CACHE = LRUCacheDict(max_size=max_size, expiration=expiration)

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            key = repr(*args, **kwargs)
            try:
                result = CACHE[key]
            except KeyError:
                result = func(*args, **kwargs)
                CACHE[key] = result
            return result
        return inner
    return wrapper


@cache_it(max_size=10, expiration=3)
def query(sql):
    time.sleep(1)
    result = 'execute %s' % sql
    return result


if __name__ == '__main__':
    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)

    start = time.time()
    query('SELECT * FROM blog_post')
    print(time.time() - start)

