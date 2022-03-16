from flask import current_app

def log_info(text):
    current_app.logger.info(text)