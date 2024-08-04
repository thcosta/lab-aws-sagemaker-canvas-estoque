import csv
import random
from datetime import datetime, timedelta

class StockGenerator:
    MAX_ITENS_STOCK = 100
    MIN_PRICE = 10
    MAX_PRICE = 100
    MIN_ITENS_BUYED = 1
    MAX_ITENS_BUYED = 10
    PRICE_VARIATION = 0.15
    COLUMNS = ['PRODUCT_ID', 'DATE', 'PRICE', 'QUANTITY']
    
    def __init__(self):
        self.filename = self.__get_filename()
        self.dates = self.__generate_date_list()
        self.stock = self.__generate_stock_dic()
        self.prices = self.__generate_price_dic()

    @property
    def filename(self):
      return self._filename
    
    @filename.setter
    def filename(self, filename):
      self._filename = filename

    def __get_filename(self):
      filename = input('Enter filename: ')
      return f'{filename}.csv'

    # generate dictionary of all dates in a period
    def __generate_date_list(self):
      start_date = self.__get_date('Enter start date: ')
      end_date = self.__get_date('Enter end date: ')
      date_list = []
      current_date = start_date
      while current_date <= end_date:
          date_list.append(current_date)
          current_date += timedelta(days=1)
      return date_list

    def __get_date(self, message):
      while(True):
        try:
          return datetime.strptime(input(message), '%d/%m/%Y')
        except ValueError:
          print('Date invalid! Try again...')
    
    # generate dictionary of all products and their quantity in stock
    def __generate_stock_dic(self):
      start_id = self.__get_product_id('Enter first product ID: ')
      end_id = self.__get_product_id('Enter last product ID: ', start_id)
      return { i: self.MAX_ITENS_STOCK for i in range(start_id, end_id + 1) }
    
    def __get_product_id(self, message, greater_than=0):
      while(True):
        try:
          id = int(input(message))
          if id < greater_than:
            raise ValueError
          return id
        except ValueError:
          print('Product ID is invalid! Try again...')

    # generate product price of all products in stock
    def __generate_price_dic(self):
      return { i: round(random.uniform(self.MIN_PRICE, self.MAX_PRICE), 2) for i in self.stock.keys() }
    
    def generate(self):
      with open(self.filename, mode='w', newline='') as file:
          writer = csv.writer(file)
          writer.writerow(self.COLUMNS)
    
          for date in self.dates:
              for product_id in self.stock:
                  price = self.__adjust_price(self.prices[product_id]) if bool(random.getrandbits(1)) else self.prices[product_id]
                  quantity = self.stock[product_id]
                  writer.writerow([product_id, date.strftime('%Y-%m-%d'), price, quantity])
                  self.__adjust_stock(product_id)

    # Random price adjust up to 15%
    def __adjust_price(self, base_price):
      return round(base_price * (1 + random.uniform(self.PRICE_VARIATION*-1, self.PRICE_VARIATION)), 2)
    
    def __adjust_stock(self, product_id):
      self.stock[product_id] -= random.randint(self.MIN_ITENS_BUYED, self.MAX_ITENS_BUYED)
      if self.stock[product_id] <= 0:
          self.stock[product_id] = self.MAX_ITENS_STOCK


generator = StockGenerator()
generator.generate()