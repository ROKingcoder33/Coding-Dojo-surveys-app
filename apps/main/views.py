from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1

    context = {
        "title" : "Survey",
    }
    return render(request, 'main/index.html', context)


def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session.modified = True
        return redirect('/result')


def result(request):
    request.session['counter'] += 1
    context = {
        "title": "Survey Result",
        "name": request.session['name'],
        "location": request.session['location'],
        "language": request.session['language'],
        "comment": request.session['comment'],
        "number": request.session['counter'],
    }
    return render(request, 'main/result.html', context)
