from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'tras/index.html', context)
def index_1(request):
    context={}
    return render(request,'tras/footer.html',context)
def main(request):
    context={}
    return render(request,'tras/main.html',context)
def acticle(request):
    context={}
    return render(request,'tras/acticle_page.html',context)