# AdventureWorks SQLite Database Creation

This document outlines the process of creating a SQLite database from AdventureWorks CSV data files.

## Database Schema

### Dimension Tables

1. **Territory**
   - TerritoryKey (PRIMARY KEY)
   - Region
   - Country
   - Continent

1. **Customer**
   - CustomerKey (PRIMARY KEY)
   - Prefix
   - FirstName
   - LastName
   - BirthDate
   - MaritalStatus
   - Gender
   - EmailAddress
   - AnnualIncome
   - TotalChildren
   - EducationLevel
   - Occupation
   - HomeOwner

1. **ProductCategory**
   - ProductCategoryKey (PRIMARY KEY)
   - CategoryName

1. **ProductSubcategory**
   - ProductSubcategoryKey (PRIMARY KEY)
   - SubcategoryName
   - ProductCategoryKey (FOREIGN KEY)

1. **Product**
   - ProductKey (PRIMARY KEY)
   - ProductSubcategoryKey (FOREIGN KEY)
   - ProductSKU
   - ProductName
   - ModelName
   - ProductDescription
   - ProductColor
   - ProductSize
   - ProductStyle
   - ProductCost
   - ProductPrice

### Fact Tables

1. **Sales**
   - OrderDate
   - StockDate
   - OrderNumber
   - ProductKey (FOREIGN KEY)
   - CustomerKey (FOREIGN KEY)
   - TerritoryKey (FOREIGN KEY)
   - OrderLineItem
   - OrderQuantity

1. **Returns**
   - TerritoryKey (FOREIGN KEY)
   - ReturnDate
   - ProductKey (FOREIGN KEY)
   - ReturnQuantity

## Implementation Steps

1. **Create Database Schema**
   - Create tables in order of dependencies
   - Implement all constraints
   - Define appropriate data types

2. **Data Import Order**
   ```
   1. Territory
   2. Product Categories
   3. Product Subcategories
   4. Products
   5. Customers
   6. Sales (2020, 2021, 2022)
   7. Returns
   ```

3. **Verification Queries**
   - Count rows in each table
   - Verify foreign key relationships
   - Check data integrity

## Source Files

### Dimension Data
- `AdventureWorks Territory Lookup.csv`
- `AdventureWorks Customer Lookup.csv`
- `AdventureWorks Product Categories Lookup.csv`
- `AdventureWorks Product Subcategories Lookup.csv`
- `AdventureWorks Product Lookup.csv`

### Fact Data
- Sales:
  - `AdventureWorks Sales Data 2020.csv`
  - `AdventureWorks Sales Data 2021.csv`
  - `AdventureWorks Sales Data 2022.csv`
- Returns:
  - `AdventureWorks Returns Data.csv`

## Data Types

SQLite supports the following storage classes which we'll use:
- TEXT: For strings and dates
- INTEGER: For whole numbers
- REAL: For decimal numbers
- BLOB: For binary data
- NULL: For null values

## Directory Structure 