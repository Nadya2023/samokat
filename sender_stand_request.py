import requests
import configuration
import data



# Создаем заказ
def post_orders(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body_order)


#Получаем заказ по номеру
def get_orders_number(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_NUMBER, params=track)


