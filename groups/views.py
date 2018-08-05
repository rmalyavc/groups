from django.shortcuts import render, redirect, reverse
from .models import Group, Elem
from .forms import ElemCreateForm

def Index(request):
	groups = Group.objects.all()
	return render(request, 'groups/base.html', {
		'index': 'index',
		'groups': groups,
	})

def elems(request):
	elems = Elem.objects.filter(checked = True)
	return render(request, 'groups/base.html', {
		'elems': elems,	
	})

def detail(request, id):
	groups = Group.objects.all().filter(parent_group__pk=id)
	elems = Elem.objects.all().filter(elem_parent_group__pk=id)
	group = Group.objects.get(pk=id)
	return render(request, 'groups/base.html', {
		'groups': groups,
		'elems': elems,
		'main_group': group,
	})

def create_elem(request):
	print(request.method + '\n')
	if request.method == 'GET':
		form = ElemCreateForm()
		return render(request, 'groups/add.html', {
			'form': form,
		})
	else:
		form = ElemCreateForm(request.POST, request.FILES)
		print('test!\n')
		print(form.data)
		if form.is_valid():
			form.save()
		return redirect('groups:Elems')
# Create your views here.
