from .models import About, Link, Category, Post

# ABOUT


def ctx_dic_about(request):
    ctx_about = {}
    ctx_about['ABOUT'] = About.objects.latest('created')

    return ctx_about

# CATEGORIAS
def ctx_dic_category(request):
    ctx_category= {}
    
    ctx_category['categories']=Category.objects.filter(active=True)
    
    return ctx_category

# ARCHIVOS

# REDES SOCIALES


def ctx_dic_link(request):

    ctx_link = {}
    links = Link.objects.all()

    for link in links:
        ctx_link[link.key] = {'url': link.url, 'icon': link.icon}

    return ctx_link
