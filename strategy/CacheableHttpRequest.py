import requests
import sqlite3
from abc import ABC, abstractmethod

class CachingStrategy(ABC):
    
    @abstractmethod
    def __setitem__(self, key, item):
        pass
    
    @abstractmethod
    def __getitem__(self, key):
        pass
    
    @abstractmethod
    def __contains__(self, key):
        pass
    

class MemoryCache(CachingStrategy):

    def __init__(self):
      self._cache = {}
    
    def __setitem__(self, key, item):
        self._cache[key] = item
    
    def __getitem__(self, key):
        return self._cache[key]

    def __contains__(self, key):
        return key in self._cache


class SqlliteCache(CachingStrategy):

    def __init__(self):
        self._conn = sqlite3.connect(":memory:")
        self._init_dict_table()
    
    def _init_dict_table(self):
        cursor = self._conn.cursor()
        cursor.execute("CREATE TABLE dict (key VARCHAR PRIMARY KEY, value VARCHAR)")
        self._conn.commit()
        cursor.close()
    
    def __setitem__(self, key, item):
        cursor = self._conn.cursor()
        cursor.execute("INSERT INTO dict (key, value) VALUES (?, ?)", (key, item))
        self._conn.commit()
        cursor.close()
    
    def __getitem__(self, key):
        cursor = self._conn.cursor()
        cursor.execute("SELECT value FROM dict WHERE key = ?", (key,))
        record = cursor.fetchone()
        cursor.close()
        return record[0]

    def __contains__(self, key):
        cursor = self._conn.cursor()
        cursor.execute("SELECT value FROM dict WHERE key = ?", (key,))
        record = cursor.fetchone()
        cursor.close()
        return record is not None


class CacheableHttpRequester:

    def __init__(self, caching_strategy = MemoryCache()):
        self._cache = caching_strategy
    
    def request(self, url):
        if url in self._cache:
            print("item already in cache")
            return self._cache[url]
        else:
            print("item not in cache")
            req = requests.get(url)
            self._cache[url] = req.text
            return self._cache[url]


def main():
    for strategy in [MemoryCache(), SqlliteCache()]:
        http_requester = CacheableHttpRequester(caching_strategy=strategy)
        for _ in range(5):
            http_requester.request("http://news.ycombinator.com")


if __name__ == "__main__":
    main()
