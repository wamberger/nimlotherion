

__all__ = ['Email']


import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class Email:

    def __init__(self, server, port, user, password, start_tls):
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.start_tls = start_tls

    def send_email(
            self,
            sender_email: str,
            receiver_email: list,
            subject: str,
            body: str,
            content_type: str = 'plain',
            attachments: dict = {},
            cc_email: list = [],
            bcc_email: list = [],
            reply_to: list = []) -> None:
        
        message = MIMEMultipart()

        message["From"] = sender_email
        message["To"] = ', '.join(receiver_email)
        message["Subject"] = subject

        if cc_email:
            message["Cc"] = ', '.join(cc_email)
        if bcc_email:
            message["Bcc"] = ', '.join(bcc_email)
        if reply_to:
            message["reply-to"] = ', '.join(reply_to)
        
        message.attach(MIMEText(body, content_type))

        for attachment_filename, attachment_content in attachments.items():
            attach = MIMEBase("application", "octet-stream")
            attach.set_payload(attachment_content)
            # Encode file in ASCII characters to send by email
            encoders.encode_base64(attach)
            # Add header as key/value pair to attachment
            attach.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment_filename}",
            )
            # Add attachment to message
            message.attach(attach)

        # Connect to the SMTP server
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.ehlo()
            # Start the TLS connection (secure connection)
            if self.smtp_start_TLS:
                server.starttls()
            # Login to the email account
            server.login(self.smtp_user, self.smtp_password)
            
            server.sendmail(
                sender_email, 
                receiver_email + cc_email + bcc_email,
                message.as_string()
                )
            server.quit()
