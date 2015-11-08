from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponse,HttpResponseRedirect,Http404
# from django.views.generic import DetailView
# from django.contrib.auth.models import User


from helian.models import Department, Person, Status, Device, PowerUsage

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Site Brain!!")
    pass

def dash(request):
    d = {}
    map_list=[]
    depts = Department.objects.all()
    dept_colors = ["panel panel-green",
                   "panel panel-yellow",
                   "panel panel-red"]
    dept_icons = ["fa fa-tasks fa-5x","fa fa-shopping-cart fa-5x","fa fa-support fa-5x"]
    
    for index, dept in enumerate(depts):
        device_count = len(Device.objects.filter(dept__pk=dept.id).all())
        mapping = {}
        mapping['devcount'] = device_count
        mapping['name'] = dept.name
        mapping['id'] = dept.id
        mapping['icon'] = dept_icons[index]
        mapping['color'] = dept_colors[index]
        map_list.append(mapping)
#     print map_list
    d['dept_list'] = map_list
    
    return render_to_response('base.html', d, context_instance=RequestContext(request))

def devices(request):
    return render_to_response('charts.html',context_instance=RequestContext(request))

def tables(request):
    return render_to_response("tables.html", context_instance=RequestContext(request))

def getdevices(request,dept):
    mapping = {}
    devicelist = Device.objects.filter(dept__pk = int(dept)).values()
    depobj = Department.objects.filter(pk=dept).all()[0]
    mapping = {'devices':devicelist, 'department':depobj.name}
    rc = RequestContext(request, mapping)
    return render_to_response("devices.html", 
                              mapping,
                              context_instance=rc)
    
# def devicedetails(request, deviceid):
#     mapping = 
    
def engagedevice(request,devid):
#     print devid
    device = Device.objects.filter(pk=int(devid)).all()[0]
    status = Status.objects.filter(name='locked').all()[0]
    device.status = status
    device.save()
    return HttpResponse("Device " + device.name + " isolated")

def disengagedevice(request,devid):
    device = Device.objects.filter(pk=int(devid)).all()[0]
    status = Status.objects.filter(name='available').all()[0]
    device.status = status
    device.save()
    return HttpResponse("Device " + device.name + " available")

def updatetemperature(request,devid,tmpr):
    device = Device.objects.filter(pk=int(devid)).all()[0]
    usage = PowerUsage(device=Device.objects.filter(pk=int(devid)).all()[0])
    if PowerUsage.objects.filter(device__pk=int(devid)).all():
        usage = PowerUsage.objects.filter(device__pk=int(devid)).all()[0]
    usage.temperature = float(tmpr)
    usage.unitsconsumed = 0.0
    usage.save()
    device.save() 
    return HttpResponse("Device " + device.name + " reported temperature of "+ tmpr + " degrees")
