from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
#g = Group.objects.get(name='groupname')
#g.user_set.add(your_user)

#prueba:
from django.contrib.auth.decorators import user_passes_test

def is_productor(user):
    return user.groups.filter(name='PRODUCTOR').exists()


@user_passes_test(is_productor)
def productor_agregar(request):
    return render(request, 'core/productor/producto-agregar.html')

