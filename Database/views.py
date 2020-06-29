from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.views import APIView

import os, glob, csv

# Create your views here.


class ServerViews(APIView):
    def get(self, request):
        return render(request, "home.html")


class A(APIView):
    def get(self, request):
        return render(request, "chemViewer2D.html")


class B(APIView):
    def get(self, request):
        mol_path = "chemFiles/pyrrole.mol"
        ctx = {
            "mol_location": f"url(../static/{mol_path})",
        }
        return render(request, "renderStatic.html", context=ctx)


class D(APIView):
    def get(self, request):
        return render(request, "render3D.html")


class InputChemStruc(APIView):
    def get(self, request):
        return render(request, "compose.html")


class About(APIView):
    def get(self, request):
        return render(request, "about.html")
