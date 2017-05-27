from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from novousapp.models import fuel
from novousapp.serializers import FuelStationSerializer

@csrf_exempt
def options(request):
    if request.method == 'GET':
        return render(request, 'options.html',{"message": "Please select filters for searching"})

    if request.method == 'POST':
        temp = request.POST
        print temp.values()
        return render(request,'searchpage.html',{'temp':temp})

@csrf_exempt
def searchpage(request):
    if request.method == 'GET':
        return render(request,'searchpage.html')
    templist = []
    if request.method == 'POST':
        tempdata = request.POST

        if "city" in tempdata.keys() and "name" in tempdata.keys():
            tempname = tempdata['name']
            tempcity = tempdata['city']
            print tempname,tempcity
            tempobject = fuel.objects.filter(City__icontains=tempcity,Name__icontains=tempname)
            print tempobject
            print "double if"

        elif "city" in tempdata.keys():
            tempcity = tempdata['city']
            tempobject = fuel.objects.filter(City__icontains=tempcity)
            # print tempobject[0].City

        elif "name" in tempdata.keys():
            tempname = tempdata['name']
            tempobject = fuel.objects.filter(Name__icontains=tempname)

        else:

            tempobject = fuel.objects.all()

        return render(request,'result.html',{'tempobject' : tempobject})

class FuelStationList(APIView):
    def get(self, request):
        q = fuel.objects.all()
        serializer = FuelStationSerializer(q, many=True)
        # pagination_class = StandardResultsSetPagination
        return Response(serializer.data)

    def post(self, request):
        temp = request.data
        for x in temp:
            serializer = FuelStationSerializer(data=x)
            if serializer.is_valid():
                serializer.save()
