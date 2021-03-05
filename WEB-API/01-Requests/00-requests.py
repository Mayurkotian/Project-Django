import requests

def main():
    payload = {'base':'USD', 'symbols': 'SEK'}
    response = requests.get("https://api.exchangeratesapi.io/latest", params = payload)
    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("There was a majour error! ")
    data = response.json()
    print("JSON data", data)
    print(response.text)

if __name__ == "__main__":
    main()