-- Create the supplier table
CREATE TABLE supplier_table (
    supplier_id SERIAL PRIMARY KEY,
    supplier_name VARCHAR(50) NOT NULL
);



-- Insert suppliers into supplier_table
INSERT INTO supplier_table (supplier_name)
VALUES 
('BBraun'),
('Hartmann'),
('Pascorbin'),
('ViktoriaApotheke'),
('ArnikaManufaktur');
