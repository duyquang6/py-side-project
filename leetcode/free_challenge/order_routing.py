w_cost = 0.6
w_pdd = 0.4
# B1: Collect các thông tin ban đầu (chi phí giao hàng ứng với mỗi kho đến client, thông tin tồn kho (stocks),... )
cart = [
    {
        'item_id': 1,
        'product_id': 1,
        'qty': 15,
    },
    {
        'item_id': 2,
        'product_id': 5,
        'qty': 2,
    },
]

delivery_cost = {
    "sgn": 50000,
    "sgn3": 40000,
    "vln": 45000,
}


stocks = {
    1: {
        'qty_salable': 5
    },
    2: {
        'qty_salable': 5
    },
}

# B2: loop qua 1 lần các phương án để tính PDD và Cost cho mỗi phương án



# B3: Tính toán phương án best nhất dựa vào kết quả B2
plans = [
    {
        "packages": [
            {
                "items": [
                    {
                        "item_id": 1,
                        "qty": 3,
                        "sku": "2514716496708",
                        "product_id": 580534,
                        "seller_id": 641
                    }
                ],
                "leadtime": {
                    "lgh": 24,
                    "lss": 0,
                    "lrim": 0,
                    "no_process_date": [],
                    "no_inbound_date": []
                },
                "fulfillment_type": "tiki_delivery",
                "warehouse": "sgn",
                "shipping_plan_id": 1,
                "delivery_commitment_time": "2019-09-26 23:59:59",
                "order_route": "same_province",
                "order_area": "urban"
            },
            {
                "items": [
                    {
                        "item_id": 2,
                        "qty": 1,
                        "sku": "2304288033667",
                        "product_id": 225,
                        "seller_id": 1
                    }
                ],
                "leadtime": {
                    "lgh": 24,
                    "lss": 0,
                    "lrim": 0,
                    "no_process_date": [],
                    "no_inbound_date": []
                },
                "fulfillment_type": "tiki_delivery",
                "warehouse": "vln",
                "shipping_plan_id": 1,
                "delivery_commitment_time": "2019-09-26 23:59:59",
                "order_route": "same_province",
                "order_area": "urban"
            }
        ],
        "pdd": 2,
        "delivery_cost": 50000,
    },
    {
        "packages": [
            {
                "items": [
                    {
                        "item_id": 1,
                        "qty": 3,
                        "sku": "2514716496708",
                        "product_id": 580534,
                        "seller_id": 641
                    }
                ],
                "leadtime": {
                    "lgh": 24,
                    "lss": 0,
                    "lrim": 0,
                    "no_process_date": [],
                    "no_inbound_date": []
                },
                "fulfillment_type": "tiki_delivery",
                "warehouse": "sgn",
                "shipping_plan_id": 1,
                "delivery_commitment_time": "2019-09-26 23:59:59",
                "order_route": "same_province",
                "order_area": "urban"
            },
            {
                "items": [
                    {
                        "item_id": 2,
                        "qty": 1,
                        "sku": "2304288033667",
                        "product_id": 225,
                        "seller_id": 1
                    }
                ],
                "leadtime": {
                    "lgh": 24,
                    "lss": 0,
                    "lrim": 0,
                    "no_process_date": [],
                    "no_inbound_date": []
                },
                "fulfillment_type": "tiki_delivery",
                "warehouse": "vln",
                "shipping_plan_id": 1,
                "delivery_commitment_time": "2019-09-26 23:59:59",
                "order_route": "same_province",
                "order_area": "urban"
            }
        ],
        "pdd": 3,
        "delivery_cost": 40000,
    },
    {
        "packages": [
            {
                "items": [
                    {
                        "item_id": 1,
                        "qty": 3,
                        "sku": "2514716496708",
                        "product_id": 580534,
                        "seller_id": 641
                    }
                ],
                "leadtime": {
                    "lgh": 24,
                    "lss": 0,
                    "lrim": 0,
                    "no_process_date": [],
                    "no_inbound_date": []
                },
                "fulfillment_type": "tiki_delivery",
                "warehouse": "sgn",
                "shipping_plan_id": 1,
                "delivery_commitment_time": "2019-09-26 23:59:59",
                "order_route": "same_province",
                "order_area": "urban"
            },
            {
                "items": [
                    {
                        "item_id": 2,
                        "qty": 1,
                        "sku": "2304288033667",
                        "product_id": 225,
                        "seller_id": 1
                    }
                ],
                "leadtime": {
                    "lgh": 24,
                    "lss": 0,
                    "lrim": 0,
                    "no_process_date": [],
                    "no_inbound_date": []
                },
                "fulfillment_type": "tiki_delivery",
                "warehouse": "vln",
                "shipping_plan_id": 1,
                "delivery_commitment_time": "2019-09-26 23:59:59",
                "order_route": "same_province",
                "order_area": "urban"
            }
        ],
        "pdd": 4,
        "delivery_cost": 45000,
    },
]


print(cart)
