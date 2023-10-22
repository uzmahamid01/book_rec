from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {"time": datetime.now().strftime("%H:%M:%S")}
    return render(request, "core/index.html", context)
