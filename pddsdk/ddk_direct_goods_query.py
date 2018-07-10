from client import Client


class DdkDirectGoodsQuery(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.direct.goods.query', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    r = DdkDirectGoodsQuery(client_id, client_secret).call()
    print(r)
