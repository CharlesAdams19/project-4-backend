import hmac 
import hashlib

def calculate_hmac(url, secret_key):  

    signature = hmac.new(secret_key.encode('utf8'), url.encode('utf8'), hashlib.sha1).hexdigest()
    print(signature)
    return signature


# calculate_hmac('/events?key=m29y-OHICHwcZPK','Noo5CoFCyOM6RWYxA58iefB4Ivs7MmK')
calculate_hmac('/events/c3-1507890?key=m29y-OHICHwcZPK','Noo5CoFCyOM6RWYxA58iefB4Ivs7MmK')
