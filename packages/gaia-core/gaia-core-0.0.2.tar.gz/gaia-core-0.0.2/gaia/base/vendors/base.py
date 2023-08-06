# from abc import ABCMeta, abstractmethod

class BaseVendor:
    # __metaclass__ = ABCMeta
    # @abstractmethod
    def __init__(self): raise NotImplementedError
    def run_chat(self): raise NotImplementedError
    def run_completion(self): raise NotImplementedError
    def get_tokens(self): raise NotImplementedError
    def get_price(self): raise NotImplementedError
    def calculate_price(self): raise NotImplementedError