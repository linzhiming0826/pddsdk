from pddsdk.client import Client


class DdkGoodsPromotionUrlGenerate(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.goods.promotion.url.generate', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    p_id = '123456'
    params = {'p_id': p_id,
              'goods_id_list': '[2072723175]', 'generate_short_url': 'true'}
    r = DdkGoodsPromotionUrlGenerate(client_id, client_secret).call(params)
    print(r)
