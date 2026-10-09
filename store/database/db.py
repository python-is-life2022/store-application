import mysql.connector as msqc

class ConnectDataBase ():
    def connect_to_store_database (self):
        self.cnx = msqc.Connect(user= 'root',
                           password= 'amir137900',
                           host= 'localhost')
        self.query = self.cnx.cursor()
        self.query.execute("CREATE DATABASE IF NOT EXISTS store_app_db;")
        self.query.execute("USE store_app_db;")
        print('Connected Succesfully!')

class UsersTable (ConnectDataBase):
    def create_users_table (self):
        self.query.execute("""
                           CREATE TABLE 
                           IF NOT EXISTS 
                           users(
                           user_id INT PRIMARY KEY AUTO_INCREMENT, 
                           first_name VARCHAR(45) NOT NULL,
                           last_name VARCHAR(45) NOT NULL,
                           age TINYINT NOT NULL,
                           birth_date DATE NOT NULL,
                           email VARCHAR(100) UNIQUE NOT NULL, 
                           national_id CHAR(10) UNIQUE NOT NULL,
                           phone_number CHAR(11) UNIQUE NOT NULL,
                           address VARCHAR(500) NOT NULL,
                           username VARCHAR(30) UNIQUE NOT NULL,
                           password VARCHAR(30) NOT NULL)
                           CHARACTER SET utf8mb4
                           COLLATE utf8mb4_unicode_ci;
                           """)
        self.cnx.commit()
        print('Table Created!')    

    def insert_into_users_table (self, f_name, l_name, age, b_date, email, n_id, tel, address, user_name, password):
        self.query.execute("""
                           INSERT INTO 
                           users (
                                first_name,
                                last_name,
                                age,
                                birth_date,
                                email,
                                national_id,
                                phone_number,
                                address,
                                username,
                                password)
                            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
                           """, (f_name, l_name, age, b_date, email, n_id, tel, address, user_name, password))
        self.cnx.commit()