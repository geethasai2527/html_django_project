from django.shortcuts import render

# Create your views here.
def table(request):
    return render(request,'table.html')
def forms(request):
    return render(request,'forms.html')
def image(request):
    return render(request,'image.html')
def lists(request):
    return render(request,'lists.html')
def formatting(request):
    return render(request,'formatting.html')
def anchor(request):
    return render(request,'anchor.html')
def marquee(request):
    return render(request,'marquee.html')
def colspan(request):
    return render(request,'colspan.html')
def nestedtable(request):
    return render(request,'nestedtable.html')
def rowspan(request):
    return render(request,'rowspan.html')