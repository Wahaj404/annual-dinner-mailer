import pickle
import pandas as pd
from redmail import gmail


import constants as c
from student import Student


gmail.username = c.SENDER_MAIL
gmail.password = c.SENDER_PASS


def send_email(student: Student):
    gmail.send(
        receivers=[student.nu_id],
        subject=c.SUBJECT,
        html=c.BODY.format(name=student.name) + '<img src="{{ my_image.src }}">',
        body_images={"my_image": c.IMAGE_PATH},
    )


def read_sent():
    with open(c.SENT_FILE, "rb") as f:
        return pickle.load(f)


def write_sent(sent):
    with open(c.SENT_FILE, "wb") as f:
        pickle.dump(sent, f)


if __name__ == "__main__":
    sent = read_sent()
    students = [Student(row) for row in pd.read_csv(c.SHEET_URL).values]
    for student in students:
        if student.verified and student.nu_id not in sent:
            try:
                send_email(student)
                print(student.name)
                sent.add(student.nu_id)
            except Exception as e:
                print(e)
    write_sent(sent)
