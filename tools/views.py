from django.shortcuts import render


def multiple_stopwatch(request):
    return render(request, 'tools/multiple_stopwatch_gemini.html')

def stopwatches(request):
    return render(request, 'tools/stopwatches.html')
