from django.contrib.auth import logout
from django.shortcuts import redirect, render

def logout_view(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return render(request, 'registration/logged_out_page.html')
    else:
        return redirect('login')
