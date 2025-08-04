from . import accounts,menu_items,menu,orders,orders_current

def load_routes_main(app):
    #app.include_router()
    pass
def load_routes_admin(app):
    app.include_router(accounts.router)
    app.include_router(menu_items.router)
    app.include_router(menu.router)
    app.include_router(orders.router)
    app.include_router(orders_current.router)