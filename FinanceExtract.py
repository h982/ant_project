import pandas as pd 
import requests     
from bs4 import BeautifulSoup
from selenium import webdriver
    
class FinanceExtract():
    
    def __init__(self):
        self.common_url = 'https://navercomp.wisereport.co.kr/v2/company/c1010001.aspx?cmp_cd=' 
        self.driver = webdriver.Chrome('C:\chromedriver.exe')    
        pass
    
    def __make_url(self,stock_code):
        self.driver.get(self.common_url + stock_code)
    
    def __get_table(self):
        table = pd.read_html(self.driver.page_source)
        
        finance_table = table[12]
        finance_extract =finance_table.iloc[[0,1,4,7,8,9,19,20],:].dropna(axis=1)
        return finance_extract
    
    def show_finance_table(self,stock_code):
        self.__make_url(stock_code)
        table = self.__get_table()
        return table
