import psycopg2

import configparser


class Db:
    def __init__(self, table_name):
        self.table_name = table_name
        config = configparser.ConfigParser()
        config.read('config.ini')

        database_config = config['database']
        host = database_config['host']
        port = database_config['port']
        database = database_config['database']
        username = database_config['username']
        password = database_config['password']

        print(f"Host: {host}")
        print(f"Port: {port}")
        print(f"Database: {database}")
        print(f"Username: {username}")
        print(f"Password: {password}")

        self.conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=database
        )
        self.cursor = self.conn.cursor()
        self._create_table_if_not_exists()

    def _create_table_if_not_exists(self):
        query = f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                cnp TEXT NOT NULL,
                age INTEGER NOT NULL
            );
        """
        self.execute_query(query)

    def execute_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        self.conn.commit()

    def execute_select(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        rows = self.cursor.fetchall()
        return rows

    def add(self, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join('%s' for _ in data)
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        params = tuple(data.values())
        self.execute_query(query, params)
        return self.cursor.lastrowid

    def get_all(self):
        query = f"SELECT * FROM {self.table_name}"
        rows = self.execute_select(query)
        items = []
        for row in rows:
            item = {}
            for i, column_name in enumerate(self.cursor.description):
                item[column_name.name] = row[i]
            items.append(item)
        return items

    def get_by_id(self, id):
        query = f"SELECT * FROM {self.table_name} WHERE id = %s"
        params = (id,)
        rows = self.execute_select(query, params)
        if len(rows) > 0:
            item = {}
            for i, column_name in enumerate(self.cursor.description):
                item[column_name.name] = rows[0][i]
            return item
        else:
            return None

    def update(self, id, data):
        set_columns = ', '.join(f"{column_name} = %s" for column_name in data.keys())
        query = f"UPDATE {self.table_name} SET {set_columns} WHERE id = %s"
        params = tuple(data.values()) + (id,)
        self.execute_query(query, params)

    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = %s"
        params = (id,)
        self.execute_query(query, params)

    def add_column(self, column_name, data_type):
        query = f"ALTER TABLE {self.table_name} ADD COLUMN {column_name} {data_type}"
        self.execute_query(query)

    def delete_column(self, column_name):
        query = f"ALTER TABLE {self.table_name} DROP COLUMN {column_name}"
        self.execute_query(query)

    def print_db_structure(self, path):
        # Establish a connection to the database
        conn = self.conn
        cursor = conn.cursor()

        # Get the table names in the database
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
        table_names = cursor.fetchall()

        with open(path, "w") as f:
            # Loop through each table and print its structure to the file
            for table_name in table_names:
                cursor.execute(f"SELECT column_name, data_type FROM information_schema.columns WHERE table_name = '{table_name[0]}'")
                columns = cursor.fetchall()
                f.write(f"Table: {table_name[0]}\n")
                for column in columns:
                    f.write(f"    Column: {column[0]}, Data Type: {column[1]}\n")
                f.write("\n")

        cursor.close()
        conn.close()

