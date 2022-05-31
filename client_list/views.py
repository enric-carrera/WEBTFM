from django.shortcuts import render, redirect
from client_list.models import Client
from django.contrib.auth.decorators import login_required
from .forms import AddClientForm
# Create your views here

@login_required
def clients_index(request):

    clients = Client.objects.all()
    print(clients[0].image)
    context = {

        'clients': clients

    }

    return render(request, 'clients_index.html', context)

@login_required
def client_detail(request,pk):

    client = Client.objects.get(pk=pk)

    context = {

	'client': client

    }

    return render(request, 'client_detail.html', context)

@login_required
def add_client(request):

    form = AddClientForm()
   
    if request.method == 'POST':

        form = AddClientForm(request.POST)

        if form.is_valid():

            client = Client(

                company=form.cleaned_data["company"],

                description=form.cleaned_data["description"],

                budget=form.cleaned_data["budget"],

		image=form.cleaned_data["image"],

		expiration_date=form.cleaned_data["expiration_date"]

            )

            client.save()

            return redirect('clients_index')
    
    context = {

        "form": form,

    }
    return render(request, "add_client.html", context)

@login_required
def eliminate_client(request, pk):

    client = Client.objects.get(pk=pk)
    
    client.delete()
#    print("client eliminated")
    return redirect('clients_index')
