from django.shortcuts import render


def visual_feed(request):
    return render(request, 'visual_feed.html')

