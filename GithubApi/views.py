from django.shortcuts import render
import requests


def indexView(request):
    userInformation = False
    if request.method == 'POST':
        username = request.POST.get('username')
        url = f'https://api.github.com/users/{str(username)}'
        response = requests.get(url)
        userInformation = response.json()

    return render(request, 'index.html', context={'userInformation': userInformation})
