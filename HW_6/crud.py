from typing import List
from flask_sqlalchemy import SQLAlchemy

from models import User, Product, Order

db = SQLAlchemy()


# CRUD операции для таблицы пользователей
def create_user(user: User) -> User:
    db_user = User.query.filter_by(email=user.email).first()
    if db_user:
        raise ValueError("User with this email address already exists")

    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    )
    db.session.add(db_user)
    db.session.commit()
    return db_user


def get_user(user_id: int) -> User:
    db_user = User.query.get(user_id)
    if not db_user:
        raise ValueError("User not found")
    return db_user


def update_user(user_id: int, user: User) -> User:
    db_user = User.query.get(user_id)
    if not db_user:
        raise ValueError("User not found")

    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db_user.password = user.password

    db.session.commit()
    return db_user


def delete_user(user_id: int):
    db_user = User.query.get(user_id)
    if not db_user:
        raise ValueError("User not found")

    db.session.delete(db_user)
    db.session.commit()


def get_all_users() -> List[User]:
    return User.query.all()


# CRUD операции для таблицы товаров
def create_product(product: Product) -> Product:
    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price
    )
    db.session.add(db_product)
    db.session.commit()
    return db_product


def get_product(product_id: int) -> Product:
    db_product = Product.query.get(product_id)
    if not db_product:
        raise ValueError("Product not found")
    return db_product


def update_product(product_id: int, product: Product) -> Product:
    db_product = Product.query.get(product_id)
    if not db_product:
        raise ValueError("Product not found")

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price

    db.session.commit()
    return db_product


def delete_product(product_id: int):
    db_product = Product.query.get(product_id)
    if not db_product:
        raise ValueError("Product not found")

    db.session.delete(db_product)
    db.session.commit()


def get_all_products() -> List[Product]:
    return Product.query.all()


# CRUD операции для таблицы заказов
def create_order(order: Order) -> Order:
    db_order = Order(
        user_id=order.user_id,
        product_id=order.product_id,
        order_date=order.order_date,
        status=order.status
    )
    db.session.add(db_order)
    db.session.commit()
    return db_order


def get_order(order_id: int) -> Order:
    db_order = Order.query.get(order_id)
    if not db_order:
        raise ValueError("Order not found")
    return db_order


def update_order(order_id: int, order: Order) -> Order:
    db_order = Order.query.get(order_id)
    if not db_order:
        raise ValueError("Order not found")

    db_order.user_id = order.user_id
    db_order.product_id = order.product_id
    db_order.order_date = order.order_date
    db_order.status = order.status

    db.session.commit()
    return db_order


def delete_order(order_id: int):
    db_order = Order.query.get(order_id)
    if not db_order:
        raise ValueError("Order not found")

    db.session.delete(db_order)
    db.session.commit()


def get_all_orders() -> List[Order]:
    return Order.query.all()