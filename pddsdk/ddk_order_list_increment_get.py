from client import Client


class DdkOrderListIncrementGet(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.order.list.increment.get', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    params = {'start_update_time': 1531099393, 'end_update_time': 1531099429}
    r = DdkOrderListIncrementGet(client_id, client_secret).call(params)
    print(r)
