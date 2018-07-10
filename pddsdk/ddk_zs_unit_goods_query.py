from client import Client


class DdkZsUnitGoodsQuery(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.zs.unit.goods.query', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'zs_duo_id': 11, 'page_size': 100}
    r = DdkZsUnitGoodsQuery(client_id, client_secret).call(params)
    print(r)
