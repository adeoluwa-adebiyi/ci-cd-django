from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import response

from .usecases.arithmetics import multiply


class MultiplyView(APIView):
    def get(self, request
            # , a=None, b=None
            ):
        return response.Response(data={"result": multiply(float(6), float(4))})
