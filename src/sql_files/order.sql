-- Create the order table
CREATE TABLE order_table (
    order_id SERIAL PRIMARY KEY,
    product_id INT NOT NULL REFERENCES product_table(product_id),
    order_quantity NUMERIC(5) NOT NULL CHECK (order_quantity >= 0),
    order_date DATE NOT NULL
);

-- Example inserts into order_table
INSERT INTO order_table (product_id, order_quantity, order_date)
VALUES 
(1, 100, '2024-06-01'),
(2, 20, '2024-06-02');