from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pickle, PickleMaker, Tag
from django.shortcuts import get_object_or_404, render, redirect
import json
from django.views import generic
from django.core.paginator import Paginator

def index(request):
    return HttpResponse("PICKLES!")

def review(request, review_id):
    return HttpResponse(f"Looking at review {review_id}")

def review_new(request):
    return HttpResponse("Looking at new review page")

def pickle_maker(request, pickle_maker_id):
    return HttpResponse(f"Looking at pickle maker {pickle_maker_id}")

def pickle_maker_new(request):
    return HttpResponse('Looking at new pickle maker page')

def pickle_maker_all(request):
    makers = PickleMaker.objects.all()
    return JsonResponse(sorted(m.name for m in makers), safe=False)

def tags_all(request):
    tags = Tag.objects.all()
    return JsonResponse(sorted(t.tag for t in tags), safe=False)

def pickle(request, pickle_id):
    pickle = get_object_or_404(Pickle, pk=pickle_id)
    return render(request, 'pickles/pickle.html', {'pickle': pickle})

class PickleAll(generic.ListView):
    template_name = 'pickles/all_pickles.html'
    context_object_name = 'all_pickles'
    paginate_by = 25

    def get_queryset(self):
        return Pickle.objects.all()

def pickle_new(request):
    if request.POST:
        name = request.POST['new_pickle_name']
        maker = request.POST['pickle_maker']
        tags = request.POST['pickle_tags']
        pickle_makers = PickleMaker.objects.filter(name=maker)
        pickle_maker = None
        is_new_pickle_maker = False
        if len(pickle_makers) > 0:
            pickle_maker = pickle_makers[0]
        else:
            pickle_maker = PickleMaker(name=maker)
            pickle_maker.save()
            is_new_pickle_maker = True
        pickles = Pickle.objects.filter(name=name, maker=pickle_maker)
        if len(pickles) == 0:
            new_pickle = Pickle(name=name, maker=pickle_maker)
            new_pickle.save()
            return redirect(f'/pickles/{new_pickle.id}')
        else:
            pickle_id = pickles[0].id
            return redirect(f'/pickles/{pickle_id}')
    else:
        return render(request, 'pickles/new_pickle.html')  
