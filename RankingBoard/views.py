from django.shortcuts import render
from django.http import JsonResponse
from .models import RankingBoard
# Create your views here.
def rankingboard(request):
    if request.method == "GET":
        namechar = str(request.GET.get("name", default=''))[:200]
        mark = 0
        try:
            mark = int(request.GET.get("mark"))
        except (TypeError, ValueError):
            pass
        if namechar:
            add = RankingBoard(namechar=namechar, mark=mark)
            add.save()
    return JsonResponse(list(RankingBoard.objects.all().order_by('-mark', 'datetime')[0:50].values('namechar','mark','datetime')), safe = False)