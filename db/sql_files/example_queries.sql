-- example Queries


--list all products with their suppliers
SELECT 
    p.product_name,
    p.category,
    p.unit_price,
    p.quantity_in_stock,
    s.supplier_name
FROM product_table p
JOIN supplier_table s ON p.supplier_id = s.supplier_id;

-- find products that need to be reordered
SELECT 
    product_name,
    quantity_in_stock,
    reorder_level
FROM 
    product_table
WHERE 
    quantity_in_stock <= reorder_level;

-- total quantity of each product ordered

SELECT p.product_name, SUM(o.order_quantity) AS total_quantity_ordered
FROM order_table o
JOIN product_table p ON o.product_id = p.product_id
GROUP BY p.product_name;

-- List all products that are expiring soon (within the next month)

SELECT 
    product_name,
    category,
    supplier_id,
    unit_price,
    quantity_in_stock,
    reorder_level,
    expiry_date
FROM product_table
WHERE expiry_date <= CURRENT_DATE + INTERVAL '1 month';

-- list all products with the name 'BBraun'
SELECT 
    p.product_name,
    p.category,
    p.unit_price,
    p.quantity_in_stock,
    p.reorder_level,
    p.expiry_date
FROM product_table p
JOIN supplier_table s ON p.supplier_id = s.supplier_id
WHERE s.supplier_name = 'BBraun';


-- Find the most expensive ampoule? 
SELECT 
    product_name,
    unit_price
FROM product_table
WHERE category = 'ampoule'
ORDER BY unit_price DESC
LIMIT 1;

--Find the most expensive product;
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

--find least expensive product?
SELECT product_name, unit_price FROM product_table ORDER BY unit_price ASC LIMIT 1; 

-- list all products according to price in ascending order
SELECT product_name, unit_price FROM product_table ORDER BY unit_price ASC; 


-- Which ampoules are  expiring within the next 6 months? 
SELECT 
    product_name,
    category,
    supplier_id,
    unit_price,
    quantity_in_stock,
    reorder_level,
    expiry_date
FROM product_table
WHERE category = 'ampoule' AND expiry_date <= CURRENT_DATE + INTERVAL '6 months';






