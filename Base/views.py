from django.shortcuts import render,get_object_or_404 , redirect
from .Form import detailsform
from .models import Details

# Create your views here.

def index(request):
    form = detailsform(request.POST)
    if form.is_valid():
        form.save(commit=True)
        form = detailsform()
    taskss = Details.objects.all()
    return render(request,'index.html' , context={
        'forms':detailsform,
        'contents':taskss
    })

def editform(request,id):
    post = get_object_or_404(Details,id=id)
    context = {'form':detailsform(instance=post)}
    if request.method == 'POST':
        form = detailsform(request.POST,instance=post)
        form.save()
        if form.is_valid():
            return redirect(to='index')
    
    return render(request , 'edti.html',context=context)

def deleteform(request,id):
    item = Details.objects.get(id=id)
    item.delete()
    return redirect(to='index')
