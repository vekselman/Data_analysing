--Challenge 1: Retrieve Customer Addresses
--1.Retrieve billing addresses
--2.Retrieve shipping addresses
--3.Combine billing and shipping addresses
SELECT sc.CompanyName, sca.AddressID, sa.AddressLine1,sa.City ,'Billing' as AddressType
FROM SalesLT.Customer as sc
	INNER JOIN SalesLT.CustomerAddress as sca
		ON sc.CustomerID = sca.CustomerID
	INNER JOIN SalesLT.Address as sa
		ON sca.AddressID = sa.AddressID
WHERE sca.AddressType = 'Main Office'
UNION ALL
	SELECT sc.CompanyName, sca.AddressID, sa.AddressLine1,sa.City ,'Shipping' as AddressType
	FROM SalesLT.Customer as sc
		INNER JOIN SalesLT.CustomerAddress as sca
			ON sc.CustomerID = sca.CustomerID
		INNER JOIN SalesLT.Address as sa
			ON sca.AddressID = sa.AddressID
	WHERE sca.AddressType = 'Shipping'
ORDER BY sc.CompanyName;

--Challenge 2: Filter Customer Addresses
--1.Retrieve customers with only a main office address
SELECT sc.CompanyName
FROM SalesLT.Customer as sc
	INNER JOIN SalesLT.CustomerAddress as sca
		ON sc.CustomerID = sca.CustomerID
	INNER JOIN SalesLT.Address as sa
		ON sca.AddressID = sa.AddressID
	WHERE sca.AddressType = 'Main Office'
EXCEPT
	SELECT sc.CompanyName
	FROM SalesLT.Customer as sc
		INNER JOIN SalesLT.CustomerAddress as sca
			ON sc.CustomerID = sca.CustomerID
		INNER JOIN SalesLT.Address as sa
			ON sca.AddressID = sa.AddressID
	WHERE sca.AddressType = 'Shipping';
--2.Retrieve only customers with both a main office address and a shipping address
SELECT sc.CompanyName
FROM SalesLT.Customer as sc
	INNER JOIN SalesLT.CustomerAddress as sca
		ON sc.CustomerID = sca.CustomerID
	INNER JOIN SalesLT.Address as sa
		ON sca.AddressID = sa.AddressID
	WHERE sca.AddressType = 'Main Office'
INTERSECT
	SELECT sc.CompanyName
	FROM SalesLT.Customer as sc
		INNER JOIN SalesLT.CustomerAddress as sca
			ON sc.CustomerID = sca.CustomerID
		INNER JOIN SalesLT.Address as sa
			ON sca.AddressID = sa.AddressID
	WHERE sca.AddressType = 'Shipping';