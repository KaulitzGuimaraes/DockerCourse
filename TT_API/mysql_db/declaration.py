from mysql_db.implementation import MySql

##   Class to declare CRUD Database
#@author Kaulitz.Guimaraes@ibm

class DataBaseDeclaration:
    ##  Class creator
    # @param db
    def __init__(self,db=MySql):
        try:
         self.mydb = db()
        except :
            return  None
    ## This method creates a new register on the table given by the values given.
    # @param table str
    # @param fields str
    # @param value str
    # @return tuple
    def create(self,table,fields,value):

        result = self.mydb.create(fields,table,value)
        self.mydb.commit()
        return result

    ##  This method retrieves registers from table by the condition given, if there is no condition it will returns all the registers
    # @param table     str
    # @param fields    str
    # @param condition str
    # @return object
    def retrieve(self, table, fields="*", condition=None):
        try:
            result = self.mydb.retrieve(table, fields, condition)
            self.mydb.commit()
            return result
        except :
            raise  Exception
    ## This method update (a) register(s) condition given
    # @param table      str
    # @param set_values str
    # @param condition  str
    # @return           object
    def update(self,table,set_values,condition):
        result = self.mydb.update(table, set_values, condition)
        self.mydb.commit()
        return result

    ##   This method delete  (a) register(s) condition given
    # @param table     str
    # @param condition str
    # @return          object
    def delete(self,table,condition):
        result = self.mydb.retrieve(table, condition)
        self.mydb.commit()
        return result

