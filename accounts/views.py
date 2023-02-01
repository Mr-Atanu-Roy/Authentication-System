from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from accounts.models import *

import uuid

from .utils import *



# Create your views here.
@login_required(login_url="/login")
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
    else:
        context = {
                    'fname' : '',
                    'email' : '',
                    'password' : '',
                    'cPassword' : '',
                    }
        try:
            if request.method == "POST":
                fname = request.POST.get("fname")
                email = request.POST.get("email")
                password = request.POST.get("password")
                cPassword = request.POST.get("confirm-password")
                
                context['fname'] = fname
                context['email'] = email
                context['password'] = password
                context['cPassword'] = cPassword
                
                
                if email != "":
                    if User.objects.filter(username = email).first() :
                        messages.error(request, "An account already exists with this email")
                    else:
                        if fname != "" and password != "" and cPassword != "":
                            if password == cPassword:
                                newUser = User.objects.create_user(username=email, email=email, password=password)
                                newUser.first_name = fname
                                newUser.save()
                                
                                token = str(uuid.uuid4())
                                newProfile = Profile.objects.create(user = newUser, auth_token = token)
                                newProfile.save()
                                
                                context['fname'] = context['email'] = context['password'] = context['cPassword'] = ""
                                
                                subject = "Please verify your email"
                                message = f"Hello!!! Thank you for signing up with us {fname}... Please verify your email : {email} by clicking on the given link http://127.0.0.1:8000/email-verify/{token}"
                                send_custom_email(email, subject, message)
                
                                messages.success(request, "Account created successfully. Please check your email to verify it")
                                return redirect('/login')
                            else:
                                messages.warning(request, "Your passwords do not match")
                        else:
                            messages.warning(request, "All fields are required")
                            
                else:
                    messages.warning(request, "Email is required")
                    
                
        except Exception as e:
            print(e)
            
            
        return render(request, 'signup.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect('/')
        
    else:
        context = {
                'email' : '',
                'password' : '',
                }
        try:
            if request.method == "POST":
                email = request.POST.get('email')
                password = request.POST.get('password')
                
                context['email'] = email
                context['password'] = password
                if email != "" and password != "":
                    userCheck = User.objects.filter(username = email).first()
                    
                    if userCheck:
                        user = auth.authenticate(username = email, password = password)
                        print(user)
                        if user is not None:
                            userProfile = Profile.objects.get(user = user)
                            if userProfile.is_verified:
                                if user is not None:
                                    auth.login(request, user)
                                    messages.success(request, "Login successful")
                                    
                                    if request.GET.get('next') != None:
                                        return redirect(request.GET['next'])
                                    
                                    return redirect('/')
                                else:
                                    messages.warning(request, "Invalid credentials")
                            else:
                                messages.warning(request, "Your email is not verified. Verify it to login")
                        else:
                            messages.error(request, "invalid credentials")
                    
                    else:
                        messages.warning(request, "No account exists with this email")
                
                else:
                    messages.warning(request, "Email and Password are required")
                
                
        except Exception as e:
            print(e)
            
        
        return render(request, 'login.html', context)


@login_required(login_url="/login")
def logout(request):
    auth.logout(request)  
    messages.warning(request, "You are logged out now")  
    return redirect('/login')


def email_verify(request, token):
    try:
        profileObj = Profile.objects.filter(auth_token = token).first()
        
        if profileObj.is_verified:
            print("true")
            messages.warning(request, "Your account is already verified")
        else:
            profileObj.is_verified = True
            profileObj.save()
            messages.success(request, "Your account is now verified. Please Login")
            print("done true")
        
    except Exception as e:
        print(e)
        
    
    return redirect('/login')


def resetPassword(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are logged in")
        
        return redirect('/')
    else:
        context = {
            "email" : ""
        }
        try:
            if request.method == "POST":
                email = request.POST.get("email")
                if email != "":
                    context['email'] = email
                    checkUser = User.objects.filter(username = email).first()
                    
                    if checkUser:
                        token = str(uuid.uuid4())
                        subject = f"Reset password for {email}"
                        message = f"To reset password for email : {email} click on the given link http://127.0.0.1:8000/reset-password/{token}"
                        
                        newResetPass = ResetPassword(user = checkUser, otp = token)
                        newResetPass.save()
                        
                        send_custom_email(email, subject, message)
                        messages.success(request, "Password reset link has been sent to your email")
                    else:
                        messages.error(request, "No account exists with the given email")
                else:
                    messages.error(request, "Email is required")
                
        except Exception as e:
            print(e)
                
        
        return render(request, 'reset_password.html', context)

def resetPasswordLink(request, token):
    if request.user.is_authenticated:
        messages.waring(request, "You are logged in")
        return redirect('/')
    else:
        context = {
            'password' : ""
        }
        resetPassObj = ResetPassword.objects.filter(otp = token, is_used = False).first()
        if resetPassObj:
            context['username'] = resetPassObj.user
            if request.method == "POST":
                password = request.POST.get('password')
                if password != "":
                    context['password'] = password
                    
                    user = User.objects.get(username = resetPassObj.user)
                    user.set_password(password)
                    user.save()
                    
                    resetPassObj.is_used = True
                    resetPassObj.save()                    
                    
                    messages.success(request, "Password successfully updated")
                    return redirect('/login')
                    
                else:
                    messages.error(request, "Enter a new password")
        else:
            messages.error(request, "Invalid URL")
            return redirect('/reset-password')
        
    return render(request, 'reset_password_link.html', context)


