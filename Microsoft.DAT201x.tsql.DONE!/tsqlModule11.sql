--Challenge 1: Logging Errors
--1.Throw an error for non-existent orders
DECLARE @OrderID int = 0

IF NOT EXISTS(SELECT * FROM SalesLT.SalesOrderHeader WHERE SalesOrderID = @OrderID)
BEGIN
	-- Throw a custom error if the specified order doesn't exist
	DECLARE @error varchar(25) = 'Order #' + cast(@OrderID as varchar) + ' does not exist';
	THROW 50001, @error, 0
END
ELSE
BEGIN
	DELETE FROM SalesLT.SalesOrderDetail WHERE SalesOrderID = @OrderID;
	DELETE FROM SalesLT.SalesOrderHeader WHERE SalesOrderID = @OrderID;
END
--2.Handle errors
DECLARE @OrderID int = 0

-- Wrap IF ELSE in a TRY block
BEGIN TRY
    IF NOT EXISTS (SELECT * FROM SalesLT.SalesOrderHeader WHERE SalesOrderID = @OrderID)
    BEGIN
    	-- Throw a custom error if the specified order doesn't exist
    	DECLARE @error varchar(25) = 'Order #' + cast(@OrderID as varchar) + ' does not exist';
    	THROW 50001, @error, 0
    END
    ELSE
    BEGIN
    	DELETE FROM SalesLT.SalesOrderDetail WHERE SalesOrderID = @OrderID;
      DELETE FROM SalesLT.SalesOrderHeader WHERE SalesOrderID = @OrderID;
    END
END TRY
-- Add a CATCH block to print out the error
BEGIN CATCH
	-- Catch and print the error
	PRINT ERROR_MESSAGE();
END CATCH

--Challenge 2: Ensuring Data Consistency
--1.
DECLARE @OrderID int = 0

BEGIN TRY
	IF NOT EXISTS(SELECT * FROM SalesLT.SalesOrderHeader
				   WHERE SalesOrderID = @OrderID)
	BEGIN
		-- Throw a custom error if the specified order doesn't exist
		DECLARE @error varchar(25);
		SET @error = 'Order #' + cast(@OrderID as varchar) + ' does not exist';
		THROW 50001, @error, 0
	END
	ELSE
	BEGIN
	  BEGIN TRANSACTION
		DELETE FROM SalesLT.SalesOrderDetail
		WHERE SalesOrderID = @OrderID;

		THROW 50001, 'Unexpected error', 0 --Uncomment to test transaction

		DELETE FROM SalesLT.SalesOrderHeader
		WHERE SalesOrderID = @OrderID;
	  COMMIT TRANSACTION
	END
END TRY
BEGIN CATCH
	IF @@TRANCOUNT > 0
	BEGIN
		-- Rollback the transaction and re-throw the error
		ROLLBACK TRANSACTION;
		THROW;
	END
	ELSE
	BEGIN
		-- Report the error
		PRINT ERROR_MESSAGE();
	END
END CATCH