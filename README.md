# Vendor Management System

This project is a Vendor Management System built using Django and Django REST Framework. It allows users to manage vendors, track purchase orders, and evaluate vendor performance metrics.

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x recommended)
- Django
- Django REST Framework

### Installation

1. Clone the repository:

git clone https://github.com/your_username/vendor-management-system.git


2. Navigate to the project directory:

cd vendor-management-system


3. Install dependencies:

pip install -r requirements.txt


4. Apply migrations:

python manage.py migrate


### Usage

1. Run the development server:

python manage.py runserver


2. Access the API endpoints in your browser or using a tool like Postman:

- Vendors:
  - Create: `POST /api/vendors/`
  - List: `GET /api/vendors/`
  - Retrieve: `GET /api/vendors/{vendor_id}/`
  - Update: `PUT /api/vendors/{vendor_id}/`
  - Delete: `DELETE /api/vendors/{vendor_id}/`

- Purchase Orders:
  - Create: `POST /api/purchase_orders/`
  - List: `GET /api/purchase_orders/`
  - Retrieve: `GET /api/purchase_orders/{po_id}/`
  - Update: `PUT /api/purchase_orders/{po_id}/`
  - Delete: `DELETE /api/purchase_orders/{po_id}/`

- Vendor Performance:
  - Retrieve: `GET /api/vendors/{vendor_id}/performance/`

### Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for any bugs or feature requests.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

