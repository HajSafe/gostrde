
import requests
from threading import Thread,local


def usdt():
    return requests.post('https://ramzarz.news//wp-admin/admin-ajax.php',data={'action':'usdtPrice_ajax','price':'usdt'}).content.decode('utf-8')