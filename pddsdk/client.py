import time
import hashlib
import requests


class Client:
    def __init__(self, client_id, client_secret, client_type=None, url=None):
        '''init
        '''
        self.client_id = client_id
        self.client_secret = client_secret
        self.client_type = client_type
        if url:
            self.url = url
        else:
            self.url = 'http://gw-api.pinduoduo.com/api/router'

    def _get_local_timestamp(self):
        '''get local timestamp
        '''
        return str(int(time.time()*1000))

    def _create_sign(self, params):
        '''create sign
        '''
        keys = sorted(params.keys())
        content = ''.join('%s%s' % (key, params[key]) for key in keys)
        content = ''.join([self.client_secret, content, self.client_secret])
        sign = hashlib.md5(content.encode()).hexdigest().upper()
        return sign

    def call(self, params=None):
        '''get api and return result
        '''
        data = {
            'client_id': self.client_id,
            'timestamp': self._get_local_timestamp()
        }
        if self.client_type:
            data['type'] = self.client_type
        if params:
            data = {**data, **params}
        data['sign'] = self._create_sign(data)
        r = requests.post(self.url, data)
        r.raise_for_status()
        return r.json()


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {
        'sort_type': 0,
        'type': 'pdd.ddk.goods.search'}
    request = Client(client_id, client_secret)
    print(request.call(params))
