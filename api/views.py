from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.helperFunc import formatter

class PredictDigit(APIView):
    def get(self, request, *args, **kwargs):
        # fp1_data = [123, 324, 123, 345, 123, 12, 43, 214, 234, 223, 235, 2351, 112, 142, 1241, 1421, 142]
        # fp2_data = [2351, 13412, 14142, 1241, 43, 214, 234, 123, 345, 123, 12, 43, 214, 234, 23523, 1421, 142]
        # t9_data = [14142, 1241, 345, 123, 12, 43, 214, 234, 324, 123, 345, 123, 12, 43, 214, 234, 1241, 1421, 142]
        # t10_data = [123, 324, 123, 345, 123, 12, 43, 214, 234, 225, 251, 1312, 1414, 1241, 1421, 142]
        # arr = []
        # arr.append({'type': 'FP1', 'data': fp1_data})
        # arr.append({'type': 'FP2', 'data': fp2_data})
        # arr.append({'type': 'T9', 'data': t9_data})
        # arr.append({'type': 'T10', 'data': t10_data})
        digit = kwargs['digit']
        new_dict = formatter(digit)
        return Response({'status': 'successful', 'data': new_dict})