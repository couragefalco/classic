import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(recipients, subject, body):
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = 465  # Updated for SSL
    smtp_user = os.getenv('SMTP_USER')
    smtp_password = os.getenv('SMTP_PASSWORD')
    
    from_email = smtp_user

    try:
        # Updated to use SSL directly
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(smtp_user, smtp_password)
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = ", ".join(recipients)
        part2 = MIMEText(body, 'html')
        msg.attach(part2)
        server.sendmail(from_email, recipients, msg.as_string())
        server.quit()
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Failed to send test email: {e}")


if __name__ == "__main__":
    csv_file_path = 'emails.csv'  # Path to your CSV file
    recipient_email = 'falco02@gmx.de'

    # Define the subject and body of your test email
    subject = "Test Email5"
    body = """
    
    




<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="de">
<head>
<title>$subject</title>
<meta charset="UTF-8" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<!--[if !mso]><!-->
<meta http-equiv="X-UA-Compatible" content="IE=edge" />
<!--<![endif]-->
<meta name="x-apple-disable-message-reformatting" content="" />
<meta content="target-densitydpi=device-dpi" name="viewport" />
<meta content="true" name="HandheldFriendly" />
<meta content="width=device-width" name="viewport" />
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no, url=no" />
<style type="text/css">
table {
border-collapse: separate;
table-layout: fixed;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt
}
table td {
border-collapse: collapse
}
.ExternalClass {
width: 100%
}
.ExternalClass,
.ExternalClass p,
.ExternalClass span,
.ExternalClass font,
.ExternalClass td,
.ExternalClass div {
line-height: 100%
}
body, a, li, p, h1, h2, h3 {
-ms-text-size-adjust: 100%;
-webkit-text-size-adjust: 100%;
}
html {
-webkit-text-size-adjust: none !important
}
body, #innerTable {
-webkit-font-smoothing: antialiased;
-moz-osx-font-smoothing: grayscale
}
#innerTable img+div {
display: none;
display: none !important
}
img {
Margin: 0;
padding: 0;
-ms-interpolation-mode: bicubic
}
h1, h2, h3, p, a {
line-height: 1;
overflow-wrap: normal;
white-space: normal;
word-break: break-word
}
a {
text-decoration: none
}
h1, h2, h3, p {
min-width: 100%!important;
width: 100%!important;
max-width: 100%!important;
display: inline-block!important;
border: 0;
padding: 0;
margin: 0
}
a[x-apple-data-detectors] {
color: inherit !important;
text-decoration: none !important;
font-size: inherit !important;
font-family: inherit !important;
font-weight: inherit !important;
line-height: inherit !important
}
a[href^="mailto"],
a[href^="tel"],
a[href^="sms"] {
color: inherit;
text-decoration: none
}
img,p{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:25px;font-weight:400;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#121212;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px}h1{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:28px;font-weight:700;font-style:normal;font-size:22px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px}h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}
</style>
<style type="text/css">
@media (min-width: 481px) {
.hd { display: none!important }
}
</style>
<style type="text/css">
@media (max-width: 480px) {
.hm { display: none!important }
}
</style>
<style type="text/css">
[style*="Fira Sans"] {font-family: 'Fira Sans', BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif !important;}
@media only screen and (min-width: 481px) {img,p{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:28px;font-weight:400;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#121212;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px}h1{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:700;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px}h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.t16{max-width:520px!important}.t19,.t21{padding-top:60px!important;padding-bottom:60px!important}.t25{width:74px!important}.t51{line-height:28px!important;mso-text-raise:4px!important}.t58,.t60{padding-top:30px!important}.t92{line-height:34px!important;mso-text-raise:5px!important}.t102{line-height:28px!important;mso-text-raise:4px!important}}
</style>
<style type="text/css" media="screen and (min-width:481px)">.moz-text-html img,.moz-text-html p{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:28px;font-weight:400;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#121212;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px}.moz-text-html h1{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:700;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}.moz-text-html .t16{max-width:520px!important}.moz-text-html .t19,.moz-text-html .t21{padding-top:60px!important;padding-bottom:60px!important}.moz-text-html .t25{width:74px!important}.moz-text-html .t51{line-height:28px!important;mso-text-raise:4px!important}.moz-text-html .t58,.moz-text-html .t60{padding-top:30px!important}.moz-text-html .t92{line-height:34px!important;mso-text-raise:5px!important}.moz-text-html .t102{line-height:28px!important;mso-text-raise:4px!important}</style>
<!--[if !mso]><!-->
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@500&amp;display=swap" rel="stylesheet" type="text/css" />
<!--<![endif]-->
<!--[if mso]>
<style type="text/css">
img,p{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:28px;font-weight:400;font-style:normal;font-size:18px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#121212;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px}h1{margin:0;Margin:0;font-family:Fira Sans,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:34px;font-weight:700;font-style:normal;font-size:28px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#000;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px}h2{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:30px;font-weight:400;font-style:normal;font-size:24px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}h3{margin:0;Margin:0;font-family:Lato,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:26px;font-weight:400;font-style:normal;font-size:20px;text-decoration:none;text-transform:none;letter-spacing:0;direction:ltr;color:#333;text-align:left;mso-line-height-rule:exactly;mso-text-raise:2px}div.t16{max-width:520px !important}td.t19{padding-top:60px !important;padding-bottom:60px !important}td.t21{padding-top:60px !important;padding-bottom:60px !important;width:520px !important}td.t25{width:74px !important}p.t51{line-height:28px !important;mso-text-raise:4px!important}td.t58,td.t60{padding-top:30px !important}h1.t92{line-height:34px !important;mso-text-raise:5px!important}p.t102{line-height:28px !important;mso-text-raise:4px!important}
</style>
<![endif]-->
<script type="application/ld+json">[{"@context":"http://schema.org/","@type":"EmailMessage","subjectLine":"van gogh"}]</script>
<!--[if mso]>
<xml>
<o:OfficeDocumentSettings>
<o:AllowPNG/>
<o:PixelsPerInch>96</o:PixelsPerInch>
</o:OfficeDocumentSettings>
</xml>
<![endif]-->
</head>
<body class="t0" style="min-width:100%;Margin:0px;padding:0px;background-color:#F7F7F7;"><div style="display:none; font-size:1px; color:#333333; line-height:1px; max-height:0px; max-width:0px; opacity:0; overflow:hidden;">kids turned out fine #1</div><div style="font-size: 0px; line-height:0px; display: none; max-height: 0px; overflow: hidden;">&#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy; &#847; &zwnj; &nbsp; &#8199; &shy;</div><div class="t1" style="background-color:#F7F7F7;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center"><tr><td class="t2" style="font-size:0;line-height:0;mso-line-height-rule:exactly;background-color:#F7F7F7;" valign="top" align="center">
<!--[if mso]>
<v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="true" stroke="false">
<v:fill color="#F7F7F7"/>
</v:background>
<![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" align="center" id="innerTable"><tr><td><div class="t12" style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="top" width="520"><tr><td width="520" valign="top"><![endif]-->
<div class="t16" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:480px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t18"><tr>
<td class="t19" style="background-color:#FCFCFC;padding:50px 20px 50px 20px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t24" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t25" style="width:30px;">
<!--<![endif]-->
<!--[if mso]><td class="t25" style="width:30px;"><![endif]-->
<div style="font-size:0px;"><img class="t31" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="74" height="74" alt="" src="$picture_link"/></div>
</tr></table>
</td></tr><tr><td><div class="t32" style="mso-line-height-rule:exactly;mso-line-height-alt:55px;line-height:55px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t34" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t35" style="border:5px solid #EDEDED;width:368px;">
<!--<![endif]-->
<!--[if mso]><td class="t35" style="border:5px solid #EDEDED;width:378px;"><![endif]-->
<div style="font-size:0px;"><img class="t41" style="display:block;border:0;height:auto;width:100%;Margin:0;max-width:100%;" width="368" height="276" alt="" src="https://cdn.shopify.com/s/files/1/1771/4067/files/The_Starry_Night_By_Vincent_Van_Gogh_5fea445a-de35-4ebc-b749-408bf21bac34_large.jpg?v=1571687140"/></div></td>
</tr></table>
</td></tr><tr><td><div class="t83" style="mso-line-height-rule:exactly;mso-line-height-alt:60px;line-height:60px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t85" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t86" style="width:375px;">
<!--<![endif]-->
<!--[if mso]><td class="t86" style="width:375px;"><![endif]-->
<h1 class="t92" style="margin:0;Margin:0;font-family:Helvetica,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:28px;font-weight:700;font-style:normal;font-size:16px;text-decoration:none;text-transform:none;direction:ltr;color:#424242;text-align:left;mso-line-height-rule:exactly;mso-text-raise:4px;">$subject</h1>
</tr></table>
</td></tr><tr><td><div class="t93" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t95" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t96" style="width:375px;">
<!--<![endif]-->
<!--[if mso]><td class="t96" style="width:375px;"><![endif]-->
<p class="t102" style="margin:0;Margin:0;font-family:Helvetica,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:25px;font-weight:400;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;direction:ltr;color:#424242;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">$description</p>
</tr></table>
</td></tr><tr><td><div class="t42" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t44" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t45" style="width:375px;">
<!--<![endif]-->
<!--[if mso]><td class="t45" style="width:375px;"><![endif]-->
<p class="t51" style="margin:0;Margin:0;font-family:Helvetica,BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif;line-height:25px;font-weight:400;font-style:normal;font-size:14px;text-decoration:none;text-transform:none;direction:ltr;color:#424242;text-align:left;mso-line-height-rule:exactly;mso-text-raise:3px;">Kids turned out fine.</p></td>
</tr></table>
</td></tr><tr><td><div class="t52" style="mso-line-height-rule:exactly;mso-line-height-alt:20px;line-height:20px;font-size:1px;display:block;">&nbsp;</div></td></tr><tr><td>
<table class="t59" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t60" style="background-color:#FCFCFC;width:400px;padding:20px 0 0 0;">
<!--<![endif]-->
<!--[if mso]><td class="t60" style="background-color:#FCFCFC;width:400px;padding:20px 0 0 0;"><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td>
<table class="t63" role="presentation" cellpadding="0" cellspacing="0" align="center"><tr>
<!--[if !mso]><!--><td class="t64" style="background-color:#FCFCFC;">
<!--<![endif]-->
<!--[if mso]><td class="t64" style="background-color:#FCFCFC;"><![endif]-->
<div class="t70" style="display:inline-table;width:100%;text-align:center;vertical-align:top;">
<!--[if mso]>
<table role="presentation" cellpadding="0" cellspacing="0" align="center" valign="top" width="86"><tr><td class="t75" style="width:3px;" width="3"></td><td width="80" valign="top"><![endif]-->
<div class="t76" style="display:inline-table;text-align:initial;vertical-align:inherit;width:100%;max-width:86px;"><div class="t77" style="padding:0 3px 0 3px;">
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" class="t78"><tr>
<td class="t79" style="overflow:hidden;text-align:center;line-height:20px;mso-line-height-rule:exactly;mso-text-raise:2px;padding:5px 0 5px 0;border-radius:8px 8px 8px 8px;"><span class="t80" style="display:block;margin:0;Margin:0;font-family:BlinkMacSystemFont,Segoe UI,Helvetica Neue,Arial,sans-serif,'Fira Sans';line-height:20px;font-weight:500;font-style:normal;font-size:12px;text-decoration:none;direction:ltr;color:#CCCCCC;text-align:center;mso-line-height-rule:exactly;mso-text-raise:2px;">Unsubscribe</span></td>
</tr></table>
</div></div>
<!--[if mso]>
</td><td class="t75" style="width:3px;" width="3"></td>
</tr></table>
<![endif]-->
</div></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</td></tr></table></td>
</tr></table>
</div>
<!--[if mso]>
</td>
</tr></table>
<![endif]-->
</div></td></tr></table></td></tr></table></div></body>
</html>


    
    
    
"""

    send_email(recipient_email, subject, body)
