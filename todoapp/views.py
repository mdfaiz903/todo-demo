from django.shortcuts import redirect, render
from.models import Todo
# Create your views here.
def index(request):
    if request.method=='POST':
        text = request.POST.get("text").strip()
        if text:
            Todo.objects.create(text=text)
        return redirect('/')
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request,'todoapp/index.html',context)
def about(request):
    return render(request,'todoapp/about.html')