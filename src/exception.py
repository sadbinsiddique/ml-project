from types import ModuleType

def error_message_detail(error: BaseException, error_detail: ModuleType):
    _, _, exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename
    else:
        line_number = "unknown"
        file_name = "unknown"
    error_message = f"Error occurred in script: {file_name} at line number: {line_number} with message: {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: ModuleType):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
