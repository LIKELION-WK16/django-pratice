from django.shortcuts import render
from todo.models import TodoList

# Create your views here.
def todos(request):
    return render(
        request,
        'todo/todos.html',
        {
            'todolist': todos,
        }
    )

def index(request):
    #todolist의 모든 레코드를 가져온다.
    todolist = TodoList.objects.all()
    return render(
        request,
        'todo/index.html',
        {
            'todolist': todolist,
            }
        )
      #html에서 todolist라는 이름으로 todolist를 넘겨준다
      
    