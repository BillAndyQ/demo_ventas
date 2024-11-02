from django.contrib import admin
from django.urls import path, include
from .views.home import hola_mundo
from .views.auth import login, logout
from .views.ventas import listar_ventas, comprobantes, comprobante, nueva_venta
from .views.series import series
# from .views.login import login

urlpatterns = [
    path('', hola_mundo, name='hola_mundo'),
    path('api/login/', login, name='login'),
    path('api/logout/', logout, name='logout'),
    
    path('api/ventas/', listar_ventas, name='ventas'),       # Todas las ventas por producto, búsqueda / GET
    path('api/ventas/nueva/', nueva_venta, name='nueva_venta'),   # Nueva venta / POST
    
    path('api/ventas/comprobantes/', comprobantes, name='comprobantes'),  # Todos los comprobantes y búsqueda / GET
    path('api/ventas/comprobante/<str:serie>-<int:numero>', comprobante, name='comprobante'),   # Comprobante específico / GET
    
    path('api/productos/', logout, name='productos'),           # Todos los productos o búsqueda / GET
    path('api/productos/nuevo/', logout, name='productos'),     # Nuevo producto / POST
    path('api/producto/', logout, name='productos'),            # Producto específico / PUT / GET / DELETE
    
    path('api/series/', series, name='series'),        # Todas las series por producto, búsqueda / GET
    path('api/serie/', series, name='serie'),        # Serie específica / GET / DELETE
]
