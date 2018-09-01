from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from personal.models import source, node1, node2, node3

def index(request):
    return render(request, 'personal/home.html')

def TurnOFF1(request):
    return render(request, 'personal/status.html', {'content':['The first node is now turned off in the HES Scholar Room']})

def TurnOFF2(request):
    return render(request, 'personal/status.html', {'content':['The second node is now turned off in the HES Scholar Room']})

def TurnOFF3(request):
    return render(request, 'personal/status.html', {'content':['The third node is now turned off in the HES Scholar Room']})

def TurnOFFS(request):
    return render(request, 'personal/status.html', {'content':['Everything is now turned off in the HES Scholar Room']})

def vals(request):
    source_obj = source.objects.last()
    node1_obj = node1.objects.last()
    node2_obj = node2.objects.last()
    node3_obj = node3.objects.last()
    
    s = source_obj.valuesV + "#"+ source_obj.valuesI + "#" + source_obj.valuesP + "#" + node1_obj.value1V + "#"+ node1_obj.value1I + "#" + node1_obj.value1P + "#" + node2_obj.value2V + "#"+ node2_obj.value2I + "#" + node2_obj.value2P + "#" + node3_obj.value3V + "#"+ node3_obj.value3I + "#" + node3_obj.value3P
    return JsonResponse({"resp" : s})
