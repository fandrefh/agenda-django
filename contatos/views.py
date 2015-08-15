from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .forms import ContatoForm
from .models import Contato

# Create your views here.

def add_contato(request):
	if request.method == 'POST':
		form_contato = ContatoForm(request.POST)
		if form_contato.is_valid():
			form_contato.save()
			return redirect(reverse('sucesso'))
		else:
			print(form_contato.errors)
	else:
		form_contato = ContatoForm()
	return render(request, 'add_contato.html', {'form_contato': form_contato})

def cadastro_sucesso(request):
	return render(request, 'sucesso.html')

def lista_contatos(request):
	contatos = Contato.objects.all()
	return render(request, 'lista_contatos.html', {'contatos': contatos})

def apagar_contato(request, id):
	Contato.objects.get(id=id).delete()
	return redirect(reverse('listacontatos'))