from client import Client


class DdkThemePromUrlGenerate(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.theme.prom.url.generate', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'pid': '123456', 'theme_id_list': '[1235]'}
    r = DdkThemePromUrlGenerate(client_id, client_secret).call(params)
    print(r)
