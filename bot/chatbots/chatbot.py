from abc import ABCMeta, abstractmethod


class ChatBot(metaclass=ABCMeta):
    @abstractmethod
    def talk(self, message: str)->str:
        pass
