import mariadb
import dbcreds
def run_statement(sql, args=None):
    try:
        result = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchall()
    except mariadb.OperationalError as error:
        print('Operational Error', error)
    except mariadb.ProgrammingError as error:
        print('SQL Error', error)
    except mariadb.IntegrityError as error:
        print('DB Integrity Error', error)
    except mariadb.DataError as error:
        print('Data Error', error)
    except mariadb.DatabaseError as error:
        print('DB Error', error)
    except mariadb.InterfaceError as error:
        print('Interface Error', error)
    except mariadb.Warning as error:
        print('Warning', error)
    except mariadb.PoolError as error:
        print('Pool Error', error)
    except mariadb.InternalError as error:
        print('Internal Error', error)
    except mariadb.NotSupportedError as error:
        print('Not Supporter By DB Error', error)
    except Exception as error:
        print('Unknown Error', error)
    finally:
        if(cursor != None):
            cursor.close()
        if(conn != None):
            conn.close()
        return result
