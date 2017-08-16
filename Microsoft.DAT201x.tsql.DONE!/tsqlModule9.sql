--Challenge 1: Inserting Products
--1.Insert a product
/*--Get All nullable culumns
SELECT tinfo.COLUMN_NAME, tinfo.IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS as tinfo
WHERE TABLE_SCHEMA = 'SalesLT' and TABLE_NAME = 'Product'
ORDER BY tinfo.IS_NULLABLE DESC;
sp_help 'SalesLT.Product'
*/
-- Finish the INSERT statement
INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, ProductCategoryID, SellStartDate)
VALUES
('LED Lights', 'LT-L123', 2.56, 12.99, 37, GETDATE());

-- Get last identity value that was inserted
SELECT SCOPE_IDENTITY();

-- Finish the SELECT statement
SELECT * FROM SalesLT.Product
WHERE ProductID = SCOPE_IDENTITY();
--2.Insert a new category with two products
INSERT INTO SalesLT.ProductCategory (Name, ParentProductCategoryID)
VALUES
('Bells and Horns', 4);

SELECT * FROM SalesLT.ProductCategory as pc
WHERE pc.ProductCategoryID = SCOPE_IDENTITY();

-- Insert product category
/*
INSERT INTO SalesLT.ProductCategory (ParentProductCategoryID, Name)
VALUES
(4, 'Bells and Horns');
*/
-- Insert 2 products
INSERT INTO SalesLT.Product (Name, ProductNumber, StandardCost, ListPrice, ProductCategoryID, SellStartDate)
VALUES
('Bicycle Bell', 'BB-RING', 2.47, 4.99, IDENT_CURRENT('SalesLT.ProductCategory'), GETDATE()),
('Bicycle Horn', 'BB-PARP', 1.29, 3.75, IDENT_CURRENT('SalesLT.ProductCategory'), GETDATE());

-- Check if products are properly inserted
SELECT c.Name As Category, p.Name AS Product
FROM SalesLT.Product AS p
JOIN SalesLT.ProductCategory as c ON p.ProductCategoryID = c.ProductCategoryID
WHERE p.ProductCategoryID = IDENT_CURRENT('SalesLT.ProductCategory');

--Challenge 2: Updating Products
--1.Update product prices
UPDATE SalesLT.Product
SET ListPrice = ListPrice * 1.1
WHERE ProductCategoryID =
  (SELECT ProductCategoryID FROM SalesLT.ProductCategory WHERE Name = 'Bells and Horns');

SELECT *
FROM SalesLT.Product
WHERE ProductCategoryID = (SELECT ProductCategoryID FROM SalesLT.ProductCategory WHERE Name = 'Bells and Horns');
--2.Discontinue products
UPDATE SalesLT.Product
SET DiscontinuedDate = GETDATE()
WHERE ProductCategoryID = 37 AND ProductNumber <> 'LT-L123';

SELECT *
FROM SalesLT.Product
WHERE ProductCategoryID = 37 AND ProductNumber <> 'LT-L123';

--Challenge 3: Deleting Products
--1.Delete a product category and its products
-- Delete records from the SalesLT.Product table
DELETE FROM SalesLT.Product
WHERE ProductCategoryID =
	(SELECT ProductCategoryID FROM SalesLT.ProductCategory WHERE Name = 'Bells and Horns');

-- Delete records from the SalesLT.ProductCategory table
DELETE FROM SalesLT.ProductCategory
WHERE ProductCategoryID =
	(SELECT ProductCategoryID FROM SalesLT.ProductCategory WHERE Name = 'Bells and Horns');


SELECT *
FROM SalesLT.ProductCategory
ORDER BY CASE WHEN ProductCategoryID = (
	SELECT ProductCategoryID FROM SalesLT.ProductCategory Where Name = 'Bells and Horns'
	) THEN 1 ELSE 2 END, ProductCategoryID;