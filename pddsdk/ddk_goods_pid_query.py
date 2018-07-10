from pddsdk.client import Client


class DdkGoodsPidQuery(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.goods.pid.query', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    r = DdkGoodsPidQuery(client_id, client_secret).call()
    print(r)
