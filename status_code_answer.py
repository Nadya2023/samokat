#Надежда Тирская, 8-а Меркурий - дипломный проект
import sender_stand_request
import data

def test_get_orders_nambers ():
    resp_number = sender_stand_request.post_orders(data.body) # передаем в функцию тело из даты
    track = {"t": resp_number.json()["track"]} # достаем трек из прошлой переменной
    order_response = sender_stand_request.get_orders_number(track) # запрос с новым номером заказа
    assert order_response.status_code == 200
