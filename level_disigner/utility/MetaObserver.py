from abc import ABCMeta, abstractmethod


class MetaObserver( metaclass = ABCMeta ):

    @abstractmethod
    def change( self ):
        pass