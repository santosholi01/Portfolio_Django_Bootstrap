from django.shortcuts import render,redirect
from django.views import View
from .forms import contractform

# Create your views here.

class home(View):
    def get(self, request):
        return render(request, 'index.html')


class contractuser(View):
    def get(self, request):
        fm=contractform()
        return render(request, 'index.html',{'form':fm} )
    
    def post(self, request):
        fm=contractform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            print("invalid message")