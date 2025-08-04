from . import accounts,menu_items,menu,orders
from . import orders_current,promos,resources
from . import reviews

def load_routes_main(app):
    #app.include_router()
    pass
def load_routes_admin(app):
    app.include_router(accounts.router)
    app.include_router(menu_items.router)
    app.include_router(menu.router)
    app.include_router(orders.router)
    app.include_router(orders_current.router)
    app.include_router(promos.router)
    app.include_router(resources.router)
    app.include_router(reviews.router)