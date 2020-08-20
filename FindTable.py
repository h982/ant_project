import pandas as pd 
import requests

class Ant():
    def __init__(self):
        pass
    
    @staticmethod
    def findTable(itemCode):
        commonHtml = 'https://finance.naver.com/item/sise_day.nhn?code={0}&page={1}'

        for pageNum in range(50):
            stockPage = requests.get(commonHtml.format(itemCode,pageNum+1))
            stockTable = pd.read_html(stockPage.text)[0]
            remakeTable= stockTable.dropna().reset_index(drop = True)
            
            if pageNum == 0:
                mergeTable = remakeTable
            else:
                mergeTable = pd.concat([mergeTable, remakeTable])

        return mergeTable