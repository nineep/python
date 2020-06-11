import os
import email
import datetime

import tornado.httpserver
import tornado.websocket
import tornado.web
import argparse

from tornado.ioloop import IOLoop
from tornado import gen
from aiosmtpd.controller import Controller

#===============================================================================
#===============================================================================

class HealthCheckHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        self.write('Still here ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
        self.finish()

#===============================================================================
#===============================================================================

class SMTPHandler:
    @gen.coroutine
    def handle_RCPT(self, server, session, envelope, address, rcpt_options):

        # Filter valid email addresses
        if address not in ["email@domain.com"]: # Replace with email address of service
            return '550 invalid email address'

        envelope.rcpt_tos.append(address)
        return '250 OK'

    @gen.coroutine
    def handle_DATA(self, server, session, envelope):
        try:
            parsed_email = email.message_from_string(envelope.content.decode('utf8', errors='replace'))

            header_to = parsed_email['to']
            header_from = parsed_email['from']
            header_subject = parsed_email['subject']

            if header_from.endswith("domain.com"):  # Replace with domain of service
                raise RuntimeError("header_from is from domain.com")

            payload_plain = ""
            payload_html = ""
            attachments = []

            # Multipart messages
            if parsed_email.is_multipart():
                for part in parsed_email.walk():
                    ctype = part.get_content_type()
                    cdispo = str(part.get('Content-Disposition'))

                    # skip any text/plain (txt) attachments
                    if 'attachment' in cdispo:
                        filename = part.get_filename()
                        attachments.append(filename)
                    elif 'text/plain' in ctype:
                        payload_string = part.get_payload(decode=True).decode('utf8', errors='replace')
                        payload_plain += payload_string
                    elif 'text/html' in ctype:
                        payload_string = part.get_payload(decode=True).decode('utf8', errors='replace')
                        payload_html += payload_string

            # Not multipart - i.e. plain text, no attachments, keeping fingers crossed
            else:
                ctype = parsed_email.get_content_type()

                if ctype == 'text/plain':
                    payload_string = parsed_email.get_payload(decode=True).decode('utf8', errors='replace')
                    payload_plain += payload_string
                elif ctype == 'text/html':
                    payload_string = parsed_email.get_payload(decode=True).decode('utf8', errors='replace')
                    payload_html += payload_string

            # Do further processing

        except Exception as e:
            pass

        return '250 Message accepted for delivery'

#===============================================================================
# Build Tornado web server
#===============================================================================

APP_SETTINGS = {
    "cookie_secret": "SomeCookieSecretString",
    "login_url": "/index.html"
}

application = tornado.web.Application(
    [
        # Health Checks
        (r'/healthcheck', HealthCheckHandler),
    ],
    debug=(os.environ.get('DEBUG_MODE') == 'devel'),
    **APP_SETTINGS
)

#===============================================================================
#===============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', help='Server Port')
    parser.add_argument('--smtpport', help='SMTP Port')
    args = parser.parse_args()

    # Begin SMTP server
    smtp_server = Controller(SMTPHandler(), hostname='0.0.0.0', port=int(args.smtpport))
    smtp_server.start()

    # Begin Web server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(int(args.port))

    IOLoop.instance().start()

#===============================================================================
#===============================================================================