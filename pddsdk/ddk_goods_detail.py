from client import Client


class DdkGoodsDetail(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.goods.detail', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'goods_id_list': '[785266126]'}
    r = DdkGoodsDetail(client_id, client_secret).call(params)
    print(r)
