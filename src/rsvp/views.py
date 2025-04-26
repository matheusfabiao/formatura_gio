from django.shortcuts import redirect, render

from .forms import RSVPForm


# Create your views here.
def index(request):
    if request.method != 'POST':
        # Nenhum dado submetido; exibe um formulário em branco.
        form = RSVPForm()
    else:
        # Dados POST submetidos; processa os dados.
        form = RSVPForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'rsvp/index.html', context)


def success(request):
    return render(request, 'rsvp/success.html')
