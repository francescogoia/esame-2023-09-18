from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select distinct Country 
            from go_retailers gr 
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["Country"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodes(country):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select Retailer_code, Retailer_name
            from go_retailers gr 
            where gr.Country = %s
        """
        cursor.execute(query, (country,))
        result = []
        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdge(u, v, anno):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select gds1.Retailer_code as r1, gds2.Retailer_code as r2, count(distinct gds1.Product_number) as peso
            from go_daily_sales gds1, go_daily_sales gds2
            where gds1.Retailer_code = %s and gds2.Retailer_code = %s
                and year(gds1.`Date`) = year(gds2.`Date`) and year(gds1.`Date`) = %s
                and gds1.Product_number = gds2.Product_number
                """
        try:
            cursor.execute(query, (u.Retailer_code, v.Retailer_code, anno,))

        except Exception as e:
            print(e)
            cursor.close()
            conn.close()
            return []
        result = []
        for row in cursor:
            result.append((row["r1"], row["r2"], row["peso"]))
        cursor.close()
        conn.close()
        return result
