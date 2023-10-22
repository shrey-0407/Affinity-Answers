import streamlit as st
import json
import requests
import re

def validate_address_pin(pin, address):
    # Specify the API endpoint with the PIN code you want to query
    api_url = f"http://www.postalpincode.in/api/pincode/{pin}"

    # Make an HTTP GET request to the API
    response = requests.get(api_url)

    # Check the HTTP status code
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Use exception handling to avoid 'NoneType' error
        try:
            # Extract details from the JSON response
            response_details = [post_office['Name'] for post_office in data['PostOffice']]
            # st.write("Names from the API response:", response_details)

            # Check if any of the API names is present in the address
            for api_name in response_details:
                if api_name in address:
                    st.success(f"'Name' found in the API response: {api_name}")

                    # Here you can add additional checks for other details if needed

                    return True

            st.error("No matching 'Name' found in the address.")
            return False
        except (KeyError, TypeError, IndexError):
            st.error("Address details not found in the API response.")
            return False
    else:
        st.error(f"API request failed with status code: {response.status_code}")
        return False

st.title("Address Validation Web App")

# Input for the address
address = st.text_input("Enter an address:")

if address:
    # Extract the 6-digit number
    pin_match = re.search(r'\d{6}$', address)
    if pin_match:
        six_digit_number = pin_match.group()
        address_without_number = address.replace(six_digit_number, '').strip()
    else:
        st.warning("No 6-digit number found in the address.")

    # Split the address string by commas and remove leading/trailing spaces
    words_list = [word.strip() for word in address_without_number.split(',')]
    pin = six_digit_number

    if validate_address_pin(pin, address_without_number):
        st.success("The PIN code corresponds to the address.")
    else:
        st.error("The PIN code does not correspond to the address.")
