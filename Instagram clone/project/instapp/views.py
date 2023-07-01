from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib import messages










    # Create the user


    # Save the user to the database
   





def home(request):
    
    return render(request, "index.html")


def logindone(request):
    if request.method == "POST":
        unm = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(username=unm, password=pwd)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully.')
            return render(request, 'profilepage.html')
        else:
            messages.error(request, 'Invalid login credentials.')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def signup(request):
    return render(request, 'signup.html')


def registerdone(request):
    if request.method == "POST":
        fname = request.POST['first_name']
        email = request.POST['email']
        unm = request.POST['username']
        pwd = request.POST['password']
        try:
            user = User.objects.get(username=unm)
            messages.error(request, 'Username already exists.')
            return render(request, 'signup.html')
        except:
            user = User.objects.create_user(first_name=fname, email=email, username=unm, password=pwd)
            Profile(user=user).save()
            user.save()
            messages.success(request, 'Account created successfully.')
            return render(request, 'index.html')
    else:
        return render(request, 'signup.html')


def profileshow(request):
    currentuser  = Profile.objects.get(user=request.user)
    followcount = currentuser.following.count()
    followerscount = currentuser.followers.count()
    Bio = currentuser.bio
    print(Bio)
    context ={
        'followcount' :followcount,
        'followerscount' : followerscount,
        'Bio':Bio,
        'currentuser' :currentuser,
    }
    print(followcount)
    return render(request, "profilepage.html",context)


def editprofile(request):
    return render(request, "editprofile.html")


def editeprofiledone(request):
    if request.method == 'POST' and request.FILES['profile-pic']:
        image_file = request.FILES['profile-pic']
        bio = request.POST['bio']
        user_profile = Profile.objects.get(user=request.user)
        user_profile.bio = bio
        user_profile.profile_pic = image_file
        user_profile.save()
        messages.success(request, 'Profile updated successfully.')
        return render(request, "profilepage.html")
    else:
        return render(request, "editprofile.html")


def search(request):
    catid = request.GET.get('q')
    searchusers = Profile.objects.filter(user__username__icontains = catid)
    context ={
        "searchusers" :searchusers,
        "catid"  : catid,
    }
    if(searchusers.count() != 0):
       return render(request, "search.html",context)
    return redirect('profileshow')

def followounfollow(request):
    if request.method == "POST":
        userid = request.POST["userid"]
        serchq = request.POST["serchq"]
        print(serchq)

        foolowuser = Profile.objects.get(id = userid)
        currentuser = Profile.objects.get(user = request.user)
        if request.user in foolowuser.followers.all():
            foolowuser.followers.remove(request.user)
            currentuser.following.remove(foolowuser.user) 
            return redirect(f'/search?q={serchq}')
            


        else:   
            foolowuser.followers.add(request.user)
            currentuser.following.add(foolowuser.user)  
            return redirect(f'/search?q={serchq}')
            


            
    else:
        return render(request, "search.html")
         


