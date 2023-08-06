import abc


class ECPublicKey(abc.ABC):
    @abc.abstractmethod
    def serialize(self) -> bytes:
        pass

    @abc.abstractmethod
    def get_type(self) -> int:
        pass


class ECPrivateKey(abc.ABC):
    @abc.abstractmethod
    def serialize(self) -> bytes:
        pass

    @abc.abstractmethod
    def get_type(self) -> int:
        pass
