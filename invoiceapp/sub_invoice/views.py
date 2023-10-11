
from django.views import View
from .serializers import *
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .data import *
from .models import *



class AllInvoices(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        invoices = Invoices.objects.filter(user=request.user.id)
        serializer = InvoicesSerializer(invoices, many=True).data  # Use 'invoices' queryset
        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        serializer = InvoicesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class SingleInvoice(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, id):
        try: 
            invoice = Invoices.objects.get(invoice_id=id, user=request.user.id)
            serializer = InvoicesSerializer(invoice).data
            return Response(serializer, status=status.HTTP_200_OK)
        except Invoices.DoesNotExist:  # Fix the typo here
            return Response({"message": "Invoice not found"}, status=status.HTTP_404_NOT_FOUND)
    


class AddItems(APIView):
    def post(self, request, id):
        data = request.data  # Removed extra 'data' from 'request.datadata'
        data["invoices"] = id
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         

class SignupView(APIView):
     def post(self,request):
        data = request.data
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account created succefully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class SigninView(APIView):
    def post(self,request):
         data = request.data
         serializer = LoginSerializer(data=data)
         if serializer.is_valid():
            user = serializer.validated_data
            token = RefreshToken.for_user(user)
            return Response({"messages":"login sucess", "access_token": str(token.access_token), "refresh_token": str(token) }, status=status.HTTP_200_OK)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    