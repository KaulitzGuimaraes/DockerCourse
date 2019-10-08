import mysql.connector as mc
import  os
## Mysql implemenation class
# @author   Kaulitz.Guimaraes@ibm.com
class MySql:
    ##   Class constructor
    def __init__(self):
        try:
            self.mydb = self.connect_my_sql()
            self.mycursor = self.mydb.cursor()
            self.assembly_base_query()
        except :
            raise Exception

    ## This method returns a dictionary that contains the query structure for all the CRUD methods
    # @return dict
    def assembly_base_query(self):
        self.base_queries = {
            'create': '''
            INSERT INTO {} ({}) VALUES ({});
            ''',
            'update': '''
            UPDATE  {} SET {} WHERE {};
            ''',
            'delete': '''
            DELETE FROM  {}  WHERE {};
            ''',
            'select': '''
            SELECT {}  FROM {}  WHERE {};
            ''',
            'selectWithouWhere': '''
                    SELECT {}  FROM {};
                    ''',

        }

    ## This method connects with MySql database
    # @return void
    def connect_my_sql(self):

            mydb = mc.connect(
                host=os.getenv("HOST"),
                user=os.getenv("USER"),
                password=os.getenv("PASSWORD"),
                database="TWITTERDATASET"
            )
            return mydb


    ## This method execute the query
    # @param  query str
    # @return       object
    def call_exec(self, query):
        try:
            return self.mycursor.execute(query)
        except Exception:
            return None

    ## This method creates a register in the database
    # @param fields str
    # @param table  str
    # @param values str
    # @return       object
    def create(self, fields, table, values):
        query = self.base_queries['create'].format(table, fields, values)
        result = self.call_exec(query)
        return result

    ## This methods retrieve register(s) by the condition given, if there is no condition, it will return all results founded.
    # @param  table
    # @param  fields
    # @param  condition
    # @return object
    def retrieve(self, table, fields, condition):
        query = None
        try:
            if condition is None:
                raise BaseException
            query = self.base_queries['select'].format(fields, table, condition)
        except BaseException:
            query = self.base_queries['selectWithouWhere'].format(fields, table)
        finally:
            try:
                self.call_exec(query)
                result = self.mycursor.fetchall()
                return result
            except:
                return None

    ##  This methods update the register by the condition given
    # @param table       str
    # @param set_values  str
    # @param condition   str
    # @return            object

    def update(self, table, set_values, condition):
        query = self.base_queries['update'].format(table, set_values, condition)
        result = self.call_exec(query)
        return result

    ## This method delete a register by the condition given.
    #  @param table     str
    #  @param condition str
    #  @return          object
    def delete(self, table, condition):
        query = self.base_queries['delete'].format(table, condition)
        result = self.call_exec(query)
        return result

    ## This method persist all the changes in DB
    # @return void
    def commit(self):
        self.mydb.commit()
