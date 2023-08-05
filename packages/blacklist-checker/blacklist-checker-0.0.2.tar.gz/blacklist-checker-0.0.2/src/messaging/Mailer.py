import os
import configparser
import json
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MyMailer():
    def load_smtp_config(self,config_smtp):

        if "smtp_host" not in config_smtp.keys():
            raise Exception("The SMTP host is missing")
        else:
            self.smtp_host=config_smtp["smtp_host"]

        if "smtp_port" not in config_smtp.keys():
            raise Exception("The SMTP port is missing")
        else:
            self.smtp_port=config_smtp["smtp_port"]

        if "smtp_user" not in config_smtp.keys():
            raise Exception("The SMTP user is missing")
        else:
            self.smtp_user=config_smtp["smtp_user"]

        if "smtp_pass" not in config_smtp.keys():
            raise Exception("The SMTP pass is missing")
        else:
            self.smtp_pass=config_smtp["smtp_pass"]

        if "smtp_sender" not in config_smtp.keys():
            raise Exception("The SMTP sender is missing")
        else:
            self.smtp_sender = config_smtp["smtp_sender"]

        if "smtp_daily_report_receivers" not in config_smtp.keys():
            raise Exception("At least one receiver for daily report needs to be provided")
        else:
            self.smtp_daily_report_receivers=config_smtp["smtp_daily_report_receivers"]

        if "smtp_alert_report_receivers" not in config_smtp.keys():
            raise Exception("At least one receiver for daily reports need to be be provided")
        else:
            self.smtp_alert_report_receivers=config_smtp["smtp_alert_report_receivers"]

        if "smtp_alert_report_subject" not in config_smtp.keys():
            self.smtp_alert_report_subject="Alert blacklisting domain "+self.domain
        else:
            self.smtp_alert_report_subject = config_smtp["smtp_alert_report_subject"]

        if "smtp_daily_report_subject" not in config_smtp.keys():
            self.smtp_daily_report_subject="Daily report for domain "+self.domain
        else:
            self.smtp_daily_report_subject = config_smtp["smtp_daily_report_subject"]

        if "smtp_template_directory" not in config_smtp.keys():
            raise Exception("Provide a directory for the e-mail body template")
        else:
            self.smtp_template_directory = config_smtp["smtp_template_directory"]

        if "smtp_template_language" not in config_smtp.keys():
            self.smtp_template_language="fr"
        else:
            self.smtp_template_language = config_smtp["smtp_template_language"].lower()


    def __init__(self,config_file:str,domain:str,provider):
        self.domain=domain
        if not os.path.exists(config_file):
            raise Exception(f"The config file {config_file} does not exist")
        config = configparser.ConfigParser()
        config.read(config_file)
        if domain not in config.keys():
            raise Exception(f"The config file does not contains a smtp configuration for {domain}")
        self.provider_name=config[provider]["provider_name"]
        self.load_smtp_config(config[domain])

    def set_complete_template_path(self,type="report"):
        if str(type) != "daily"  and str(type) != "alert":
            raise Exception("The type of report need to be 'daily' or 'alert' ")
        if os.path.exists(self.smtp_template_directory+os.sep+self.domain):
            path=self.smtp_template_directory+os.sep+self.domain+os.sep+type+os.sep+self.smtp_template_language+"_"+type+"_report.html"
        else:
            path=os.getcwd()+os.sep+"resources"+os.sep+"templates"+os.sep+"default"+os.sep+type+os.sep+self.smtp_template_language+"_"+type+"_report.html"
        if not os.path.exists(path):
            raise Exception(f"The template {path} does not exist")
        return path

    def load_daily_report_template(self):
        lines=""
        template_to_load=self.set_complete_template_path("daily")
        if not os.path.exists(template_to_load):
            raise Exception(f"The template {template_to_load} does not exists on disk")
        with open(template_to_load) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    lines=lines+line
        return lines

    def transform_json_to_html_table(self,reporting):
        reporting_json=str(reporting).replace("'","\"")
        reporting_json=reporting_json.replace("True","true")
        reporting_json=reporting_json.replace("False","false")

        reporting_json_object=json.loads(reporting_json)
        html_output="<table border=\"solod;1px\"><tr><td>id</td><td>name</td><td>detected</td></tr>\n"
        for item in reporting_json_object:
            line=f"<tr><td>{item['id']}</td><td>{item['name']}</td><td>{item['detected']}</td></tr>\n"
            html_output+=line

        html_output+="</table>\n"
        return html_output
        


    def load_alert_report_template(self):
        lines=""
        template_to_load=self.set_complete_template_path("alert")
        if not os.path.exists(template_to_load):
            raise Exception(f"The template {template_to_load} does not exists on disk")
        with open(template_to_load) as f:
            while True:
                line = f.readline()
                if not line:
                    break
                else:
                    lines=lines+line
        return lines

    def send_regular_report(self):
        self.set_complete_template_path("daily")
        html_mail_body_template=self.load_daily_report_template()
        html_mail_body= self.replace_template_placeholder(html_mail_body_template,None)
        self.send_mail(self.smtp_daily_report_receivers,self.smtp_daily_report_subject,html_mail_body)

    def replace_template_placeholder(self,html_body_template,report_html_table):
        html_body_template= html_body_template.replace("%DOMAIN%",self.domain)
        html_body_template=html_body_template.replace("%PROVIDERS%",self.provider_name)
        if report_html_table is not None:
            html_body_template=html_body_template.replace("%BLACKLISTS%",report_html_table)

        return html_body_template

    def send_mail(self,receiver_email,subject,html_mail_body):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.smtp_sender
        message["To"] = receiver_email
        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(html_mail_body, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
            server.login(self.smtp_user, self.smtp_pass)
            server.sendmail(
                self.smtp_sender, receiver_email, message.as_string()
            )


    def send_alert_report(self,report):
        self.set_complete_template_path("alert")
        html_mail_body_template=self.load_alert_report_template()
        report_html_table=self.transform_json_to_html_table(report)
        html_mail_body= self.replace_template_placeholder(html_mail_body_template,report_html_table)
        self.send_mail(self.smtp_alert_report_receivers,self.smtp_alert_report_subject,html_mail_body)
