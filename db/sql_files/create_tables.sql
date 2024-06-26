-- Create the order table
CREATE TABLE order_table (
    order_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES product_table(product_id),
    order_quantity NUMERIC(5) NOT NULL CHECK (order_quantity >= 0),
    order_date DATE NOT NULL
);


-- Create the product table
CREATE TABLE product_table (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50) NOT NULL,
    supplier_id INT NOT NULL REFERENCES supplier_table(supplier_id),
    unit_price NUMERIC(5,2) NOT NULL CHECK (unit_price >= 0),
    quantity_in_stock NUMERIC(5) NOT NULL CHECK (quantity_in_stock >= 0),
    reorder_level SMALLINT NOT NULL CHECK (reorder_level >= 0),
    expiry_date DATE NOT NULL
);

-- Create the supplier table
CREATE TABLE supplier_table (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(50) NOT NULL
);
