from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.exc import SQLAlchemyError 
from sqlalchemy import func

# create 
Base = declarative_base()

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20))
    email = Column(String(50))
    address = Column(String(100))

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    price = Column(Integer)
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    
    # relationship between Product and Supplier
    supplier = relationship("Supplier")

engine = create_engine('sqlite:///17/database.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


# insert
try:
    with Session() as session:  
        suppliers = [
            Supplier(name="Supplier A", phone="12345678", email="contact@a.com", address="Address A"),
            Supplier(name="Supplier B", phone="87654321", email="contact@b.com", address="Address B"),
            Supplier(name="Supplier C", phone="12348765", email="contact@c.com", address="Address C"),
            Supplier(name="Supplier D", phone="56781234", email="contact@d.com", address="Address D"),
            Supplier(name="Supplier E", phone="43217865", email="contact@e.com", address="Address E")
        ]
        session.add_all(suppliers)
        session.commit()
except SQLAlchemyError as e:  
    print(f"Error in: {e}")

try:
    with Session() as session:  
        products = [
            Product(name="Product 1", description="Prodcut description 1", price=100, supplier_id=1),
            Product(name="Product 2", description="Prodcut description 2", price=200, supplier_id=2),
            Product(name="Product 3", description="Prodcut description 3", price=300, supplier_id=3),
            Product(name="Product 4", description="Prodcut description 4", price=400, supplier_id=4),
            Product(name="Product 5", description="Prodcut description 5", price=500, supplier_id=5)
        ]
        session.add_all(products)
        session.commit()
except SQLAlchemyError as e:
    print(f"Error in: {e}")

# consult
for product in session.query(Product).all():
    print(f"Product: {product.name}, Supplier: {product.supplier.name}")

# query
with Session() as session:
    query_result = session.query(
    Supplier.name,
    func.sum(Product.price).label('total_preco')
    ).join(Product, Supplier.id == Product.supplier_id
    ).group_by(Supplier.name).all()

    for name, total_price in query_result:
        print(f"Suppllier: {name}, Total Price: {total_price}")