def address_in_county(zip_codes, address):
    """
    Determines if an address is in a county by parsing the 
    zip code from the address and checking to see if it is
    contained in the list of zip codes
    
    Parameters:
    zip_codes (list): Zip codes found in county.
    address (string): Address to be tested.
    
    Returns:
    (bool): True if address is in county, False if not.
    """
    # Determine if address is long enough to contain a zip code
    if len(address) < 5:
        return False

    # Determine if address contains at least 2 spaces  
    if address.count(' ') < 1:
        return False
    
    # Determine if address contains at least 1 comma
    if address.count(',') < 1:
        return False

    # Parse zip code from address
    zip_code = address.split(' ')[-1]
    
    try:
        # Determines if zip code is in list of zip codes
        return int(zip_code) in zip_codes

    # If an error is encountered the error message is stored in the err variable
    except Exception as err:
        print(err)
        return False
    
def main():
    
    # Define list of zip codes found in Beltrami County
    beltrami_zip_codes = [56601,56633,56630,56676,56725,56727,56678,56670,56667,56666,56663,56647,56650,56683,56685,56671,56687,56619]      

    # Define address to be tested
    paul_bunyan_address = '300 Bemidji Ave N, Bemidji, MN 56601'

    # Test if address is in county and print result
    print(address_in_county(
        zip_codes = beltrami_zip_codes,
        address = paul_bunyan_address))

if __name__ == '__main__':
    
    main()