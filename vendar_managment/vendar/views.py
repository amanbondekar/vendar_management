from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vendor
from .serializer import VendorSerializer,PurchaseOrderSerializer

class VendorCreateAPIView(APIView):
    def post(self, request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendorListAPIView(APIView):
    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

class VendorRetrieveAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

class VendorUpdateAPIView(APIView):
    def put(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            serializer = VendorSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)

class VendorDeleteAPIView(APIView):
    def delete(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            performance_metrics = {
                'on_time_delivery_rate': vendor.on_time_delivery_rate,
                'quality_rating_avg': vendor.quality_rating_avg,
                'response_time_avg': vendor.response_time_avg,
                'fulfilment_rate': vendor.fulfilment_rate
            }
            return Response(performance_metrics)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)




class PurchaseOrderCreateAPIView(APIView):
    def post(self, request):
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PurchaseOrderListAPIView(APIView):
    def get(self, request):
        if 'vendor_id' in request.query_params:
            purchase_orders = PurchaseOrder.objects.filter(vendor_id=request.query_params['vendor_id'])
        else:
            purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

class PurchaseOrderRetrieveAPIView(APIView):
    def get(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
            serializer = PurchaseOrderSerializer(purchase_order)
            return Response(serializer.data)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)


class PurchaseOrderUpdateAPIView(APIView):
    def put(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
            serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)


class PurchaseOrderDeleteAPIView(APIView):
    def delete(self, request, po_id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=po_id)
            purchase_order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)
