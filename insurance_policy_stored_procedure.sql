CREATE PROCEDURE GetCustomerPolicyDetails
    @CustomerID INT
AS
BEGIN
    -- This procedure retrieves detailed information about insurance policies
    -- for a specific customer identified by CustomerID.

    -- Check for the existence of the CustomerID in the database.
    IF NOT EXISTS (SELECT * FROM Customers WHERE CustomerID = @CustomerID)
    BEGIN
        PRINT 'No customer found with the provided CustomerID.';
        RETURN;
    END

    -- Retrieve policy details for the given CustomerID.
    SELECT 
        p.PolicyNumber,
        p.PolicyType,
        p.StartDate,
        p.EndDate,
        p.PremiumAmount,
        c.FirstName,
        c.LastName
    FROM 
        Policies p
    JOIN 
        Customers c ON p.CustomerID = c.CustomerID
    WHERE 
        p.CustomerID = @CustomerID;

    -- This is a simple procedure without complex business logic or transactions.
    -- It can be extended to include more sophisticated features as needed.
END;
