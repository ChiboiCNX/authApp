from django.shortcuts import render, redirect
from .forms import CreateUserForm


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print('User created')  # Replace with logging for production
            return redirect("signin")
        else:
            print('Form errors:', form.errors)  # Debugging: Log form errors

    context = {'form': form}
    return render(request, 'signup.html', context)
       
def signin(request):
    return render(request, 'signin.html')

# # @login_required
def success(request):
    return render(request, 'success.html')

# # @login_required
def home(request):
    return render(request, 'home.html')

# # @login_required
def logout(request):
    return render(request, 'logout.html')

