from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    lista=list('abcdefghijklmnñopqrstuvwxyz')
    
    largo=int(request.GET.get('length'))
    
    if(request.GET.get('uppercase')):
        lista.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    
    if(request.GET.get('special')):
        lista.extend(list('+-*/.,-_|!"#$%&/()?¡¿'))
    
    if(request.GET.get('numbers')):
        lista.extend(list('0123456789'))
    
    contraseña_aleatoria=''
    for x in range(largo):
        contraseña_aleatoria+=random.choice(lista)

    return render(request,'generator/password.html',
                  {'password':contraseña_aleatoria}
                  )
