import requests.

API_ENDPOINT = 'https://api.shoppingapp.com/'

def send_api_request(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(API_ENDPOINT, headers=headers)
    return response.json()

def main():
    access_token = 'your_access_token'  # Replace with your actual access token

    response = send_api_request(access_token)
    print('API Response:', response)

if __name__ == '__main__':
    main()
