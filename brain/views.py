from django.shortcuts import render
from django.http import HttpResponse
import aiml

kernel = aiml.Kernel()
print (kernel.learn("brain/k.xml"))
kernel.respond("load aiml b")




# def home(reuest):
#     while True:
#         print (kernel.respond(input("Enter your message >> ")))



def teena(request):
    lookup = request.GET.get('q')
    print (lookup)
    t = kernel.respond(lookup)
    print (t)
    context = {
        't': t
    }
    
    return render(request, 'teena.html',context)


def home(request):

    return render(request, 'home.html')




