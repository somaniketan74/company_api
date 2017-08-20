# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from company.models import Company
from company.serializers import CompanySerializer
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

import uuid
import traceback
import base64
from django.core.files.base import ContentFile


class companyView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer

    def get(self, request, *args, **kwargs):
        if 'profile_id' in request.query_params:
            company_profile = Company.objects.get(profile_id=request.query_params['profile_id'])
            serializer = CompanySerializer(company_profile)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(data={"id not found"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = request.data

        # Generating unique id for company
        data['profile_id'] = str(uuid.uuid4())

        # Convert base64 to file
        if 'logo' in data:
            format, imgstr = data['logo'].split(';base64,')
            ext = format.split('/')[-1]
            image = ContentFile(base64.b64decode(imgstr), name='logo.' + ext)
            data['logo'] = image

        serializer = CompanySerializer(data=data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except BaseException as ex:
            traceback.print_exc()
            print(ex)
            return Response(status=status.HTTP_400_BAD_REQUEST)
