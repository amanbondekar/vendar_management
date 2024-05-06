# vendar_management

# Vendor Management System API

The Vendor Management System API is a Django-based application designed to help businesses manage their vendors and purchase orders effectively.

## Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
Install dependencies:
pip install -r requirements.txt
#Apply migrations:
python manage.py migrate
Run the development server:

python manage.py runserver
Access the application:Open your web browser and go to http://localhost:8000/ to access the application.
API Endpoints
The following API endpoints are available:

Vendors
Create a new vendor:
Endpoint: POST /api/vendors/
Request body: JSON object with vendor details (name, contact_details, address, vendor_code)
Example:
json
{
    "name": "Vendor Name",
    "contact_details": "vendor@example.com",
    "address": "123 Vendor Street",
    "vendor_code": "V001"
}
List all vendors:
Endpoint: GET /api/vendors/
Retrieve a specific vendor's details:
Endpoint: GET /api/vendors/<vendor_id>/
Update a vendor's details:
Endpoint: PUT /api/vendors/<vendor_id>/
Request body: JSON object with updated vendor details
Example:
json
{
    "name": "Updated Vendor Name",
    "contact_details": "updated_vendor@example.com",
    "address": "456 Updated Vendor Street",
    "vendor_code": "V002"
}
Delete a vendor:
Endpoint: DELETE /api/vendors/<vendor_id>/
Purchase Orders
Create a new purchase order:
Endpoint: POST /api/purchase_orders/
Request body: JSON object with purchase order details (po_number, vendor, order_date, delivery_date, items, quantity, status)
Example:
json
{
    "po_number": "PO001",
    "vendor": 1,
    "order_date": "2024-05-08T10:00:00Z",
    "delivery_date": "2024-05-15T10:00:00Z",
    "items": ["Item 1", "Item 2"],
    "quantity": 10,
    "status": "pending"
}
List all purchase orders:
Endpoint: GET /api/purchase_orders/
Retrieve details of a specific purchase order:
Endpoint: GET /api/purchase_orders/<po_id>/
Update a purchase order:
Endpoint: PUT /api/purchase_orders/<po_id>/
Request body: JSON object with updated purchase order details
Example:
json
{
    "po_number": "Updated PO001",
    "vendor": 1,
    "order_date": "2024-05-08T10:00:00Z",
    "delivery_date": "2024-05-15T10:00:00Z",
    "items": ["Updated Item 1", "Updated Item 2"],
    "quantity": 20,
    "status": "completed"
}
Delete a purchase order:
Endpoint: DELETE /api/purchase_orders/<po_id>/

Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.
Create a new branch (git checkout -b feature/my-feature).
Make your changes and commit them (git commit -am 'Add my feature').
Push to the branch (git push origin feature/my-feature).
Create a new Pull Request.
License
This project is licensed under the MIT License.

rust
Replace `<repository-url>` with the actual URL of your project's Git repository.

This README provides detailed setup instructions, information about each API 
