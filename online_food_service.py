#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector as sql

cnx=sql.connect(host='127.0.0.1', user='root', 
                password='Indhu@33', 
                database='online_food_service',
                auth_plugin='mysql_native_password')
if cnx.is_connected()==False:
                print('Not connected')
else:
                print('Database Connected....')


# In[1]:


import mysql.connector

hostname = 'localhost'
username = 'root'
password = 'Indhu@33'
database_name = 'online_food_service'

try:
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password
    )
    if connection.is_connected():
        print("Connected to MySQL server")
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created or already exists")

        cursor.execute(f"USE {database_name}")
        print(f"Using database '{database_name}'")

        sql_commands = [
            """
            CREATE TABLE IF NOT EXISTS restaurants (
                restaurant_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                location VARCHAR(255),
                phone VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE,
                phone VARCHAR(20),
                address TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS menus (
                menu_id INT PRIMARY KEY AUTO_INCREMENT,
                restaurant_id INT,
                item_name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS homemade_foods (
                homemade_food_id INT PRIMARY KEY AUTO_INCREMENT,
                restaurant_id INT,
                item_name TEXT,
                price DECIMAL(10, 2),
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS foods (
                food_id INT AUTO_INCREMENT PRIMARY KEY,
                food_name VARCHAR(100) NOT NULL,
                is_veg BOOLEAN NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                description TEXT
            )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS customer_foods (
                food_id INT AUTO_INCREMENT PRIMARY KEY,
                food_name VARCHAR(100) NOT NULL,
                seller_name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                description TEXT
            )
            """
        ]

        for sql_command in sql_commands:
            try:
                cursor.execute(sql_command)
            except mysql.connector.Error as err:
                print(f"Error executing command: {sql_command}")
                print(f"Error message: {err}")

        # Commit the changes
        connection.commit()
        print("Tables created successfully")

    else:
        print("Failed to connect to MySQL server")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# In[2]:


import mysql.connector

hostname = 'localhost'
username = 'root'
password = 'Indhu@33'
database_name = 'online_food_service'

