from . import accounts, menuitems,menus,orders,orders_current
# promos, resources, reviews, tickets
from ..dependencies.database import engine
from ..dependencies.database import Base


def index():
    #orders_all.Base.metadata.create_all(engine)
    #order_details.Base.metadata.create_all(engine)

    #order_details.Base.metadata.create_all(engine)
    #recipes.Base.metadata.create_all(engine)
    #sandwiches.Base.metadata.create_all(engine)
    #resources.Base.metadata.create_all(engine)
    
    

    #should run tables for all classes with a base arg
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
