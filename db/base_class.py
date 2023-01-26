from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr

"""
Using the Declarative system, we can create classes that include directives to describe the actual database table they will map to
A class using Declarative at a minimum needs a __tablename__ attribute and atleast one Column
cls
as_declarative is a Class decorator for declarative_base().
"""

@as_declarative()
class Base:
    id: Any
    __name__:str 
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()