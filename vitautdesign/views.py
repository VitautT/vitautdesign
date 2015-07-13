# djcode/pySite/pySite/views.py

from django.shortcuts import render_to_response
from django.template import RequestContext
from news.views import Post


# ����� ���������� ��� � news/views.py
def home(request):
    vars = dict (
            posts=Post.objects.all().order_by('-timestamp')[:10],
                )

    return render_to_response('vitautdesign/index.html', vars, context_instance=RequestContext(request))