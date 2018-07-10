from pddsdk.client import Client


class DdkGoodsZsUnitUrlGen(Client):
    def __init__(self, client_id, client_secret, url=None):
        '''init
        '''
        Client.__init__(self, client_id, client_secret,
                        'pdd.ddk.goods.zs.unit.url.gen', url)


if __name__ == '__main__':
    client_id = '123456'
    client_secret = '123456'
    source_url = 'https://mobile.yangkeduo.com/duo_theme_activity.html?themeId=1235&pid=123456&sign=1XBANTnNmUbAs27Q1Vl2aSZtV50SKWaL4F-LgFRjUcg%3D&duoduo_type=2'
    pid = '123456'
    params = {'pid': pid, 'source_url': source_url}
    r = DdkGoodsZsUnitUrlGen(client_id, client_secret).call(params)
    print(r)
