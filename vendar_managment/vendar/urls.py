from django.urls import path
from .views import VendorCreateAPIView, VendorListAPIView, VendorRetrieveAPIView, VendorUpdateAPIView, VendorDeleteAPIView, PurchaseOrderCreateAPIView, PurchaseOrderListAPIView, PurchaseOrderRetrieveAPIView, PurchaseOrderUpdateAPIView, PurchaseOrderDeleteAPIView,VendorPerformanceAPIView



urlpatterns = [
    
    path('vendors/', VendorListAPIView.as_view(), name='vendor-list'),
    path('vendors/<int:vendor_id>/', VendorRetrieveAPIView.as_view(), name='vendor-detail'),
    path('vendors/<int:vendor_id>/update/', VendorUpdateAPIView.as_view(), name='vendor-update'),
    path('vendors/<int:vendor_id>/delete/', VendorDeleteAPIView.as_view(), name='vendor-delete'),
    path('vendors/create/', VendorCreateAPIView.as_view(), name='vendor-create'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
    path('purchase_orders/', PurchaseOrderListAPIView.as_view(), name='purchaseorder-list'),
    path('purchase_orders/<int:po_id>/', PurchaseOrderRetrieveAPIView.as_view(), name='purchaseorder-detail'),
    path('purchase_orders/create/', PurchaseOrderCreateAPIView.as_view(), name='purchaseorder-create'),
    path('purchase_orders/<int:po_id>/update/', PurchaseOrderUpdateAPIView.as_view(), name='purchaseorder-update'),
    path('purchase_orders/<int:po_id>/delete/', PurchaseOrderDeleteAPIView.as_view(), name='purchaseorder-delete'),
]
