class BuilderTypeError(Exception):
    def __init__(self, __class_name, __arg, __type_expect, __type_received):
        super().__init__(f"TypeError: '{__class_name}' builder '{__arg}' expects {__type_expect}, but received {__type_received}.")

class BuilderVariableError(Exception):
    def __init__(self, __class_name, __arg):
        super().__init__(f"AttributeError: '{__class_name}' object has no attribute '{__arg}'.")