from django.shortcuts import render, redirect
from app.models import Todo_list, Email

# Create your views here.


def landingPages(request):
    return render(request, 'landing_page.html',)


def todoListViews(request):
    if request.method == "POST":
        if 'title' in request.POST:
            title = request.POST['title']
            detail = request.POST['detail']
            todo_model = Todo_list.objects.create(title=title, detail=detail)
            todo_model.save()
        return redirect('todoView')
    todo_all = Todo_list.objects.all()
    context = {"todo_all": todo_all}
    return render(request, 'todolist.html', context)


def todoListSetting(request, id):
    if request.method == "POST":
        if "setTodo" in request.POST:
            todo_set = Todo_list.objects.get(id=id)
            todo_set.title = request.POST['setTitle']
            todo_set.detail = request.POST['setDetail']
            todo_set.save()
    return redirect('todoView')


def todoListDelete(request, id):
    if request.method == "POST":
        if "deleteTodo" in request.POST:
            todo_model = Todo_list.objects.get(id=id)
            todo_model.delete()
    return redirect('todoView')


def emailReply(request):
    if request.method == "POST":
        if 'email_reply' in request.POST:
            email = request.POST['email_reply']
            subject = request.POST['subject']
            detail = request.POST['detail']
            email_model = Email.objects.create(email_address=email, subject=subject, detail=detail)
            email_model.save()
        return redirect('emailView')
    context = {'emails': Email.objects.all()}
    return render(request, 'email_reply.html', context)


def emailDelete(request, id):
    email_model = Email.objects.get(id=id)
    email_model.delete()
    return redirect('emailView')
