--Challenge 1: Retrieve Product Information
--1.Retrieve product model descriptions
SELECT P.ProductID, P.Name AS ProductName, PM.Name AS ProductModel, PM.Summary
FROM SalesLT.Product AS P
	JOIN SalesLT.vProductModelCatalogDescription AS PM
		ON P.ProductModelID = PM.ProductModelID
ORDER BY ProductID;
--2.Create a table of distinct colors
DECLARE @Colors AS TABLE (Color nvarchar(15));

INSERT INTO @Colors
SELECT DISTINCT Color FROM SalesLT.Product;

SELECT ProductID, Name, Color
FROM SalesLT.Product
WHERE Color IN (SELECT Color FROM @Colors);
--3.Retrieve product parent categories
SELECT C.ParentProductCategoryName AS ParentCategory,
       C.ProductCategoryName AS Category,
       P.ProductID, P.Name AS ProductName
FROM SalesLT.Product AS P
	JOIN dbo.ufnGetAllCategories() AS C
		ON P.ProductCategoryID = C.ProductCategoryID
ORDER BY ParentCategory, Category, ProductName;

--Challenge 2: Retrieve Customer Sales Revenue
--1.Retrieve sales revenue by customer and contact
SELECT CustomerSales.CompanyContact, SUM(CustomerSales.SalesAmount) AS Revenue
FROM
	(SELECT CONCAT(c.CompanyName, CONCAT(' (' + c.FirstName + ' ', c.LastName + ')')), SOH.TotalDue
	 FROM SalesLT.SalesOrderHeader AS SOH
	 JOIN SalesLT.Customer AS c
	 ON SOH.CustomerID = c.CustomerID) AS CustomerSales(CompanyContact, SalesAmount)
GROUP BY CompanyContact
ORDER BY CompanyContact;