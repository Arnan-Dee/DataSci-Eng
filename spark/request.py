import requests

if __name__ == "__main__":
    url = "https://publicapi.traffy.in.th/dump-csv-chadchart/bangkok_traffy.csv"

    response = requests.get(url)
    content = response.content

    with open("response.csv", "w", encoding="utf-8") as response_file:
        response_file.write(content.decode('utf-8'))

    
