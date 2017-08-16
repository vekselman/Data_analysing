--Challenge 1: Retrieve Product Information
--1.Retrieve the name and approximate weight of each product
SELECT CONCAT(sp.ProductID, ' ' + UPPER(sp.Name)) as ProductIDName, ROUND(sp.Weight,-1) as ApproxWeight
FROM SalesLT.Product as sp
ORDER BY ApproxWeight DESC;
--2.Retrieve the year and month in which products were first sold
SELECT CONCAT(sp.ProductID, ' ' + UPPER(sp.Name)) as ProductIDName, ROUND(sp.Weight,-1) as ApproxWeight,
	YEAR(sp.SellStartDate) as SellStartYear, DATENAME(MONTH,sp.SellStartDate) as SellStartMonth
FROM SalesLT.Product as sp
ORDER BY ApproxWeight DESC;
--3.Extract product types from product numbers
SELECT CONCAT(sp.ProductID, ' ' + UPPER(sp.Name)) as ProductIDName, ROUND(sp.Weight,-1) as ApproxWeight,
	YEAR(sp.SellStartDate) as SellStartYear, DATENAME(MONTH,sp.SellStartDate) as SellStartMonth,
	LEFT(sp.ProductNumber,2) as ProductType
FROM SalesLT.Product as sp
ORDER BY ApproxWeight DESC;
--4.Retrieve only products with a numeric size
SELECT CONCAT(sp.ProductID, ' ' + UPPER(sp.Name)) as ProductIDName, ROUND(sp.Weight,-1) as ApproxWeight,
	YEAR(sp.SellStartDate) as SellStartYear, DATENAME(MONTH,sp.SellStartDate) as SellStartMonth,
	LEFT(sp.ProductNumber,2) as ProductType, sp.ProductNumber
FROM SalesLT.Product as sp
WHERE ISNUMERIC(SUBSTRING(ProductNumber,LEN(ProductNumber) - CHARINDEX('-',REVERSE(RIGHT(ProductNumber,3)))+2,2)) = 1
ORDER BY ApproxWeight DESC;

--Challenge 2: Rank Customers by Revenue
--1.Retrieve total sales by product
SELECT sc.CompanyName,
	RANK() OVER(ORDER BY soh.TotalDue DESC) as Ranking
FROM SalesLT.SalesOrderHeader as soh
	JOIN SalesLT.Customer as sc
		ON soh.CustomerID = sc.CustomerID
ORDER BY soh.TotalDue DESC;

--Challenge 3: Aggregate Product Sales
--1.Retrieve total sales by product
SELECT sp.Name, SUM(ISNULL(ssod.LineTotal,0.00)) as TotalSum
FROM SalesLT.Product as sp
	JOIN SalesLT.SalesOrderDetail as ssod
		ON sp.ProductID = ssod.ProductID
GROUP BY sp.Name;
--2.Filter the product sales list to include only products that cost over $1,000
SELECT sp.Name, SUM(ISNULL(ssod.LineTotal,0.00)) as TotalSum
FROM SalesLT.Product as sp
	JOIN SalesLT.SalesOrderDetail as ssod
		ON sp.ProductID = ssod.ProductID
WHERE ssod.UnitPrice > 1000
GROUP BY sp.Name
ORDER BY TotalSum;
--3.Filter the product sales groups to include only total sales over $20,000
SELECT sp.Name, SUM(ISNULL(ssod.LineTotal,0.00)) as TotalSum
FROM SalesLT.Product as sp
	JOIN SalesLT.SalesOrderDetail as ssod
		ON sp.ProductID = ssod.ProductID
GROUP BY sp.Name
HAVING SUM(ISNULL(ssod.LineTotal,0.00)) > 20000
ORDER BY TotalSum;