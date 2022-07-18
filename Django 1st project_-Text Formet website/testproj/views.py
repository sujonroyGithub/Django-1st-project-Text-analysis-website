#i have create this  file= sujon
from itertools import count
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
 
def index(request):
    # params = {'name': 'sujon' , 'place':'setabgonj'}
    return render(request , 'index.html' , )
    # return HttpResponse(" <h1>Hello</h1>") 


def nav(request):
    s = '''<h2>Navigation Bar </h2><br> 
       <a href="https://www.youtube.com">YouTube</a><br>
       <a href="https://www.facebook.com">Facebook</a><br>
       <a href="https://www.gmail.com">Gmail</a><br>
       <a href="https://www.google.com">Google</a><br>
        '''
    return HttpResponse(s)
def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    #checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspeceremover = request.POST.get('extraspeceremover', 'off')
    characounter = request.POST.get('characounter', 'off')
    # print(removepunc)
    # print(djtext)
    #check which cheakbox is on
    if removepunc == "on":
   
        punctuations = """!()-[]{};:'"/,<>.\?@#$%^&*_~"""
        analyzed=""
        for char in djtext:
           if char not in punctuations:
            analyzed = analyzed + char

        params = {'purpuse': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps =="on":
        analyzed=""
        for char in djtext:
         analyzed = analyzed + char.upper()
        params = {'purpuse': 'changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and  char!="\r":
               analyzed = analyzed + char 
        params = {'purpuse': 'Remove New Line', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyze.html', params)
    if(extraspeceremover=="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" ") :
            
               analyzed = analyzed + char 
        params = {'purpuse': 'Extra spece Removed', 'analyzed_text': analyzed}
    if(removepunc != "on" and fullcaps !="on" and newlineremover !="on" and extraspeceremover!="on"):
        return HttpResponse("Please Select any Button First")    
        # return render(request, 'analyze.html', params)



    # elif(characounter=="on"):
    #     analyzed=""
    #     for index ,char in (djtext):
    #         if djtext[index]== count :
    #            analyzed = analyzed + count
            
              
    #     params = {'purpuse': 'The number of character', 'analyzed_text': analyzed}
    #     return render(request, 'analyze.html', params)             
    # else:
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', params)


    