from telethon import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest

api_id = 
api_hash = ''
phone_number = '+79152617655'

group_id = 263549607 
guest_phone_number=XXXXXXXXXXXX

client = TelegramClient('session_name',
                    api_id,
                    api_hash)

assert client.connect()
if not client.is_user_authorized():
client.send_code_request(phone_number)
me = client.sign_in(phone_number, input('Enter code: '))

# ---------------------------------------
# add user to contact
contact = InputPhoneContact(client_id=0, phone='+79260411314', first_name="custom_first_name", last_name="custom_last_name")
result = client.invoke(ImportContactsRequest([contact]))
# ---------------------------------------
# add contact to your group
client(AddChatUserRequest(user_id=result.users[0], fwd_limit=0, chat_id=-1001540301724))
# ---------------------------------------
# remove contact
client(DeleteContactsRequest(id=result.users[0]))