"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from agenda.core.views import home
from agenda.contatos.views import add_contato
from agenda.contatos.views import cadastro_sucesso
from agenda.contatos.views import lista_contatos
from agenda.contatos.views import apagar_contato

urlpatterns = [
	url(r'^$', home, name='home'),
	url(r'^adicionar-contato/$', add_contato, name='addcontato'),
	url(r'^sucesso/$', cadastro_sucesso, name='sucesso'),
	url(r'^lista-contatos/$', lista_contatos, name='listacontatos'),
	url(r'^deletar-contato/(?P<id>\d+)/$', apagar_contato, name='apagarcontato'),
    url(r'^admin/', include(admin.site.urls)),
]
