--Challenge 1: Retrieve Customer Data
--1.
SELECT	* FROM SalesLT.Customer;
--2.
SELECT Title + ' ' + FirstName + ' ' + isnull(MiddleName,'')
	+ ' ' + LastName + ' ' +  ISNULL(Suffix,'') as SomeColamn		
FROM SalesLT.Customer;
--3.
SELECT 
	SalesPerson AS SalesPerson,
	Title + ' ' + LastName AS CustomerName,
	Phone AS PhoneNumber
FROM SalesLT.Customer;

--Challenge 2: Retrieve Customer and Sales Data
--1.
SELECT CAST(CustomerID as nvarchar(5)) + ': ' + CompanyName  
		as CompanyName
FROM SalesLT.Customer
ORDER BY CustomerID;
--2.
SELECT CAST(SalesOrderNumber AS nvarchar(8)) 
	+ '(' + CAST(RevisionNumber as nvarchar(1)) +')' as OrderNumber,
	CONVERT(varchar(10),OrderDate,102) as OrderDate
FROM SalesLT.SalesOrderHeader;

--Challenge 3: Retrieve Customer Contact Details
--1.
SElECT FirstName + ' ' + ISNULL(MiddleName,'') + ' ' + LastName
		as CustomerFullName
FROM SalesLT.Customer;
--2.
/* Use before complite the task
UPDATE SalesLT.Customer
SET EmailAddress = NULL
WHERE CustomerID % 7 = 1;
*/
SELECT CustomerID as CustomerID,
	COALESCE(EmailAddress,Phone) as PrimaryContact
FROM SalesLT.Customer
ORDER BY CustomerID;
--3.
/*Use Before task
UPDATE SalesLT.SalesOrderHeader
SET ShipDate = NULL
WHERE SalesOrderID > 71899;
*/
SELECT SalesOrderID as SalesOrderID,
		CASE
			WHEN ShipDate is null THEN 'Awaiting Shipment'
			ELSE 'Shipped ' + CONVERT(varchar(10),ShipDate,102)
		END as ShippingStatus 
FROM SalesLT.SalesOrderHeader;


SELECT CustomerID as CustomerID
FROM SalesLT.SalesOrderHeader
Order BY CustomerID
OFFSET 5 ROWS
FETCH NEXT 10 ROWS ONLY;