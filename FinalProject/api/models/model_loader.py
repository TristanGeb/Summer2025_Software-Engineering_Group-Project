from . import orders, order_details, recipes, sandwiches, resources, accounts, menus, menu_items,promos, orders_current, orders_history, reviews, tickets

from ..dependencies.database import engine
from ..dependencies.database import Base


def index():
    #orders.Base.metadata.create_all(engine)
    #order_details.Base.metadata.create_all(engine)
    #recipes.Base.metadata.create_all(engine)
    #sandwiches.Base.metadata.create_all(engine)
    #resources.Base.metadata.create_all(engine)
    
    

    #should run tables for all classes with a base arg 
    Base.metadata.create_all(engine)
