from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob


def index(request):
    
    return render(request,'index.html')
    



def counter(request):
    if request.method == 'POST':
        text = request.POST['text']
        amount_of_words = len(text.split())
        corrected_text = str(TextBlob(text).correct())  
        return render(request, 'counter.html', {'amount': amount_of_words, 'corrected_text': corrected_text})
    else:
        return render(request, 'counter.html')




