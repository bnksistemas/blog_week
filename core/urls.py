from django.urls import path
from .views import home, post, category, author, dates

urlpatterns = [
    # PAGINA DE INICIO
    path('',home, name="home"),
    
    # PAGINA FILTRADA POR CATEGORIAS
    path('category/<int:category_id>',category, name="category"),
    
    # PAGINA FILTRADA POR AHUTOR
    path('author/<int:author_id>',author, name="author"),

# PAGINA FILTRADA POR FECHA
    path('dates/<int:month_id>/<int:year_id>' , dates, name="dates"),

    path('post/<int:post_id>', post, name="post"),
]
