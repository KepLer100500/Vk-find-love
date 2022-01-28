from rest_framework.views import APIView
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .test_vk import *


class ApiTest(APIView):
    @staticmethod
    def post(request):
        print(request.user.pk, request.user.get_username)
        got_users = main_search(request.data, request.user.pk)
        return HttpResponse(got_users)


def index(request):
    return render(request, 'main/index.html')


def app(request):
    search_current_user = Search.objects.filter(user_searcher=request.user.pk).order_by('-id')
    in_work_now = search_current_user[0].in_work_now if len(search_current_user) else False
    context = {
         'in_work_now': in_work_now,
    }
    return render(request, 'main/app.html', context)


def gotcha(request):
    searches = Search.objects.filter(user_searcher=request.user.pk)
    candidates = Candidate.objects.all()
    groups = CandidateGroups.objects.all()
    context = {
        'searches': searches,
        'candidates': candidates,
        'groups': groups
    }
    return render(request, 'main/gotcha.html', context)
