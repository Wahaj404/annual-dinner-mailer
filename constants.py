SHEET_ID = ""
SHEET_NAME = "Form Responses"
SHEET_URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

SENDER_MAIL = ""
SENDER_PASS = ""

SUBJECT = "DECS Annual Dinner 2023 E-Ticket"
BODY = """<p>Dear {name},</p>

<p>Thank you for purchasing your ticket!</p>

<p>You may collect your physical ticket by showing this E-Ticket to our team in the Cafeteria.</p>

<p>If you are a Masters student or an Alumnus, you may collect your ticket from the venue on the Event Day.</p>

<p>Cheers,<br>
DECS</p>
"""

IMAGE_TITLE = "Annual Dinner E-Ticket"
IMAGE_PATH = "eticket.png"
with open(IMAGE_PATH, "rb") as f:
    E_TICKET = f.read()

SENT_FILE = "sent.pickle"
