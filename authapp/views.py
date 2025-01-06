from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('success')

    # return render(request, 'signup.html')

# def signin(request):
#     return render(request, 'signin.html')

# # @login_required
# def success(request):
#     return render(request, 'success.html')

# # @login_required
# def home(request):
#     return render(request, 'home.html')

# # @login_required
# def logout(request):
#     return render(request, 'logout.html')

