# MISSION STATEMENT

- To efficiently manage and optimize the administration of **micronutrients** through a robust **IV inventory system**, ensuring timely access to high-quality products while fostering partnerships with reliable suppliers.

## MISSION OBJECTIVE


### Efficient Supplier Management:

- Maintain a comprehensive record of all suppliers.
- Ensure each supplier has a unique identifier.
- Capture essential details such as supplier name.

### Comprehensive Product Catalog:

- Maintain a detailed list of products, including name, category, and supplier association.
- Ensure products have unique identifiers.
- Track supplier relationships via foreign keys to facilitate supplier-specific inventory management.
- Record and enforce unit prices, ensuring no negative values.
- Monitor stock levels accurately, ensuring no negative quantities.
- Define reorder levels to trigger inventory replenishment.
- Track expiry dates to manage product lifecycle and minimize waste.

### Effective Order Tracking:

- Record all product orders, including quantities and dates.
- Ensure each order has a unique identifier.
- Link orders to specific products to maintain accurate sales and inventory records.
- Track order quantities, ensuring no negative values to maintain data integrity.
- Monitor order dates to analyze sales trends and manage stock efficiently.

## Prerequisites
Before running the project, ensure you have the following:

- at least Python 3.11.5 installed
- Virtual environment tool 


### Set up
- python3 -m venv .venv     (Create a virtual environment)
- source .venv/bin/activate  (Activate the virtual environment on Linux)

### How to run
- In order to set up a database on your psql terminal:
    - CREATE DATABASE <database-name>
    - \c <database-name>

- Navigate to the src folder (cd src).
- Run the project using python terminal (python3 -m mini_project).


