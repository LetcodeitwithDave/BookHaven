from django.shortcuts import redirect 
from django.http import HttpResponse
# from .models import 
def author_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.groups.filter(name= 'Author'):
            return HttpResponse('You are not auhtourized to view this page', request.user.username)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def user_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.groups.filter(name= 'User'):
            return HttpResponse('You are not auhtourized to view this page', request.user.username)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
