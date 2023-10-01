from django.shortcuts import render

# Create your views here.
def Predict(request):
    
    
    
    context={}
    return render(request,'index.html',context)