from django.urls import path
from .views import home, post, category, author, dates

urlpatterns = [
    # PAGINA DE INICIO
    path('',home, name="home"),
    
    # PAGINA FILTRADA POR CATEGORIAS
    path('category/',category, name="category"),
    
    # PAGINA FILTRADA POR AHUTOR
    path('author/',author, name="author"),

# PAGINA FILTRADA POR FECHA
    path('dates/',dates, name="dates"),

    path('post/', post, name="post"),
]
