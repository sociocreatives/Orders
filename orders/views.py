from django.shortcuts import render,get_object_or_404
from .models import Order, About, Faq, Terms, Partners
from rest_framework import generics,status
from . import serializers
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema


User=get_user_model()

class AboutView(generics.GenericAPIView):
    serializer_class=serializers.AboutSerializer


    @swagger_auto_schema(operation_summary="Get all About Texts")
    def get(self,request):
        about=About.objects.all()

        serializer=self.serializer_class(instance=about,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Create an About")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(Author=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    @swagger_auto_schema(operation_summary="Update an About by its ID")
    def put(self,request,id):
        
        order=get_object_or_404(About,pk=id)
        
        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete an About by its ID")
    def delete(self, request,id):
        
        order =get_object_or_404(About,id=id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class FaqView(generics.GenericAPIView):
    serializer_class=serializers.AboutSerializer
    # permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all Faq Texts")
    def get(self,request):
        faq=Faq.objects.all()

        serializer=self.serializer_class(instance=faq,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Create an About")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(Author=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class TermsView(generics.GenericAPIView):
    serializer_class=serializers.AboutSerializer
    # permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all About Texts")
    def get(self,request):
        terms=Terms.objects.all()

        serializer=self.serializer_class(instance=terms,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Create an About")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(Author=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   

class PartnersView(generics.GenericAPIView):
    serializer_class=serializers.AboutSerializer
    # permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all Partners")
    def get(self,request):
        partners=Partners.objects.all()

        serializer=self.serializer_class(instance=partners,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Create a Partner")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(Author=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class OrderView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="Get all Orders")
    def get(self,request):
        orders=Order.objects.all()

        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
        
    @swagger_auto_schema(operation_summary="Create an order")
    def post(self,request):
        data=request.data

        serializer=self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(customer=request.user)

            print(f"\n {serializer.data}")

            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)   


class OrderIdView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(operation_summary="View the detail of an order by its ID")
    def get(self, request,order_id):


        order=get_object_or_404(Order,pk=order_id)

        
        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an order by its ID")
    def put(self,request,order_id):
        
        order=get_object_or_404(Order,pk=order_id)
        
        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data,status=status.HTTP_200_OK)

        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete an order by its ID")
    def delete(self, request,order_id):
        
        order =get_object_or_404(Order,id=order_id)

        order.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        
class UpdateOrderStatusView(generics.GenericAPIView):
    
    serializer_class=serializers.OrderStatusUpdateSerializer

    @swagger_auto_schema(operation_summary="Update the status of an order")
    def put(self, request,order_id):
        order=get_object_or_404(Order,pk=order_id)

        serializer=self.serializer_class(instance=order,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK,data=serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST,data=serializer.errors)


class UserOrdersView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    @swagger_auto_schema(operation_summary="Get all orders made by a specific user")
    def get(self,request,user_id):
        user=User.objects.get(pk=user_id)

        orders=Order.objects.all().filter(customer=user)

        serializer=self.serializer_class(instance=orders,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

class UserOrderDetailView(generics.GenericAPIView):
    serializer_class=serializers.OrderSerializer
    permission_classes=[IsAuthenticated,IsAdminUser]

    @swagger_auto_schema(operation_summary="Get the detail of an order made by a specific user")
    def get(self,request,user_id,order_id):
        user=User.objects.get(pk=user_id)

        order=Order.objects.all().filter(customer=user).filter(pk=order_id)


        serializer=self.serializer_class(instance=order)

        return Response(data=serializer.data,status=status.HTTP_200_OK)







