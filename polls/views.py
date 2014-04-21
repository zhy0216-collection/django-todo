from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
# Create your views here.

from polls.models import Poll

def index(request):
    last_poll_list = Poll.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #             'last_poll_list':last_poll_list
    #           })
    # return HttpResponse(template.render(context))
    context = {'latest_poll_list':last_poll_list}
    print "last_poll_list:%s"%last_poll_list
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 
                  'polls/detail.html', 
                  {'poll':poll}
                )


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)


