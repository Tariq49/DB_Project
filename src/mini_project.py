import psycopg as pg




db_params = {
            "dbname": "i_v_inventory",
            "user":"postgres",
            "password":"postgres",
            "host":"localhost",
            "port":"5432",
}
        
CONN = pg.connect(**db_params)

cur= CONN.cursor()

with open('mini_project.py', 'r') as python_file:
    file_content = python_file.read()

def query_data():
    cur.execute("SELECT * FROM supplier_table")
    suppliers = cur.fetchall()
    print("Suppliers:")
    for supplier in suppliers:
        print(supplier)

    cur.execute("SELECT * FROM product_table")
    products = cur.fetchall()
    print("\nProducts:")
    for product in products:
        print(product)

    cur.execute("SELECT * FROM order_table")
    orders = cur.fetchall()
    print("\nOrders:")
    for order in orders:
        print(order)

    # SQL query to find the most expensive product
        query = """
            SELECT 
                product_name,
                category,
                supplier_id,
                unit_price,
                quantity_in_stock,
                reorder_level,
                expiry_date
            FROM product_table
            ORDER BY unit_price DESC
            LIMIT 1;
        """
        
        # Execute the query
        cur.execute(query)

        # Fetch the result
        result = cur.fetchone()
        
        # Print the result
        if result:
            print("Most Expensive Product:")
            print(f"Name: {result[0]}")
            print(f"Category: {result[1]}")
            print(f"Supplier ID: {result[2]}")
            print(f"Unit Price: {result[3]}")
            print(f"Quantity in Stock: {result[4]}")
            print(f"Reorder Level: {result[5]}")
            print(f"Expiry Date: {result[6]}")
        else:
            print("No products found.")

# Run the functions
query_data()

# Close the cursor and connection
cur.close()
CONN.close()

  

