from datetime import datetime
from django.http import HttpResponse

def common(request):
    return HttpResponse("<strong> Common </strong> <br><br> La hoja en blanco de los anónimos")