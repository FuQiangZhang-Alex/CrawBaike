
from lxml import etree
from urllib3 import HTTPConnectionPool
from io import BytesIO


class CrawlSpider:
    def __init__(self, host='', path='', parameters={}, maxsize=1, method='GET', request_headers=()):
        self.host = host
        self.path = path
        self.parameters = parameters
        self.method = method
        self.maxsize = maxsize
        self.request_hearders = request_headers
        self.pool = HTTPConnectionPool(self.host, maxsize=1)

    def extract(self, callback=None):
        res = self.pool.request(method=self.method, url=self.path)
        parser = etree.HTMLParser()
        tree = etree.parse(BytesIO(res.data), parser=parser)
        return callback(tree)
        pass
