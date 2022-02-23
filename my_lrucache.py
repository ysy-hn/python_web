import time
from collections import OrderedDict


class LRUCacheDict:
    def __init__(self, max_size=1024, expiration=60):
        """最大容量为1024个key， 每个key的有效期为60s"""
        self.max_size = max_size  # 容量
        self.expiration = expiration  # 时效

        self._cache = {}  # 缓存
        self._access_records = OrderedDict()  # 记录访问时间
        self._expire_records = OrderedDict()  # 记录失效时间

    def __setitem__(self, key, value):
        now = int(time.time())
        self.__delete__(key)

        self._cache[key] = value
        self._access_records[key] = now
        self._expire_records[key] = now + self.expiration

        self.cleanup()

    def __getitem__(self, key):
        now = int(time.time())
        del self._access_records[key]
        self._access_records[key] = now
        self.cleanup()

        return self._cache[key]

    def __contains__(self, key):
        self.cleanup()
        return key in self._cache

    def __delete__(self, key):
        if key in self._cache:
            del self._cache[key]
            del self._expire_records[key]
            del self._access_records[key]

    def cleanup(self):
        """去掉无效（过期或超出存储大小）的缓存"""
        if self.expiration is None:
            return None

        pending_delete_keys = []  # 待定删除的键
        now = int(time.time())
        for k, v in self._expire_records.items():  # 删除已经过期的缓存
            if v < now:
                pending_delete_keys.append(k)

        for del_k in pending_delete_keys:
            self.__delete__(del_k)

        while (len(self._cache) > self.max_size):
            # 如果数据量大于max_size，则删除掉最旧的缓存
            for k in self._access_records:
                self.__delete__(k)
                break


if __name__ == '__main__':
    cache_dict = LRUCacheDict(max_size=2, expiration=10)
    cache_dict['name'] = 'the5file'
    cache_dict['age'] = 30
    cache_dict['addr'] = 'beijng'
    print('name' in cache_dict)  # 输出False， 容量为2， 第一个key被删除
    print('age' in cache_dict)  # 输出True

    time.sleep(1)

    print('age' in cache_dict)  # 输出False， 缓存失效
