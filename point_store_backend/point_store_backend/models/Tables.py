from sqlalchemy import String, DateTime, DATETIME, Float, ForeignKey, func, Integer, Table, Column
from typing import Optional, List
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .Meta import Base

association_table = Table(
    "association_table_order",
    Base.metadata,
    Column("order_id", ForeignKey("order.id")),
    Column("product_id", ForeignKey("product.id")),
)


class Client(Base):
    __tablename__ = 'client'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    last_name:   Mapped[Optional[str]] = mapped_column(
        String(30), name='lastName', nullable=True)
    cedula:   Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True)
    telephone:  Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True, default='0000000000')
    address: Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True, default='Jipiro alto')
    orders: Mapped[List['Order']] = relationship(
        back_populates="client", cascade="all, delete-orphan",
    )

    def parseJson(self):
        return {
            'type': 'cliente',
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'telephone': self.telephone,
            'address': self.address,
            'cedula': self.cedula,
            'orders': [order.parseJson() for order in self.orders]
        }

    def __repr__(self) -> str:
        return f"Client(id={self.id!r}, name={self.name!r}, last_name={self.last_name!r})"


class Order(Base):
    __tablename__ = 'order'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    create_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    amount: Mapped[int] = mapped_column(Integer, default=0)

    products: Mapped[List['Product']] = relationship(
        back_populates="orders", secondary=association_table
    )

    client_id: Mapped[int] = mapped_column(ForeignKey('client.id'))
    client: Mapped[Optional['Client']] = relationship(back_populates='orders')

    supplier_id: Mapped[int] = mapped_column(ForeignKey('supplier.id'))
    supplier: Mapped[Optional['Supplier']] = relationship(
        back_populates='orders')

    def parseJson(self):
        return {
            'id': self.id,
            'create_at': self.create_at.isoformat(),
            'amount': self.amount,
            'products': [product.parseJson() for product in self.products],
            'client_id': self.client_id,
            'supplier_id': self.supplier_id
        }

    def __repr__(self) -> str:
        return f"Order(id={self.id!r}, create_at={self.create_at!r}, amount={self.amount!r})"


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float(3))
    descripcion:   Mapped[Optional[str]] = mapped_column(
        String(55), nullable=True)
    amount: Mapped[int] = mapped_column(Integer)

    supplier_id: Mapped[int] = mapped_column(ForeignKey('supplier.id'))
    supplier: Mapped[Optional['Supplier']] = relationship(
        back_populates='products')

    orders: Mapped[List['Order']] = relationship(
        back_populates="products", secondary=association_table
    )

    def parseJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'amount': self.amount,
            'descripcion': self.descripcion,
            'supplier_id': self.supplier_id
        }

    def __repr__(self) -> str:
        return f"Product(id={self.id!r}, name={self.name!r}, amount={self.amount!r})"


class Supplier(Base):
    __tablename__ = 'supplier'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    telephone:  Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True, default='0000000000')
    cedula:   Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(
        String(30), nullable=True, default='Jipiro alto')

    products: Mapped[List['Product']] = relationship(
        back_populates="supplier", cascade="all, delete-orphan"
    )

    orders: Mapped[List['Order']] = relationship(
        back_populates="supplier", cascade="all, delete-orphan"
    )

    def parseJson(self):
        return {
            'type': 'proveedor',
            'id': self.id,
            'name': self.name,
            'telephone': self.telephone,
            'address': self.address,
            'cedula': self.cedula,
            'products': [p.parseJson() for p in self.products],
            'orders': [o.parseJson() for o in self.orders]
        }

    def __repr__(self) -> str:
        return f"Supplier(id={self.id!r}, name={self.name!r})"


# class ProductOrder(Base):
#     __tablename__ = 'intermediate'

#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

#     product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
#     product: Mapped[Optional['Product']] = relationship(back_populates='orders')

#     order_id: Mapped[int] = mapped_column(ForeignKey('order.id'))
#     order: Mapped[Optional['Order']] = relationship(back_populates='products')
