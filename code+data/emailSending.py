import os
import base64
import google.auth
import google.auth.transport.requests
import google_auth_oauthlib.flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SendEmail():

    def __init__(self):
        super().__init__()
        # 授權json檔
        self.CLIENT_SECRET_FILE = 'file/client_secret_835168134276-2viq1efineujui4o8puhm57m223kjlm0.apps.googleusercontent.com.json' 
        # 權限範圍(發送gmail功能)
        self.SCOPES = ['https://www.googleapis.com/auth/gmail.send']
        # 郵件內容
        self.sender = 'BOSS'
        self.to = 'e94106119@gs.ncku.edu.tw'
        self.subject = '來自BOSS的約談信'
        self.body = ''


    def get_credentials(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(google.auth.transport.requests.Request())
            else:
                flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRET_FILE, self.SCOPES)
                creds = flow.run_local_server(port = 0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    # 建立郵件內容
    def create_email(self, sender, to, subject, message_text):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = f"{sender} <tingouo20@gmail.com>"
        message['subject'] = subject
        msg = MIMEText(message_text)
        message.attach(msg)
        raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
        return {'raw': raw}

    def send_email(self, service, user_id, message):
        try:
            message = service.users().messages().send(userId=user_id, body=message).execute()
            print('Message Id: %s' % message['id'])
            return message
        except Exception as error:
            print(f'An error occurred: {error}')
            return None

    def main(self):
        creds = self.get_credentials()
        service = build('gmail', 'v1', credentials=creds)
        email_message = self.create_email(self.sender, self.to, self.subject, self.body)
        self.send_email(service, 'me', email_message)

if __name__ == '__main__':
    email_sender = SendEmail()
    email_sender.main()
