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




### Instructions To Run The Program: 
1. prerequisites :  
    - Open Terminal
    - Set the working directory in you computer: using below command in terminal
    ```python
        cd desktop/mini_personal_db/src
    ```

    - Run the below command in terminal to switch to postgres, and to create the database and add data into tables to use the program. 

    ```sql
    cd db/sql_files
    psql -U postgres
    \i create_tables.sql
    \i order.sql
    \i product.sql
    \i supplier.sql
    \i example_queries.sql
    \q
    ```  
    - Creating the virtual Environment and to install psycopg3 follow the instructions 
    ```python
        cd .. 
        cd .. 
        python3 -m venv .venv --prompt mini_projectDB
        source .venv/bin/activate
        pip install -r requirements.txt
    ```     

2. To Run the main program : 
    ```python 
        cd ..
        python3 -m src.mini_project
    ```



