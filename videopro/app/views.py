
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import Users
from .models import videos,score
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.
def  user_view(request):
    if request.method=="POST":
        form = Users(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video')
    else:
        form = Users()
    context={
        'form':form
    }
    return render(request,'register.html',context)

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('video')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')


def index(request):
    if 'user' in request.session:
        current_user = request.session['user']
        
        return render(request, 'base.html',{'current_user': current_user})
    else:
        return redirect('login')
    
    

def video_view(request):
    if 'user' in request.session:
        v = videos.objects.all()
        return render(request,'videos.html',{'video':v})
    else:
        return redirect('login')



@csrf_exempt
def score_view(request):
    if 'user' in request.session:
        current_user = request.session['user']
        print(current_user)
        if request.method == "POST":
        
            userid = User.objects.get(username=current_user)
            print(userid)
            videoid = videos.objects.get(pk=1)
            print(videoid)
            points = request.POST.get('point')
            print(points)
            
            a=score.objects.get(user_id=userid)
            if a.is_valid():
                print(a.point)
                Scors_save = score(user_id=userid,video_id=videoid,point=points)
                Scors_save.save()
                return JsonResponse({'status':'save'})
            else:
                Scors_save = score(user_id=userid,video_id=videoid,point=points)
                Scors_save.save()
                return JsonResponse({'status':'save'})
    else:
        return redirect('login')
    
       

    

def rank_view(request):
    ranks=score.objects.order_by('point').reverse()
   
    return render(request,'rank.html',{"ranks":ranks})

def user_rank(request,id):
    rank = score.objects.get(user_id=id)
    print(rank)
