from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("PICKLES!")

def review(request, review_id):
    return HttpResponse(f"Looking at review {review_id}")

def review_new(request):
    return HttpResponse("Looking at new review page")

def pickle(request, pickle_id):
    return HttpResponse(f'Looking at pickle {pickle_id}')

def pickle_new(request):
    return HttpResponse(f'Looking at new pickle page')