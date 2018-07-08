from django.shortcuts import render,redirect
from .models import TodoList, Category
from django.views.generic import ListView,DeleteView
from django.urls import reverse_lazy
from django.utils.timezone import localdate
from django.contrib import messages
from django.utils.dateparse import parse_date

class todo(ListView):
    model = TodoList
    template_name = "index.html"

    def get_queryset(self):
        return TodoList.objects.order_by('-created')


def add(request):
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            dateobj = parse_date(date)
            if dateobj is not None and dateobj > localdate() :
                category = request.POST["category_select"]
                if category:
                    content = title + " -- " + date + " " + category
                    Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
                    Todo.save()
                    return redirect("/")
                else:
                    messages.error(request,"Please choose the category")
            else:
                messages.error(request,"Please select the valid date")
    return render(request, "add.html", {"categories":categories})

class TodoDeleteView(DeleteView):
    success_url = reverse_lazy('Todolist')
    model = TodoList
    template_name = "delete.html"
