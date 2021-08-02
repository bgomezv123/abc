from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.utils import json
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
import json 
import codecs

class IndexView(APIView):

	def get(self, request, format=None):
		content = {
			'wmsg': 'Welcome to the American Cap'
		}
		return Response(content)

class DataMorbilidadView(APIView):

	def get(self, request, format=None):
		json_data = codecs.open('public/templates/datosAdolescentes.json','r','utf-8-sig')
		content = json.load(json_data)['Morbilidad_Adolescente']
		return Response(content)

class DataRiesgoView(APIView):

	def get(self, request, format=None):
		json_data = codecs.open('public/templates/datosAdolescentes.json','r','utf-8-sig')
		content = json.load(json_data)['Riesgo_Adolescente']
		return Response(content)

class DataTamizajeView(APIView):

	def get(self, request, format=None):
		json_data = codecs.open('public/templates/datosAdolescentes.json','r','utf-8-sig')
		content = json.load(json_data)['Tamizaje_Adolescente']
		return Response(content)

class DataAdolescentes(APIView):
	def get(self, request, format=None):
		json_data = codecs.open('public/templates/datosAdolescentes.json','r','utf-8-sig')
		content = json.load(json_data)
		return Response(content)

class DataMapas(APIView):
	def get(self, request, format=None):
		json_data = codecs.open('public/templates/datosMapas.json','r','utf-8-sig')
		content = json.load(json_data)
		return Response(content)