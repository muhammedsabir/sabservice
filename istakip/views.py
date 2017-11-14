from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import IsTakip
from .serializers import IsTakipSerializer
from django.contrib.auth.models import User
from datetime import datetime
import logging
#APIView
#@api_view(['GET', 'POST'])
#class IstakipList:
#def IstakipList(request):
    #def get(self,request):
#    if request.method == 'GET':
#        istakip = IsTakip.objects.all()
#        serializer = IsTakipSerializer(istakip,many=True)
#        return Response(serializer.data)

logger = logging.getLogger(__name__)


def checkUser(request,username,password):
    global cuser
    print(username)
    try:
         cuser = 0
         check_user = User.objects.get(username=username)
         print(check_user)
         logger.info('check_user'+str(check_user))
         if check_user.check_password(password):
             cuser = check_user.id
             print(cuser)

    except User.DoesNotExist:
        return None

@api_view(['GET','POST', 'PUT', 'DELETE'])
def Istakip_detail(request,kullanici,sifre):

    checkUser(request,kullanici,sifre)
    try:
        istakip = IsTakip.objects.all().filter(kullanici=cuser,durumu__in=["1","2"])
    except IsTakip.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IsTakipSerializer(istakip,many=True)
        logger.info('istakip line 51')
        return Response(serializer.data)
    elif request.method == 'POST':
        try:
            istakip = IsTakip.objects.all().filter(kullanici=kullanici,durumu__in=["1","2"])
            logger.info('istakip line 56')
        except IsTakip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = IsTakipSerializer(istakip,many=True)
        return Response(serializer.data)



@api_view(['GET','POST', 'PUT' ',DELETE'])
def Istakip_Start(request,kullanici,sifre,id):
    checkUser(request,kullanici,sifre)
    if request.method == 'GET' or request.method == 'POST':
        try:
            istakips = IsTakip.objects.filter(kullanici=cuser,id=id).first()
            print(id)
            print(istakips.durumu)
            istakips.durumu = 2
            istakips.başlangıç_tarihi = datetime.now()
            istakips.save()
            logger.info('istakip start 75')
            #serializer = IsTakipSerializer(istakips, many=True)
            return Response(status=status.HTTP_200_OK)
        except IsTakip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST', 'PUT' ',DELETE'])
def Istakip_Finish(request,kullanici,sifre,id):
    checkUser(request, kullanici, sifre)
    if request.method == 'GET' or request.method == 'POST':
        try:
            istakips = IsTakip.objects.filter(kullanici=cuser, id=id).first()
            print(id)
            print(istakips.durumu)
            istakips.durumu = 3
            istakips.sonlanma_tarihi = datetime.now()
            print(datetime.now())
            istakips.save()
            logger.info('istakip finish line 93')
            # serializer = IsTakipSerializer(istakips, many=True)
            return Response(status=status.HTTP_200_OK)
        except IsTakip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET','POST', 'PUT' ',DELETE'])
def Istakip_Pause(request,kullanici,sifre,id):
    checkUser(request, kullanici, sifre)
    if request.method == 'GET' or request.method == 'POST':
        try:
            istakips = IsTakip.objects.filter(kullanici=cuser, id=id)
            print(id)
            print(istakips.durumu)
            istakips.durumu = 4
            istakips.durum_güncelleme_tarihi = datetime.now()
            print(datetime.now())
            istakips.save()
            logger.info('istakip pause line 111')
            # serializer = IsTakipSerializer(istakips, many=True)
            return Response(status=status.HTTP_200_OK)
        except IsTakip.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
