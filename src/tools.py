import requests
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

load_dotenv()



#SEARCH TOOL-
search_tool = DuckDuckGoSearchRun()


#CALCULATOR TOOL-
@tool
def calculator(first_num: float, second_num: float, operation:str) ->dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations addition, substraction, multiplication, division
    """
    try:
        if operation == "add":
            result = first_num + second_num
        
        elif operation == "sub":
            result = first_num - second_num

        elif operation == "mul":
            result = first_num * second_num

        elif operation == "div":
            if second_num == 0:
                return {'error': 'Division by zero is not allowed'}
            
            else:
                result = first_num / second_num

        return {'first_num': first_num, 'second_num': second_num, 'operation': operation, 'result': result}
    
    except Exception as e:
        return {'error': str(e)}



#STOCT PRICE TOOL-
@tool
def get_stock_price(symbol: str) ->dict:
    """
    Fetch latest stock price for the given symbol. e.g - ['APPL', 'TSLA']
    using Alpha Vantage with API key in the URL.

    """

    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey=5T545HTRPD002OTK'

    response = requests.get(url)

    return response.json()














