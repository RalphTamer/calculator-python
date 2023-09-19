import requests
from py_expression_eval import Parser

def post(url,json):
    x = requests.post(url,json=json)
    return x.json()

def get(url):
    x = requests.get(base_url)
    return x.json()

parser = Parser()
base_url = "http://127.0.0.1:5000"
while True:
    inp = input(""" 
type 1 to calculate,
type 2 to clear recents,
type 3 to see recent equations
type quit to quit
""")
    if inp == "1":
        try:
            equation = input("enter equation: ")
        
            value = parser.parse(equation).evaluate({})

            print(f"""{equation} = {value}""")
            x =  post(base_url,json={
                "user_input":equation,
                "output_value":float(value)
            })
        except:
            print("unexpected equation")
    

    elif inp == "2":
        requests.delete(f'{base_url}/clear')
    elif inp == "3":
        x = requests.get(base_url)
        for item in x.json():
            print(f"""id : {item["id"]} || input : { item['user_input'] } || output : {item["output_value"]} """)
    elif inp == "quit":
        break
    else:
        print("wrong input")

    



