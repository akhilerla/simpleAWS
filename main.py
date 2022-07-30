import requests
import json
import boto3
from datetime import datetime
import time
import myaws

URL = 'https://www.reebok.com/api/search/product/GY9646?sitePath=us'

request_headers = {
        'authority':'www.reebok.com',
        'method': 'GET',
        'path': '/api/search/product/GY9646?sitePath=us',
        'scheme': 'https',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "macOS",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }


def main():
    attempt = 0
    while True:
        response = requests.get(URL, headers = request_headers)
        new_response = json.loads(response.content.decode('utf-8'))
        print(new_response)
        salePrice =  60
        Price = new_response['price']
        if salePrice == Price:
            print('Time=' + str(datetime.now()) + "- Attempt=" + str(attempt))
            attempt += 1
            time.sleep(5000)
        else:
            print('Hey there is a Sale! SalePrice=' + str(salePrice))
            send_message(salePrice)
            break


def send_message(salePrice):
    arn = 'arn:aws:sns:us-east-1:972956400174:reeboksale'
    sns_client = boto3.client(
        'sns',
        aws_access_key_id =  '*******',
        aws_secret_access_key= '*******',
        region_name='us-east-1'
    )

    response = sns_client.publish(TopicArn=arn , Message='Product is on sale ' + str(salePrice))
    print(response)


main()