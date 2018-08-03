from django.shortcuts import render
from .models import Group, Elem
from .forms import ElemCreateForm

def Index(request):
	groups = Group.objects.all()
	return render(request, 'groups/base.html', {
		'index': 'index',
		'groups': groups,
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

def create_elem(request, group_id):
	group = Group.objects.get(pk = group_id)
	form = ElemCreateForm()
	return render(request, 'groups/add.html', {
		'group': group,
		'form': form,
	})
# Create your views here.
