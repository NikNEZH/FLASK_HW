from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from models import User, Product, Order
from crud import *

app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Создание таблиц в базе данных
with app.app_context():
    db.create_all()

# Регистрация маршрутов

# Маршруты для таблицы пользователей
@app.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return {'users': users}

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user(user_id)
    return {'user': user}

@app.route('/users', methods=['POST'])
def create_user():
    user = User(**request.json)
    user = create_user(user)
    return {'user': user}

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User(**request.json)
    user = update_user(user_id, user)
    return {'user': user}

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_user(user_id)
    return {'message': 'User deleted successfully'}

# Маршруты для таблицы товаров
@app.route('/products', methods=['GET'])
def get_products():
    products = get_all_products()
    return {'products': products}

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product(product_id)
    return {'product': product}

@app.route('/products', methods=['POST'])
def create_product():
    product = Product(**request.json)
    product = create_product(product)
    return {'product': product}

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product(**request.json)
    product = update_product(product_id, product)
    return {'product': product}


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    delete_product(product_id)
    return {'message': 'Product deleted successfully'}


# Маршруты для таблицы заказов
@app.route('/orders', methods=['GET'])
def get_orders():
    orders = get_all_orders()
    return {'orders': orders}


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = get_order(order_id)
    return {'order': order}


@app.route('/orders', methods=['POST'])
def create_order():
    order = Order(**request.json)
    order = create_order(order)
    return {'order': order}


@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = Order(**request.json)
    order = update_order(order_id, order)
    return {'order': order}


@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    delete_order(order_id)
    return {'message': 'Order deleted successfully'}


if __name__ == '__main__':
    app.run(debug=True)