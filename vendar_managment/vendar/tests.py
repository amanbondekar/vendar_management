from django.test import TestCase, RequestFactory
from rest_framework import status
from .views import VendorCreateAPIView, VendorListAPIView, VendorRetrieveAPIView, VendorUpdateAPIView, VendorDeleteAPIView, VendorPerformanceAPIView,PurchaseOrderCreateAPIView, PurchaseOrderListAPIView, PurchaseOrderRetrieveAPIView, PurchaseOrderUpdateAPIView, PurchaseOrderDeleteAPIView
from .models import Vendor, PurchaseOrder


class VendorAPITests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.vendor = Vendor.objects.create(name='Test Vendor', contact_details='test@example.com', address='123 Test St', vendor_code='V001', on_time_delivery_rate=0.95, quality_rating_avg=4.5, average_response_time=2.5, fulfillment_rate=0.98)
        self.vendor_id = self.vendor.id

    def test_vendor_create_api_view(self):
        request = self.factory.post('/api/vendors/', {'name': 'New Vendor', 'contact_details': 'new@example.com', 'address': '456 New St', 'vendor_code': 'V002', 'on_time_delivery_rate': 0.98, 'quality_rating_avg': 4.7, 'average_response_time': 3.2, 'fulfillment_rate': 0.96})
        response = VendorCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_vendor_list_api_view(self):
        request = self.factory.get('/api/vendors/')
        response = VendorListAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vendor_retrieve_api_view(self):
        request = self.factory.get(f'/api/vendors/{self.vendor_id}/')
        response = VendorRetrieveAPIView.as_view()(request, vendor_id=self.vendor_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vendor_update_api_view(self):
        request = self.factory.put(f'/api/vendors/{self.vendor_id}/', {'name': 'Updated Vendor'})
        response = VendorUpdateAPIView.as_view()(request, vendor_id=self.vendor_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_vendor_delete_api_view(self):
        request = self.factory.delete(f'/api/vendors/{self.vendor_id}/')
        response = VendorDeleteAPIView.as_view()(request, vendor_id=self.vendor_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_vendor_performance_api_view(self):
        request = self.factory.get(f'/api/vendors/{self.vendor_id}/performance/')
        response = VendorPerformanceAPIView.as_view()(request, vendor_id=self.vendor_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.purchase_order = PurchaseOrder.objects.create(po_number='PO001', vendor_reference='Vendor1', order_date='2024-05-10', delivery_date='2024-05-20', items=['Item1', 'Item2'], quantity=10, status='Pending')
        self.po_id = self.purchase_order.id

    def test_purchase_order_create_api_view(self):
        request = self.factory.post('/api/purchase_orders/', {'po_number': 'PO002', 'vendor_reference': 'Vendor2', 'order_date': '2024-05-15', 'delivery_date': '2024-05-25', 'items': ['Item3', 'Item4'], 'quantity': 15, 'status': 'Pending'})
        response = PurchaseOrderCreateAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_purchase_order_list_api_view(self):
        request = self.factory.get('/api/purchase_orders/')
        response = PurchaseOrderListAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_order_list_api_view_with_vendor_filter(self):
        request = self.factory.get('/api/purchase_orders/', {'vendor_id': self.purchase_order.vendor_id})
        response = PurchaseOrderListAPIView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_order_retrieve_api_view(self):
        request = self.factory.get(f'/api/purchase_orders/{self.po_id}/')
        response = PurchaseOrderRetrieveAPIView.as_view()(request, po_id=self.po_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_order_update_api_view(self):
        request = self.factory.put(f'/api/purchase_orders/{self.po_id}/', {'status': 'Completed'})
        response = PurchaseOrderUpdateAPIView.as_view()(request, po_id=self.po_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_purchase_order_delete_api_view(self):
        request = self.factory.delete(f'/api/purchase_orders/{self.po_id}/')
        response = PurchaseOrderDeleteAPIView.as_view()(request, po_id=self.po_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
