import sqlite3
import csv
import os
from datetime import datetime

def get_data_path(filename):
    """Get absolute path to data file"""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    if filename.startswith('AdventureWorks Sales Data'):
        return os.path.join(base_dir, 'data', 'sales', filename)
    return os.path.join(base_dir, 'data', filename)

def get_db_path():
    """Get absolute path to database file"""
    base_dir = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base_dir, 'database', 'adventureworks.db')

def import_territory():
    """Import Territory data"""

    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        with open(get_data_path('AdventureWorks Territory Lookup.csv'), 'r') as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO Territory (TerritoryKey, Region, Country, Continent)
                    VALUES (?, ?, ?, ?)
                ''', (row['SalesTerritoryKey'], row['Region'], row['Country'], row['Continent']))
        conn.commit()

def import_product_categories():
    """Import Product Categories data"""
    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        with open(get_data_path('AdventureWorks Product Categories Lookup.csv'), 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO ProductCategory (ProductCategoryKey, CategoryName)
                    VALUES (?, ?)
                ''', (row['ProductCategoryKey'], row['CategoryName']))
        conn.commit()

def import_product_subcategories():
    """Import Product Subcategories data"""
    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        with open(get_data_path('AdventureWorks Product Subcategories Lookup.csv'), 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO ProductSubcategory (ProductSubcategoryKey, SubcategoryName, ProductCategoryKey)
                    VALUES (?, ?, ?)
                ''', (row['ProductSubcategoryKey'], row['SubcategoryName'], row['ProductCategoryKey']))
        conn.commit()

def import_products():
    """Import Products data"""
    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        with open(get_data_path('AdventureWorks Product Lookup.csv'), 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                cursor.execute('''
                    INSERT INTO Product (
                        ProductKey, ProductSubcategoryKey, ProductSKU, ProductName,
                        ModelName, ProductDescription, ProductColor, ProductSize,
                        ProductStyle, ProductCost, ProductPrice
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['ProductKey'], row['ProductSubcategoryKey'], row['ProductSKU'],
                    row['ProductName'], row['ModelName'], row['ProductDescription'],
                    row['ProductColor'], row['ProductSize'], row['ProductStyle'],
                    row['ProductCost'], row['ProductPrice']
                ))
        conn.commit()

def import_customers():
    """Import Customers data"""
    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        with open(get_data_path('AdventureWorks Customer Lookup.csv'), 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                if not row['CustomerKey'].strip():  # Skip empty rows
                    continue
                # Convert date string to datetime object
                birth_date = datetime.strptime(row['BirthDate'], '%Y-%m-%d')
                cursor.execute('''
                    INSERT INTO Customer (
                        CustomerKey, Prefix, FirstName, LastName, BirthDate,
                        MaritalStatus, Gender, EmailAddress, AnnualIncome,
                        TotalChildren, EducationLevel, Occupation, HomeOwner
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    row['CustomerKey'], row['Prefix'], row['FirstName'], row['LastName'],
                    birth_date, row['MaritalStatus'], row['Gender'],
                    row['EmailAddress'], row['AnnualIncome'], row['TotalChildren'],
                    row['EducationLevel'], row['Occupation'], row['HomeOwner']
                ))
        conn.commit()

def import_sales():
    """Import Sales data for 2020-2022"""
    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        for year in ['2020', '2021', '2022']:
            filename = f'AdventureWorks Sales Data {year}.csv'
            with open(get_data_path(filename), 'r') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    cursor.execute('''
                        INSERT INTO Sales (
                            OrderDate, StockDate, OrderNumber, ProductKey,
                            CustomerKey, TerritoryKey, OrderLineItem, OrderQuantity
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (
                        row['OrderDate'], row['StockDate'], row['OrderNumber'],
                        row['ProductKey'], row['CustomerKey'], row['TerritoryKey'],
                        row['OrderLineItem'], row['OrderQuantity']
                    ))
            conn.commit()

def import_returns():
    """Import Returns data"""
    with sqlite3.connect(get_db_path()) as conn:
        cursor = conn.cursor()
        with open(get_data_path('AdventureWorks Returns Data.csv'), 'r') as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:
                if not all(row.values()):  # Skip empty rows
                    continue
                cursor.execute('''
                    INSERT INTO Returns (TerritoryKey, ReturnDate, ProductKey, ReturnQuantity)
                    VALUES (?, ?, ?, ?)
                ''', (
                    row['TerritoryKey'], row['ReturnDate'],
                    row['ProductKey'], row['ReturnQuantity']
                ))
        conn.commit()

def main():
    """Import all data in the correct order"""
    print("Starting data import...")
    
    import_territory()
    print("Territory data imported")
    
    import_product_categories()
    print("Product categories imported")
    
    import_product_subcategories()
    print("Product subcategories imported")
    
    import_products()
    print("Products imported")
    
    import_customers()
    print("Customers imported")
    
    import_sales()
    print("Sales data imported")
    
    import_returns()
    print("Returns data imported")
    
    print("Data import completed successfully")

if __name__ == "__main__":
    main() 