
def check_required_keys(keys: tuple, element: dict):
    return all(element.get(key) for key in keys)


def remove_null_order_details(order):
    new_list = []
    for detail in order['detail']:
        new_dict = {
            key: value for key, value in detail.items() if value is not None
        }
        new_list.append(new_dict)
    order.update({'detail': new_list})
    return order
