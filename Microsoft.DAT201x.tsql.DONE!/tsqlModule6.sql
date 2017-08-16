--Challenge 1: Retrieve Product Price Information
--1.Retrieve products whose list price is higher than the average unit price
SELECT sp.ProductID, sp.Name, sp.ListPrice
FROM SalesLT.Product as sp
WHERE sp.ListPrice > (SELECT AVG(ssod.UnitPrice)
						FROM SalesLT.SalesOrderDetail as ssod)
ORDER BY sp.ListPrice;
--2.Retrieve Products with a list price of $100 or more that have been sold for less than $100
SELECT sp.ProductID, sp.Name, sp.ListPrice 
FROM SalesLT.Product as sp
WHERE sp.ListPrice >= 100 AND sp.ProductID IN (SELECT ssod.ProductID
												FROM SalesLT.SalesOrderDetail as ssod
												WHERE ssod.UnitPrice < 100)
ORDER BY sp.ListPrice;
--3.Retrieve the cost, list price, and average selling price for each product
SELECT sp.ProductID, sp.Name, sp.ListPrice,
	(SELECT AVG(ISNULL(ssod.UnitPrice,0.0)) FROM SalesLT.SalesOrderDetail as ssod
		WHERE ssod.ProductID = sp.ProductID) as AVGUnitSold
FROM SalesLT.Product as sp;
--4.Retrieve products that have an average selling price that is lower than the cost
SELECT sp.ProductID, sp.Name, sp.ListPrice,
	(SELECT AVG(ISNULL(ssod.UnitPrice,0.0)) FROM SalesLT.SalesOrderDetail as ssod
		WHERE ssod.ProductID = sp.ProductID) as AVGUnitSold
FROM SalesLT.Product as sp
WHERE sp.ListPrice > (SELECT AVG(ISNULL(ssod.UnitPrice,0.0)) FROM SalesLT.SalesOrderDetail as ssod
						WHERE ssod.ProductID = sp.ProductID);

--Challenge 2: Retrieve Customer Information
--1.Retrieve customer information for all sales orders
SELECT ssoh.SalesOrderID,ssoh.CustomerID, cinfo.FirstName, cinfo.LastName ,ssoh.TotalDue
FROM SalesLT.SalesOrderHeader as ssoh
	CROSS APPLY dbo.ufnGetCustomerInformation(ssoh.CustomerID) as cinfo
--2.
SELECT cinfo.CustomerID, cinfo.FirstName, cinfo.LastName, sa.AddressLine1, sa.City
FROM SalesLT.Address as sa
	JOIN SalesLT.CustomerAddress as sca
		ON sa.AddressID = sca.AddressID
	CROSS APPLY dbo.ufnGetCustomerInformation(sca.CustomerID) as cinfo