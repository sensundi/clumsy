from django.shortcuts import render
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext

from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import DetailView
from django.contrib.auth.models import User


from helian.models import Department, Person, Status, Device, PowerUsage

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Site Brain!!")
    pass

def dash(request):
    return render_to_response('base.html',context_instance=RequestContext(request))

def devices(request):
    return render_to_response('charts.html',context_instance=RequestContext(request))

def tables(request):
    return render_to_response("tables.html", context_instance=RequestContext(request))

def getdevices(request,dept):
    mapping = {}
    devicelist = Device.objects.filter(dept__pk = int(dept))
    mapping = {'devices':devicelist}
    rc = RequestContext(request, mapping)
    return render_to_response("devices.html", 
                              context_instance=rc)
    
# def devicedetails(request, deviceid):
#     mapping = 
    
def engagedevice(request,devid):
    print devid
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
