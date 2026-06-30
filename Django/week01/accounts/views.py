from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login as auth_login

def signup(request):
  if request.method == "POST": # POST 요청 시
    form = SignupForm(request.POST) # 사용자의 데이터를 form에 넣음
    if form.is_valid(): # 입력값 검증
      form.save()
      return redirect('login')
  else: # GET 요청 시 회원가입 화면 보여줌
    form = SignupForm()
  
  return render(request, "signup.html", {"form":form})

def login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password) # 사용자 인증
    if user is not None:
      auth_login(request, user) # 장고에서 제공하는 login 메소드
      return redirect('main')
    
  return render(request, 'login.html') # 인증 실패 시 로그인 페이지를 렌더링

