"""Database connector

This script allows user to connect to localhost database 'sprzedaz'. User can:
 - Order product,
 - Create order,
 - Check products quantity in magazine or in orders.
"""

import mysql
from termcolor import colored
from List4.DAO.OrderDAO import OrderDAO
from List4.DAO.ProductDAO import ProductDAO
from List4.DAO.OrdersProductsDAO import OrdersProductsDAO


def main():
    input_word = ''

    while input_word != "quit" and input_word != "-q":
        input_word = input(colored("product order", 'green') +
                           " - order product (default one, for multiply add alias -m)\n" +
                           colored("product check", 'green') +
                           " - check products quantity (-magazine, -orders)\n")
        input_word.strip()
        if 'product order' in input_word:
            create_order = input('Please type `order create`, to create order, or number of order to add items\n')
            if 'order create' in create_order:
                receiver = input('Please put order receiver:\n')
                if not None:
                    OrderDAO.add_order(receiver)
                else:
                    print('Please type something!\n')
                order_last = OrderDAO.select_last()
                order_id = order_last[0].ID
            else:
                order_id = create_order
                orderr = OrderDAO.select_by_id(order_id)
                if len(orderr) == 1:
                    order_last = orderr
                else:
                    print("There is no order with this ID\n")
                    break

            order_pretty_print(order_last)
            if '-m' in input_word:
                order_list = []
                orders = ''
                print("Please type order info like (to exit type -q):")
                while orders != '-q':
                    orders = input("Product ID, Quantity\n")
                    if orders != '-q':
                        order_list.append(parse_order(orders))
                if len(order_list) == 0:
                    print("You must put at least one order!\n")
                else:
                    orders_count = 0
                    for o in order_list:
                        orders_count = orders_count + 1
                        try:
                            OrderDAO.insert(o[0], o[1], order_id)
                        except mysql.connector.Error as err:
                            print(colored(f"{err}\n", 'red'))
                            orders_count = orders_count - 1
                    od_list = OrdersProductsDAO.select_last(orders_count)
                    orders_products_pretty_print(od_list)
            else:
                orders = input("Please type order info like:\n"
                               "Product ID, Quantity\n")
                order_tab = parse_order(orders)
                try:
                    OrderDAO.insert(order_tab[0], order_tab[1], order_id)
                    od_list = OrdersProductsDAO.select_last(1)
                    orders_products_pretty_print(od_list)
                except mysql.connector.Error as err:
                    print(colored(f"{err}\n", 'red'))
        if 'product check' in input_word:
            if '-magazine' in input_word:
                products_list = ProductDAO.select_all()
                product_pretty_print(products_list, 'Magazine Quantity')
            elif '-orders' in input_word:
                products_list = ProductDAO.select_products_order_qunatity()
                product_pretty_print(products_list, 'Products in orders')


def parse_order(order_string):
    order_info = order_string.split(',')
    if len(order_info) != 2:
        raise Exception('Input must have 2 elements separated with comma')
    else:
        return order_info


def order_pretty_print(order_list):
    space = ' '
    headers = ['ID', 'Receiver']
    spaces = [10, 45]
    print(colored(
        f'{headers[0]}{(spaces[0] - len(headers[0])) * space}'
        f'{headers[1]}{(spaces[1] - len(headers[1])) * space}', 'blue'))
    for o in order_list:
        a = len(str(o.ID))
        print(f'{o.ID}{(spaces[0] - len(str(o.ID))) * space}'
              f'{o.receiver}{(spaces[1] - len(o.receiver)) * space}')
    print()


def product_pretty_print(product_list, header_string):
    space = ' '
    headers = ['ID', 'Product name', header_string]
    spaces = [10, 45, 30]
    print(colored(
        f'{headers[0]}{(spaces[0] - len(headers[0])) * space}'
        f'{headers[1]}{(spaces[1] - len(headers[1])) * space}'
        f'{headers[2]}{(spaces[2] - len(headers[2])) * space}', 'blue'))
    for p in product_list:
        a = len(str(p.ID))
        print(f'{p.ID}{(spaces[0] - len(str(p.ID))) * space}'
              f'{p.name}{(spaces[1] - len(p.name)) * space}'
              f'{p.magazine_quantity}{(spaces[2] - len(str(p.magazine_quantity))) * space}')
    print()


def orders_products_pretty_print(order_products_list):
    space = ' '
    headers = ['ID', 'Product name', 'Order quantity', 'Order ID', 'Receiver']
    spaces = [10, 45, 15, 10, 45]
    print(colored(
        f'{headers[0]}{(spaces[0] - len(headers[0])) * space}'
        f'{headers[1]}{(spaces[1] - len(headers[1])) * space}'
        f'{headers[2]}{(spaces[2] - len(headers[2])) * space}'
        f'{headers[3]}{(spaces[3] - len(headers[3])) * space}'
        f'{headers[4]}{(spaces[4] - len(headers[4])) * space}'
        , 'blue'))
    for op in order_products_list:
        a = len(str(op.ID))
        print(f'{op.ID}{(spaces[0] - len(str(op.ID))) * space}'
              f'{op.product.name}{(spaces[1] - len(op.product.name)) * space}'
              f'{op.order_quantity}{(spaces[2] - len(str(op.order_quantity))) * space}'
              f'{op.order.ID}{(spaces[3] - len(str(op.order.ID))) * space}'
              f'{op.order.receiver}{(spaces[4] - len(str(op.order.receiver))) * space}'
              )
    print()


if __name__ == '__main__':
    main()
