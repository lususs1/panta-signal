import unittest
from panta_signal import upstream_path, validate

class Boundaries(unittest.TestCase):
    def test_read_only(self):
        for path in ['/api/claim', '/api/markets/create', '/api/markets/../claim', '/api/wallets/x']:
            with self.assertRaises(ValueError): upstream_path(path, {})
    def test_query(self):
        self.assertEqual(upstream_path('/api/markets', {'limit':['20'], 'category':['crypto']}), '/markets/?limit=20&category=crypto')
        for query in [{'limit':['51']}, {'wallet':['x']}, {'limit':['1','2']}]:
            with self.assertRaises(ValueError): upstream_path('/api/markets', query)
    def test_schema(self):
        validate({'items':[{'marketId':'test-1','title':'Example'}]})
        for payload in [{}, {'items':[{'marketId':'../claim'}]}, {'items':[{'marketId':'a','title':[]}]}]:
            with self.assertRaises(ValueError): validate(payload)

if __name__ == '__main__': unittest.main()
