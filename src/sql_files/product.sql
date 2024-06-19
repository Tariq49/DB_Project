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


-- Insert products into product_table
INSERT INTO product_table (product_name, category, supplier_id, unit_price, quantity_in_stock, reorder_level, expiry_date)
VALUES 
('Intrafix Safeset', 'infusion set', 1, 0.90, 100, 10, '2026-11-01'),
('NaCl 0.9% 100ml', 'Fluids', 1, 1.21, 20, 3, '2027-01-01'),
('NaCl 0.9% 250ml', 'Fluids', 1, 1.26, 10, 3, '2027-01-01'),
('Vasofix Safety', 'Needle(22G)', 1, 0.86, 14, 3, '2027-12-01'),
('Cosmopor I.V.', 'Dressing for securing IV cannula', 2, 0.54, 23, 3, '2028-03-01'),
('Transofix', 'transferset sterile fluids', 1, 0.39, 30, 3, '2028-10-01'),
('VitaminC 7.5 gr', 'ampoule', 3, 11.86, 10, 1, '2025-05-01'),
('ElectrolyteComplete', 'ampoule', 4, 17.90, 5, 1, '2025-04-21'),
('Glutathion3000mg', 'ampoule', 5, 48.90, 6, 1, '2024-09-21'),
('ATP Konzentrat', 'ampoule', 5, 15.00, 14, 1, '2025-01-10');