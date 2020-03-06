import mysql.connector


class SQLRequests:
    def __init__(self, user, password, database, host='127.0.0.1'):
        self.user = user
        self.password = password
        self.database = database
        self.host = host

        self.cursor = None
        self.conn = None

        self.connect_to_serer()

    def connect_to_serer(self):
        self.conn = mysql.connector.connect(
            user=self.user, password=self.password,
            host=self.host,
            database=self.database
        )

        self.cursor = self.conn.cursor(buffered=True)
        print('successful')

    def get(self, table, **kwargs):
        """

        :param table:   --
        :param kwargs:  'field'     - the field for the condition
                        'sign'      - the sign a condition
                        'condition'
                        'fields'    - the fields for a choose from table
        :return:        none
        """

        request = f"SELECT {kwargs['fields']} " \
                  f"FROM {table} "

        if 'field' in kwargs:
            request += f"WHERE {kwargs['field']} {kwargs['sign']} {kwargs['condition']} "

        request += ';'

        self.cursor.execute(request)

        for row in self.cursor:
            print(row)

