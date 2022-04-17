from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from .serializers import *
from rest_framework import status,mixins,generics
from rest_framework.views import APIView
from ..models import *
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView

@api_view(['POST',])
def contact(request):
    serializer=ContactSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        data['subject']=request.data['subject']
        data['email']=request.data['email']
        data['message']=request.data['message']
        body= data['subject']+' \n'+data['email']+' \n'+data['message']
        form=EmailMessage('contact us',body,'test',('software.proj.test@gmail.com',))
        form.send(fail_silently=False)
    return Response(data)

class faqList(ModelViewSet):
    queryset=faq.objects.all()
    serializer_class=FAQSerializer

class CategoryList(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductList(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


