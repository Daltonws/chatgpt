# Insurance Stored Procedure BRD Generator

This tool is designed to generate a Business Requirements Document (BRD) for a given insurance stored procedure. It leverages the OpenAI ChatGPT model to interpret the stored procedure and create a comprehensive BRD.

## Getting Started

These instructions will guide you on how to use the Insurance Stored Procedure BRD Generator.

### Prerequisites

- Python 3.x
- `requests` library (Install using `pip install requests`)
- An active OpenAI API key

### Installation

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Install the `requests` library using `pip`.

### Usage

1. Run the script `insurance_brd_generator.py` in your Python environment.
2. When prompted, enter your stored procedure. Type `END` on a new line to submit your input.
3. The script will communicate with the OpenAI API and return a BRD based on your input.

### Example Stored Procedure

Here's an example of an insurance stored procedure that you can use as input:

```sql
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
