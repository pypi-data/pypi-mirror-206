import contextlib
from abc import abstractmethod, ABC

from neurosdk.__cmn_types import *
from neurosdk.cmn_types import *
from neurosdk.sensor import Sensor


class EnvelopeSensor(Sensor, ABC):
    def __init__(self, ptr):
        super().__init__(ptr)
        if self.is_supported_feature(SensorFeature.FeatureEnvelope):
            self.envelopeDataReceived = None
            self.set_envelope_callbacks()
        self.__closed = False

    def __del__(self):
        with contextlib.suppress(Exception):
            if not self.__closed:
                self.__closed = True
                self.envelopeDataReceived = None
                self.unset_envelope_callbacks()
        super().__del__()

    @abstractmethod
    def set_envelope_callbacks(self):
        pass

    @abstractmethod
    def unset_envelope_callbacks(self):
        pass