try:
    connection = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password
    )
    if connection.is_connected():
        print("Connected to MySQL server")
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database '{database_name}' created or already exists")

        cursor.execute(f"USE {database_name}")
        print(f"Using database '{database_name}'")

        sql_commands = [
            """
            CREATE TABLE IF NOT EXISTS restaurants (
                restaurant_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                location VARCHAR(255),
                phone VARCHAR(20)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) UNIQUE,
                phone VARCHAR(20),
                address TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS menus (
                menu_id INT PRIMARY KEY AUTO_INCREMENT,
                restaurant_id INT,
                item_name VARCHAR(255) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS homemade_foods (
                homemade_food_id INT PRIMARY KEY AUTO_INCREMENT,
                restaurant_id INT,
                item_name TEXT,
                price DECIMAL(10, 2),
                FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS foods (
                food_id INT AUTO_INCREMENT PRIMARY KEY,
                food_name VARCHAR(100) NOT NULL,
                is_veg BOOLEAN NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                description TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS customer_foods (
                food_id INT AUTO_INCREMENT PRIMARY KEY,
                food_name VARCHAR(100) NOT NULL,
                seller_name VARCHAR(100) NOT NULL,
                price DECIMAL(10, 2) NOT NULL,
                description TEXT
            )
            """
        ]

        for sql_command in sql_commands:
            try:
                cursor.execute(sql_command)
            except mysql.connector.Error as err:
                print(f"Error executing command: {sql_command}")
                print(f"Error message: {err}")

        # Insert sample data into tables
        insert_commands = [
            """
            INSERT INTO restaurants (name, location, phone)
            VALUES ('Good Eats', '123 Food Street', '555-5555'),
                   ('Tasty Treats', '456 Snack Ave', '555-1234'),
                   ('Homemade Heaven', '789 Comfort Rd', '555-7890'),
                   ('Food Paradise', '101 Gourmet Blvd', '555-1111'),
                   ('Snack Shack', '202 Tasty Ln', '555-2222'),
                   ('Delight Diner', '303 Yum Ave', '555-3333'),
                   ('Savor Spot', '404 Flavor Rd', '555-4444'),
                   ('Bite Bistro', '505 Crave St', '555-5556')
            """,
            """
            INSERT INTO users (name, email, phone, address)
            VALUES ('Kaviya', 'kaviya@example.com', '555-0011', '101 Main St'),
                   ('Indhu', 'indhu@example.com', '555-0022', '202 First Ave'),
                   ('Mahesh', 'mahesh@example.com', '555-0033', '303 Second St'),
                   ('Anu', 'anu@example.com', '555-0044', '404 Third St'),
                   ('Vikram', 'vikram@example.com', '555-0055', '505 Fourth Ave'),
                   ('Rani', 'rani@example.com', '555-0066', '606 Fifth St'),
                   ('Arjun', 'arjun@example.com', '555-0077', '707 Sixth Ave'),
                   ('Nisha', 'nisha@example.com', '555-0088', '808 Seventh St')
            """,
            """
            INSERT INTO menus (restaurant_id, item_name, price)
            VALUES (1, 'Burger', 5.99),
                   (1, 'Fries', 2.99),
                   (2, 'Pizza', 8.99),
                   (2, 'Salad', 4.99),
                   (3, 'Pasta', 7.99),
                   (3, 'Soup', 3.99),
                   (4, 'Steak', 14.99),
                   (4, 'Garlic Bread', 2.49),
                   (5, 'Sandwich', 4.99),
                   (5, 'Nachos', 3.49),
                   (6, 'Fried Chicken', 9.99),
                   (6, 'Coleslaw', 1.99),
                   (7, 'Sushi', 12.99),
                   (7, 'Miso Soup', 2.99),
                   (8, 'Tacos', 6.99),
                   (8, 'Burrito', 7.99)
            """,
            """
            INSERT INTO homemade_foods (restaurant_id, item_name, price)
            VALUES (3, 'Homemade Pie', 10.99),
                   (3, 'Homemade Bread', 3.49),
                   (4, 'Homemade Cake', 15.99),
                   (4, 'Homemade Cookies', 4.49),
                   (5, 'Homemade Salsa', 5.99),
                   (5, 'Homemade Guacamole', 6.49),
                   (6, 'Homemade Pudding', 3.99),
                   (6, 'Homemade Granola', 4.99),
                   (7, 'Homemade Smoothie', 6.99),
                   (7, 'Homemade Ice Cream', 7.49)
            """,
            """
            INSERT INTO foods (food_name, is_veg, price, description)
            VALUES ('Veggie Burger', TRUE, 5.49, 'Delicious veggie burger'),
                   ('Chicken Burger', FALSE, 6.49, 'Tasty chicken burger'),
                   ('Grilled Cheese', TRUE, 3.99, 'Cheesy and grilled to perfection'),
                   ('Caesar Salad', TRUE, 4.99, 'Fresh and crisp salad'),
                   ('BBQ Ribs', FALSE, 12.99, 'Smoky and tender ribs'),
                   ('Veggie Pizza', TRUE, 7.99, 'Loaded with vegetables'),
                   ('Pepperoni Pizza', FALSE, 8.99, 'Classic pepperoni pizza'),
                   ('Fish Tacos', FALSE, 6.99, 'Spicy and tangy fish tacos'),
                   ('Lentil Soup', TRUE, 3.49, 'Healthy and hearty soup'),
                   ('Beef Stew', FALSE, 9.99, 'Rich and savory stew')
            """,
            """
            INSERT INTO customer_foods (food_name, seller_name, price, description)
            VALUES ('Homemade Cookies', 'Sarah Lee', 4.99, 'Freshly baked cookies'),
                   ('Homemade Jam', 'John Doe', 3.99, 'Organic strawberry jam'),
                   ('Homemade Pickles', 'Emily Clark', 5.99, 'Crunchy and tangy pickles'),
                   ('Homemade Pasta', 'Carlos Sanchez', 7.99, 'Handmade pasta with love'),
                   ('Homemade Bread', 'Sophia Wilson', 4.49, 'Warm and fluffy bread'),
                   ('Homemade Cheese', 'David Kim', 6.99, 'Rich and creamy cheese'),
                   ('Homemade Granola', 'Rachel Adams', 4.99, 'Healthy and crunchy granola'),
                   ('Homemade BBQ Sauce', 'James Brown', 5.49, 'Smoky and flavorful sauce'),
                   ('Homemade Peanut Butter', 'Linda Green', 3.99, 'Smooth and nutty butter'),
                   ('Homemade Lemonade', 'Alex White', 2.49, 'Refreshing and tangy lemonade')
            """
        ]

        for insert_command in insert_commands:
            try:
                cursor.execute(insert_command)
            except mysql.connector.Error as err:
                print(f"Error executing command: {insert_command}")
                print(f"Error message: {err}")

        # Commit the changes
        connection.commit()
        print("Tables created and data inserted successfully")

    else:
        print("Failed to connect to MySQL server")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# In[ ]:




