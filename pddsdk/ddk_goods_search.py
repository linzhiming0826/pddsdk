from pddsdk.client import Client


class DdkGoodsSearch(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.goods.search', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'sort_type': 0}
    r = DdkGoodsSearch(client_id, client_secret).call(params)
    print(r)
