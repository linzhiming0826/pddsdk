from pddsdk.client import Client


class DdkRpPromUrlGenerate(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.rp.prom.url.generate', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'p_id_list': '["123456"]'}
    r = DdkRpPromUrlGenerate(client_id, client_secret).call(params)
    print(r)
