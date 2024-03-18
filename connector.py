import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="107220Mwangi@",
    database="inventory_management_system"
)

mycursor = mydb.cursor()

def view_products():
    print("List of available products:")
    mycursor.execute("SELECT * FROM products")
    for product in mycursor.fetchall():
        print(product)

def add_product():
    name = input("Enter product name: ")
    quantity = input("Enter product quantity: ")
    price = input("Enter product price: ")

    query = "INSERT INTO products (name, quantity, price) VALUES (%s, %s, %s)"
    values = (name, quantity, price)
    mycursor.execute(query, values)
    mydb.commit()
    print("Product added successfully.")

def update_product():
    product_id = input("Enter product ID to update: ")
    name = input("Enter new product name: ")
    quantity = input("Enter new product quantity: ")
    price = input("Enter new product price: ")

    query = "UPDATE products SET name = %s, quantity = %s, price = %s WHERE id = %s"
    values = (name, quantity, price, product_id)
    mycursor.execute(query, values)
    mydb.commit()
    print("Product updated successfully.")
def purchase_product():
    product_id = input("Enter product ID to purchase: ")
    quantity = input("Enter quantity to purchase: ")

    # Check if the product exists
    query = "SELECT * FROM products WHERE id = %s"
    mycursor.execute(query, (product_id,))
    product = mycursor.fetchone()

    if product:
        available_quantity = product[2]  # Assuming quantity is stored in the third column
        if int(quantity) <= available_quantity:
            # Calculate the new quantity after purchase
            new_quantity = available_quantity - int(quantity)

            # Update the database with the new quantity
            update_query = "UPDATE products SET quantity = %s WHERE id = %s"
            mycursor.execute(update_query, (new_quantity, product_id))
            mydb.commit()

            print(f"{quantity} {product[1]} purchased successfully.")
        else:
            print("Insufficient quantity available.")
    else:
        print("Product not found.")  

def delete_product():
    product_id = input("Enter product ID to delete: ")

    query = "DELETE FROM products WHERE id = %s"
    value = (product_id,)
    mycursor.execute(query, value)
    mydb.commit()
    print("Product deleted successfully.")

def add_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, password)
    mycursor.execute(query, values)
    mydb.commit()
    print("User added successfully.")

def update_user():
    user_id = input("Enter user ID to update: ")
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    query = "UPDATE users SET username = %s, password = %s WHERE id = %s"
    values = (username, password, user_id)
    mycursor.execute(query, values)
    mydb.commit()
    print("User updated successfully.")

def delete_user():
    user_id = input("Enter user ID to delete: ")

    query = "DELETE FROM users WHERE id = %s"
    value = (user_id,)
    mycursor.execute(query, value)
    mydb.commit()
    print("User deleted successfully.")

def user_session():
    while True:
        print("..........................")
        print("Inventory Services")
        print("..........................")
        print(".    1. View Products    .")
        print(".    2. Update Product Quantity   .")
        print(".    3. Purchase Product .")
        print(".    4. Log out           .")
        print("..........................")
        
        choice = input("Choose service: ")
        if choice == "1":
            view_products()

        elif choice == "2":
            update_product_quantity()

        elif choice == "3":
            purchase_product()

        elif choice == "4":
            print("Logging out...")
            break

        else:
            print("Invalid service")

def update_product_quantity():
    product_id = input("Enter product ID to update quantity: ")
    new_quantity = input("Enter new quantity: ")

    query = "UPDATE products SET quantity = %s WHERE id = %s"
    values = (new_quantity, product_id)
    mycursor.execute(query, values)
    mydb.commit()
    print("Product quantity updated successfully.")

def product_manager_session():
    while True:
        print("..........................")
        print("Product Manager Services")
        print("..........................")
        print(".    1. Add Product      .")
        print(".    2. Update Product   .")
        print(".    3. Delete Product   .")
        print(".    4. Add User         .")
        print(".    5. Update User      .")
        print(".    6. Delete User      .")
        print(".    7. Log out          .")
        print("..........................")
        
        choice = input("Choose service: ")
        if choice == "1":
            add_product()

        elif choice == "2":
            update_product()

        elif choice == "3":
            delete_product()

        elif choice == "4":
            add_user()

        elif choice == "5":
            update_user()

        elif choice == "6":
            delete_user()

        elif choice == "7":
            print("Logging out...")
            break

        else:
            print("Invalid service")

def main():
    while True:
        print("Welcome to the Inventory Management System!")
        print("1. User Login")
        print("2. Product Manager Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_session()

        elif choice == "2":
            product_manager_session()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
