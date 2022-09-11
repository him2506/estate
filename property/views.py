from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Agent, Property,Prop_Image,Location
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def home(request):
    f_locs = Location.objects.all()
    props = Property.objects.filter(latest = True).order_by('prop_id')
 
    return render(request, 'index.html',{'f_locs': f_locs,'props':props})


def about(request):
    return render(request,'about.html')

def property(request):
    pro = Property.objects.all().order_by('prop_id')

    page = request.GET.get('page', 1)
    paginator = Paginator(pro, 6)
    try:
        content = paginator.page(page)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)
    
    return render(request,'property-grid.html',{'pro':content})

def single_prop(request,prop_id):
    pr = get_object_or_404(Property, prop_id=prop_id)
    photos = Prop_Image.objects.filter(prop=pr)
    ag = Agent.objects.filter(agent_name = pr.agent_id)
    print(pr.agent_id)
    print(ag[0])
    return render(request, 'property-single.html', {
        'pr':pr,
        'photos':photos,
        'ag':ag[0]
    })

def loc_prop(request,loc_id):
    p = Property.objects.filter(loc_id = loc_id).order_by('prop_id')
    l = Location.objects.filter(loc_id = loc_id)
    print(l)
    print(p)
    return render(request,'check.html',{'props':p,'l':l[0]})