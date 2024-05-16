# Vendor Management System API

Welcome to the Vendor Management System API, a Django project for managing vendors, purchase orders, and performance metrics.

## Project Overview

The Vendor Management System provides a set of RESTful APIs for vendor management, purchase order creation, and performance metric tracking. It is designed to streamline the process of handling vendors and purchase orders.

## Features

- Vendor Management
- Purchase Order Creation and Management
- Performance Metrics Tracking


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vaishnavrs/vendor-management.git

1. `cd Vendor-management`
2. `python -m venv vms`
3. `vms\Scripts\activate`
4. `pip install -r requirements.txt`
5. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`

The API will be accessible at `http://127.0.0.1:8000/`.


Access the admin interface at `http://127.0.0.1:8000/admin/`.

## EndPoints
1. `api/vendors/`: Create a New Vendor
    Method:   Post
    Parameters: None
2.  `api/vendors/`: Retrieves all vendors
    Method :  Get
3.  `api/vendors/vendor_id`: Retrieves Specific Vendor
    Method :Get
4.  `api/purchase_orders/`: Create Purchase Order
    Method: Post
5.  `api/purchase_orders/`: Retrieves Purchase Order
    Method :Get
6.  `api/purchase_orders/po_id`: Retrieves Specific Purchase Order
    Method :Get
7.  `api/purchase_orders/po_id`: Delete Specific Purchase Order
    Method :Delete
8. `api/vendors/vendor_id/performance`:Retrieves Vendor Performance
    Method :Get
8. `api/purchase_orders/po_id/acknowledgment_date`:Acknowledges the Purchase order
    Method :Post
