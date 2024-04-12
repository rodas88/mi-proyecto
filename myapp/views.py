from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def register(request):
    """
    Vista para manejar el registro de usuarios.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('nombre_de_tu_vista_de_inicio')  # Reemplaza 'nombre_de_tu_vista_de_inicio' con el nombre de tu vista de inicio
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    """
    Vista para manejar el inicio de sesión de usuarios.
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('nombre_de_tu_vista_de_inicio')  # Reemplaza 'nombre_de_tu_vista_de_inicio' con el nombre de tu vista de inicio
        else:
            # Manejar el caso de inicio de sesión fallido
            return render(request, 'registration/login.html', {'form': form, 'error_message': 'Usuario o contraseña incorrectos.'})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})




