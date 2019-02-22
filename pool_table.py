from datetime import datetime
file_object = open("02-22-2019.txt", "w")
file_object.close()

class PoolTable:
    def __init__(self, table_num):
        self.table_num = table_num
        self.is_available = "Not Occupied"

    def __repr__(self):
        return (f"\n Pool Table {self.table_num} - {self.is_available}")

class TableManager:
    def __init__(self):
        self.open = "Open"
        self.pool_tables = []
        self.tables()
        self.welcome()
        self.menu()

    def tables(self):
        for table_num in range(1, 13):
            pool_table = PoolTable(table_num)
            self.pool_tables.append(pool_table)

    def welcome(self):
        print("\n")
        print("Welcome to the Pool Table Manager! \n")

    def menu(self):
        while self.open == "Open":
            print("Press 1 to view tables")
            print("Press 2 to reserve a table")
            print("Press 3 to close a table ")
            print("Press 4 to quit")

            user_input = int(input("Select menu option (1, 2, 3, 4): "))
            print("\n")

            if user_input == 1:
                self.view_all()
            elif user_input == 2:
                self.reserve_table()
            elif user_input == 3:
                self.close_table()
            elif user_input == 4:
                self.quit()

    def view_all(self):
        for pool_table in self.pool_tables:
            print(f"Pool Table {pool_table.table_num} - {pool_table.is_available}")
            if pool_table.is_available == "Occupied":
                print(f"Start time: {pool_table.start_time}")
                pool_table.current_time = datetime.now()
                pool_table.play_time = pool_table.current_time - pool_table.start_time
                print(f"Play Time: {pool_table.play_time} \n")

    def reserve_table(self):
        user_input = int(input("Enter the pool table that you would like to reserve: "))
        pool_table = self.pool_tables[user_input - 1]
        if pool_table.is_available == "Occupied":
            print(f"Pool Table {pool_table.table_num} is occupied. Please choose another table. \n")
        else:
            pool_table.is_available = "Occupied"
            pool_table.start_time = datetime.now()
            print(f"Table {pool_table.table_num} is reserved. \n")

    def close_table(self):
        user_input = int(input("Enter your table number: "))
        pool_table = self.pool_tables[user_input - 1]
        pool_table.is_available = "Not Occupied"
        pool_table.end_time = datetime.now()
        pool_table.play_time = pool_table.end_time - pool_table.start_time
        print(f"Pool Table {pool_table.table_num} has been closed.")
        print(f"Time Played: {pool_table.play_time} \n")

        with open("02-22-2019.txt", "a") as file_object:
            file_object.write(f"---------------------------------------------- \n")
            file_object.write(f"Pool Table {pool_table.table_num} \n")
            file_object.write(f"Start Date & Time: {pool_table.start_time} \n")
            file_object.write(f"End Date & Time: {pool_table.end_time} \n")
            file_object.write(f"Total Time Played: {pool_table.play_time} \n")
            file_object.write(f"---------------------------------------------- \n")

    def quit(self):
        self.open = "Closed"

pool_management = TableManager()
