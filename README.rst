pddsdk
======

pddsdk is an open source api for pingduoduo.

**Installation**

.. code:: bash

    pip install pddsdk

**Simple uses**

.. code:: python

    from pddsdk.client import Client

    client_id = '123456'

    client_secret = '123456'

    params = {
        'sort_type': 0,
        'type': 'pdd.ddk.goods.search'}

    r = Client(client_id, client_secret).call(params)

    print(r)


.. code:: python

    from pddsdk.ddk_goods_search import DdkGoodsSearch

    client_id = '123456'

    client_secret = '123456'

    params = {'sort_type': 0}

    r = DdkGoodsSearch(client_id, client_secret).call(params)

    print(r)

