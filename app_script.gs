function autoResponder(e) {
  let email = e.values[4];
  let subject = "DECS Annual Dinner 2023 Online Ticket Purchase";
  let body = `
<p>Thank you for purchasing your ticket for DECS Annual Dinner 2023.</p>

<p>This is to inform you that your payment is currently in the process of being verified by our team. As soon as the verification is done, you will receive a confirmation email containing an E-Ticket.</p>

<p>When you come to collect your physical ticket, you must show your E-Ticket to our team so that we can confirm your attendance at the event.</p>

<p>All BS Students, please make sure to collect you physical ticket before the event date. You will not be allowed to enter the venue without your physical ticket.</p>

<p>All Masters Students and FAST Alumni, please note that it is preferred that you collect your ticket before the event. However, if that is not possible for you, you may collect it on the day of the event, for which you must show your E-Ticket to our team present there.</p>

<p>Looking forward to seeing you there!</p>

<p>Best Regards,</p>
<p>DECS</p>
`;
  MailApp.sendEmail(email, subject, "", { htmlBody: body, name: "DECS" });
}
