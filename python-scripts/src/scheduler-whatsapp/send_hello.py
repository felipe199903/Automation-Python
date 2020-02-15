from twilio.rest import Client 
 
account_sid = 'ACe1a6140863ad766304dfdd0d38e286b6' 
auth_token = '9898469f32fb88d5dc4ef2909894a97b' 
client = Client(account_sid, auth_token) 

def send_message():
    message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='Hello, test API',      
        to='whatsapp:+5511942371744' 
        ) 
 
    print(message.sid)