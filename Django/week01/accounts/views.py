from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
  if request.method == "POST": # POST 요청 시
    form = SignupForm(request.POST) # 사용자의 데이터를 form에 넣음
    if form.is_valid(): # 입력값 검증
      form.save()
      return redirect('login')
  else: # GET 요청 시 회원가입 화면 보여줌
    form = SignupForm()
  
  return render(request, "signup.html", {"form":form})

