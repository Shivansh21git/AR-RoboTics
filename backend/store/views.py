from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_products(request):
    return Response({"message": "Store API working!"})
# Create your views here.

