def fake_sizes():
    return (
        {'name': 'Small', 'price': 3.5},
        {'name': 'Medium', 'price': 6.5},
        {'name': 'Large', 'price': 11},
        {'name': 'Extra large', 'price': 18},
        {'name': 'Jumbo', 'price': 30}
    )


def fake_beverages():
    return (
        {'name': 'Water 1L', 'price': 0.75},
        {'name': 'Inca Kola 1.25L', 'price': 1.10},
        {'name': 'Sprite 1L', 'price': 1.30},
        {'name': 'Coca Cola 1L', 'price': 1.30},
        {'name': 'Orange Juice 1L', 'price': 1},
    )


def fake_ingredients():
    return (
        {'name': 'Cheese', 'price': 0.75},
        {'name': 'Mozzarella', 'price': 0.4},
        {'name': 'Tomato Sauce', 'price': 0.25},
        {'name': 'Red Peppers', 'price': 0.8},
        {'name': 'Broccoli ', 'price': 0.2},
        {'name': 'Roasted Fennel ', 'price': 0.55},
        {'name': 'Mushrooms', 'price': 1.2},
        {'name': 'Grilled Eggplant', 'price': 0.2},
        {'name': 'Grilled Pineapple', 'price': 3},
        {'name': 'Roasted Garlic', 'price': 0.3},
    )


def fake_clients():
    return (
        {
            'client_name': 'Client 1',
            'client_dni': '0000000001',
            'client_address': 'address 01',
            'client_phone': '0900000001',
        },
        {
            'client_name': 'Client 2',
            'client_dni': '000000000',
            'client_address': 'address 0',
            'client_phone': '0900000002',
        },
        {
            'client_name': 'Client 3',
            'client_dni': '0000000003',
            'client_address': 'address 03',
            'client_phone': '0900000003',
        },
        {
            'client_name': 'Client 4',
            'client_dni': '0000000004',
            'client_address': 'address 04',
            'client_phone': '0900000004',
        },
        {
            'client_name': 'Client 5',
            'client_dni': '0000000005',
            'client_address': 'address 05',
            'client_phone': '0900000005',
        }
    )
