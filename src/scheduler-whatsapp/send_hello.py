from twilio.rest import Client 
 
account_sid = 'INSERT YOUR account_sid HERE' 
auth_token = 'INSERT YOUR TOKEN HERE' 
client = Client(account_sid, auth_token) 

def send_message():
    message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='Hello, test API',      
        to='whatsapp:+551111111111' 
        ) 
 
    print(message.sid)