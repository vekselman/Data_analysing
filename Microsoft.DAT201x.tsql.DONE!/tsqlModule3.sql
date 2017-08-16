--Challenge 1: Generate Invoice Reports
--1.Retrieve customer orders
SELECT sc.CompanyName, ss.SalesOrderID
FROM SalesLT.Customer as sc
	INNER JOIN SalesLT.SalesOrderHeader as ss
		ON sc.CustomerID = ss.CustomerID
ORDER BY sc.CustomerID;
--2.Retrieve customer orders with addresses
SELECT sc.FirstName + ' ' + ISNULL(sc.MiddleName,'') + ' ' + sc.LastName as CustomerName,
	sa.AddressLine1,sa.AddressLine2,sa.City,sa.StateProvince,sa.PostalCode,sa.CountryRegion
FROM SalesLT.Customer as sc
	INNER JOIN SalesLT.CustomerAddress as sca
		ON sc.CustomerID = sca.CustomerID AND sca.AddressType = 'Main Office'
	INNER JOIN SalesLT.Address as sa
		ON sca.AddressID = sa.AddressID;

--Challenge 2: Retrieve Sales Data
--1.Retrieve a list of all customers and their orders
SELECT sc.CustomerID,sc.CompanyName, sc.FirstName + ' ' + sc.LastName as CustomerName,
	sso.SalesOrderID,sso.TotalDue
FROM SalesLT.Customer as sc
	LEFT JOIN SalesLT.SalesOrderHeader as sso
		ON sc.CustomerID = sso.CustomerID
ORDER BY sso.SalesOrderID DESC;
--2.Retrieve a list of customers with no address
SELECT sc.CustomerID, sc.CompanyName, sc.FirstName + ' ' + sc.LastName, sc.Phone
FROM SalesLT.Customer as sc
	LEFT JOIN SalesLT.CustomerAddress as sa
		ON sc.CustomerID = sa.CustomerID
WHERE sa.AddressID IS NOT NULL;
--3.Retrieve a list of customers and products without orders
SELECT c.CustomerID,p.ProductID
FROM SalesLT.Customer AS c
	FULL JOIN SalesLT.SalesOrderHeader AS oh
		ON c.CustomerID = oh.CustomerID
	FULL JOIN SalesLT.SalesOrderDetail AS od
		ON od.SalesOrderID = oh.SalesOrderID
	FULL JOIN SalesLT.Product AS p
		ON p.ProductID = od.ProductID
WHERE oh.SalesOrderID IS NULL
ORDER BY od.ProductID, c.CustomerID;
	
SELECT *
FROM SalesLT.Product;
SELECT *
FROM SalesLT.SalesOrderHeader;
SELECT *
FROM SalesLT.SalesOrderDetail;