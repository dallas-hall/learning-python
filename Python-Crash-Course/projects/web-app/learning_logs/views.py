from django.shortcuts import render


# Page name from urls.py
def index(request):
    """
    The home page for the Learning Log.
    """
    return render(request, "learning_logs/index.html")
