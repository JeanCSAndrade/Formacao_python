from sqlalchemy.orm import declarative_base, relationship
import sqlalchemy as sqla

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    name = sqla.Column(sqla.String)
    fullname = sqla.Column(sqla.String)

    address = relationship(
        "Address", back_populates="User", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"user_account(id = {self.id}, name = {self.name}, fullname = {self.fullname})"

class Address(Base):
    __tablename__ = "Address"

    id = sqla.Column(sqla.Integer, primary_key=True, autoincrement=True)
    email_address = sqla.Column(sqla.String, nullable=False)
    user_id = sqla.Column(sqla.Integer, sqla.ForeignKey("user_account.id"))

    user = relationship(
        "User", back_populates="Address"
    )

    def __repr__(self):
        return f"Address(ID = {self.id}, email = {self.email_address})"
    
engine = sqla.create_engine("sqlite://")

Base.metadata.create_all(engine)

inspect_engine = sqla.inspect(engine)

print(inspect_engine.get_table_names())

print(inspect_engine.get_columns("user_account"))