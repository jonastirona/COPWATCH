"""
Notifier module for COPWATCH
Handles notifications and alerts
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json


class NotificationService:
    def __init__(self):
        self.email_config = {
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587,
            'username': '',
            'password': ''
        }
        self.notification_log = []
    
    def send_email(self, to_email, subject, message):
        """Send email notification"""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_config['username']
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(message, 'plain'))
            
            server = smtplib.SMTP(self.email_config['smtp_server'], self.email_config['smtp_port'])
            server.starttls()
            server.login(self.email_config['username'], self.email_config['password'])
            text = msg.as_string()
            server.sendmail(self.email_config['username'], to_email, text)
            server.quit()
            
            self.log_notification('email', to_email, subject, 'sent')
            return True
            
        except Exception as e:
            self.log_notification('email', to_email, subject, f'failed: {str(e)}')
            return False
    
    def send_alert(self, alert_type, message, recipients=None):
        """Send alert notification"""
        timestamp = datetime.now().isoformat()
        alert_data = {
            'type': alert_type,
            'message': message,
            'timestamp': timestamp,
            'recipients': recipients or []
        }
        
        self.log_notification('alert', recipients, alert_type, 'triggered')
        return alert_data
    
    def log_notification(self, notification_type, recipient, subject, status):
        """Log notification activity"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'type': notification_type,
            'recipient': recipient,
            'subject': subject,
            'status': status
        }
        self.notification_log.append(log_entry)
        print(f"Notification logged: {json.dumps(log_entry, indent=2)}")


# Global notifier instance
notifier = NotificationService() 