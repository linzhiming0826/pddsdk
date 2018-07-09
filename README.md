pddsdk
======

Python3

pddsdk is an open source api for pingduoduo.

**Installation**
```linux
pip install pddsdk
```

**Simple uses**
```python
from pddsdk.client import Client

client_id = '123456'

client_secret = '123456'

params = {
    'sort_type': 0,
    'type': 'pdd.ddk.goods.search'}

request = Client(client_id, client_secret)

print(request.call(params))
```

```python
from pddsdk.ddk_goods_search import DdkGoodsSearch

client_id = '123456'

client_secret = '123456'

params = {'sort_type': 0}

r = DdkGoodsSearch(client_id, client_secret).call(params)

print(r)
```