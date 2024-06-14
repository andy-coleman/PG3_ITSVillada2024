import requests
from django.shortcuts import render

def index(request):
    try:
        api_url = 'https://api.thedogapi.com/v1/breeds'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()

            campos = request.GET.getlist('fields')
            busqueda = request.GET.get('search', '')
            cant_users = int(request.GET.get('user_count', len(data)))  

            if busqueda:
                data = [breed for breed in data if busqueda.lower() in breed['name'].lower()]

            data = data[:cant_users]

            return render(request, "index.html", {'data': data, 'selected_fields': campos, 'search_query': busqueda, 'user_count': cant_users})
        else:
            return render(request, "error.html", {'message': 'Error al obtener datos de la API'})
    except Exception as e:
        return render(request, "error.html", {'message': str(e)})
