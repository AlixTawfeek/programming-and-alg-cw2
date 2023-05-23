from flask import Flask, request

app = Flask(__name__)

# Endpoint to receive the callback from the authorization URL
@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')
    # Print or process the authorization code as needed
    print('Received authorization code:', authorization_code)
    return 'Authorization code received successfully.'

if __name__ == '__main__':
    app.run(debug=True)
