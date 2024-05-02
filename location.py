import requests

# Function to get location based on IP address
def get_location():
    try:
        # Send a request to the ipinfo.io API to get location information
        response = requests.get('https://ipinfo.io')
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract location data
            ip = data['ip']
            city = data['city']
            region = data['region']
            country = data['country']
            
            # Display the location information
            print(f'IP Address: {ip}')
            print(f'City: {city}')
            print(f'Region: {region}')
            print(f'Country: {country}')
        else:
            print('Failed to fetch location information.')
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    print("Fetching login location...")
    get_location()

