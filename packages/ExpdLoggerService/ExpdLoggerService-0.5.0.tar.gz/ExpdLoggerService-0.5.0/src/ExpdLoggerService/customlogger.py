import pendulum
import smtplib
import logging
import logging.handlers
from email.message import EmailMessage
from os import path, sys
from loguru import logger


class CustomSMTPHandler(logging.handlers.SMTPHandler):
    def __init__(self, appname, mailhost, fromaddr, toaddrs, subject=None, credentials=None, secure=None, timeout=5):
        super().__init__(mailhost, fromaddr, toaddrs, subject, credentials, secure, timeout)
        self.appname = appname

    def emit(self, record):
        try:
            smtp_server = smtplib.SMTP(self.mailhost, self.mailport)
            smtp_server.starttls()
            msg = EmailMessage()
            msg['From'] = self.fromaddr
            msg['To'] = ','.join(self.toaddrs)
            msg['Subject'] = f'Project - {self.appname} - Got {record.levelname} on line: {record.lineno}, file: {record.filename}'
            msg.set_content(self.format(record))
            smtp_server.send_message(msg)
        except Exception as e:
            self.handleError(record)
        finally:
            smtp_server.quit()
             

class CustomLogger:
    """
    A custom logger that logs to a file and sends error messages via email.
    Attributes:
        log_file (str): The path to the log file.
        logger (loguru.logger): The loguru logger instance.
    """
    def set_datetime(self, record):
        record["extra"]["datetime"] = pendulum.now("Asia/Shanghai").to_datetime_string()

    def __init__(self, APP_NAME, LOG_PATH, MAILHOST, MAILFROM, MAILTOCC):
        self.APP_NAME = APP_NAME
        self.LOG_PATH = LOG_PATH
        self.MAILHOST = MAILHOST
        self.MAILFROM = MAILFROM
        self.MAILTOCC = MAILTOCC
        self.logger = logger
        self.logger.remove()
        self.logger.add(sys.stderr)
        self.logger.configure(patcher=self.set_datetime)
        self.format = "<green>{extra[datetime]}</green> | <level>{level}</level> | <cyan>{name}:{function}:{line}</cyan> | {message}"
        self.instance_handler()

    def add_file_handler(self):
        fileer = path.join(self.LOG_PATH, f"{self.APP_NAME}.log")
        self.logger.add(sink=fileer, format=self.format, encoding='utf-8', retention="5 days", enqueue=True, backtrace=True, diagnose=True)

    def add_mail_handler(self):
        mailer = CustomSMTPHandler(mailhost=(self.MAILHOST, 465), fromaddr=self.MAILFROM, toaddrs=self.MAILTOCC, appname=self.APP_NAME)
        self.logger.add(sink=mailer, format=self.format, level='ERROR')

    def instance_handler(self):
        self.add_file_handler()
        self.add_mail_handler()


if __name__ == "__main__":
    from settings import Settings

    logger = CustomLogger(
        APP_NAME="XLS2XML", 
        LOG_PATH=r"/home/sha-gregh/xls2xml/server/logs", 
        MAILHOST=Settings.MAIL_SS, 
        MAILFROM=Settings.MAIL_FM, 
        MAILTOCC=Settings.MAIL_TO
    ).logger

    logger.error("A error happened during ................ ")