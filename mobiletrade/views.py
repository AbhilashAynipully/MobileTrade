from django.core.exceptions import PermissionDenied
from django.shortcuts import render


# To render custom Error Templates

# 404 Error
def handler404(request, exception):
    return render(request, '404.html', status=404)


# 500 Error
def handler500(request):
    return render(request, '500.html', status=500)


# 403 Error
def handler403(request, exception):
    if isinstance(exception, PermissionDenied):
        return render(request, '403.html', status=403)
    else:
        return render(request, '500.html', status=500)
