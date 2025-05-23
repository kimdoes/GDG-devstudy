# views.py

from django.http import HttpResponse
from django.shortcuts import render	# 추가

def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

def first_view(request):	# 추가
    return render(request, 'my_test.html')

def test(request):
    name = request.POST.get('name')

    return render(request,
                  'view.html',
                  name)