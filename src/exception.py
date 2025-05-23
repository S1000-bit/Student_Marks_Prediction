import sys

def error_message_details(error, error_detail: sys):
    try:
        _, _, exc_tb = error_detail.exc_info()
        filename = exc_tb.tb_frame.f_code.co_filename
        error_msg = f"Error occurred in python script name [{filename}] line number [{exc_tb.tb_lineno}] error message[{str(error)}]"
        return error_msg
    except Exception as internal_error:
        return f"Failed to construct error message: {internal_error}"

class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        super().__init__(str(error))
        self.error_message = error_message_details(error, error_detail)

    def __str__(self):
        return self.error_message
