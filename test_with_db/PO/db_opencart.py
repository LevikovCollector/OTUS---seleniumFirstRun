import mysql.connector


class SQLDB:
    GET_PRODUCT_BY_NAME = "SELECT oc_pd.product_id FROM opencart.oc_product_description as oc_pd where oc_pd.name = %s;"
    INSERT_NEW_PRODUCT_DESC = "INSERT INTO opencart.oc_product_description " \
                              "(product_id, language_id, name, description, meta_title) " \
                              "VALUES (%s, %s, %s, %s, %s)"

    INSERT_NEW_PRODUCT = "INSERT INTO opencart.oc_product " \
                         "(model, price, points, date_available, minimum, status, date_added) " \
                         "VALUES (%s, %s, %s, %s, %s, %s, %s)"

    GET_PRODUCT_BY_MODEL = "SELECT op.product_id FROM opencart.oc_product as op where op.model = %s;"


class WorkDB:
    def __init__(self):
        connect_data = {
            'host': '0.0.0.0',
            'port': '3306',
            'user': 'root',
            'pas': 'qwe123'
        }
        self.connection = mysql.connector.connect(user=connect_data['user'],
                                                  password=connect_data['pas'],
                                                  host=connect_data['host'],
                                                  port=connect_data['port'])
        self.cursor = self.connection.cursor()

    def get_id_product_by_name(self, pr_name):
        self.cursor.execute(SQLDB.GET_PRODUCT_BY_NAME, [(pr_name)])
        return self.cursor.fetchall()

    def insert_new_product(self, param):
        if param == 'del':
            values_product = ('Test_model', '2000', '100', '2020-04-05', '1', '1', '2020-04-05')
        else:
            values_product = ('Test_model_edit', '2000', '100', '2020-04-05', '1', '1', '2020-04-05')

        self.cursor.execute(SQLDB.INSERT_NEW_PRODUCT, values_product)
        self.connection.commit()

        self.cursor.execute(SQLDB.GET_PRODUCT_BY_MODEL, [(values_product[0])])
        prod_id = str(self.cursor.fetchall()[0][0])

        if param == 'del':
            values_desc = (prod_id, '1', 'Product_for_delete', 'test_desc', 'test_title')
        else:
            values_desc = (prod_id, '1', 'Product_for_edit', 'test_desc', 'test_title')

        self.cursor.execute(SQLDB.INSERT_NEW_PRODUCT_DESC, values_desc)
        self.connection.commit()

    def __del__(self):
        self.connection.close()


if __name__ == '__main__':
    # Product 81
    db = WorkDB()
    db.insert_new_product('')
    test = db.get_id_product_by_name('Product_for_edit')
    print(test)
    #
