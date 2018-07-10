from pddsdk.client import Client


class DdkGoodsPidGenerate(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.goods.pid.generate', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'number': 1, 'p_id_name_list': '["web"]'}
    r = DdkGoodsPidGenerate(client_id, client_secret).call(params)
    print(r)
