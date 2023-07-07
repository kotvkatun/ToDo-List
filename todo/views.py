from django.views.generic.edit import FormView, View
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoLists
# Create your views here.


class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            todolist = ToDoLists.objects.get(owner=request.user)
            if todolist:
                return render(request, "index.html", {"todojson": todolist.todolist})
        return render(request, "index.html")

    def post(self, request):
        todojson = request.POST["TodoJSON"]
        if not todojson:
            return render(request, "index.html")

        old_list = ToDoLists.objects.get(owner=request.user)
        old_list.todolist = todojson
        old_list.save()
        return render(request, "index.html", {"todojson" : todojson})