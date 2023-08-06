# Repository: https://gitlab.com/quantify-os/quantify-scheduler
# Licensed according to the LICENCE file on the main branch
from typing import Any, Dict

from qcodes.instrument import InstrumentChannel
from qcodes.instrument.base import InstrumentBase
from qcodes.instrument.parameter import (
    ManualParameter,
    Parameter,
)
from qcodes.utils import validators
from quantify_scheduler.backends.graph_compilation import (
    DeviceCompilationConfig,
    OperationCompilationConfig,
)
from quantify_scheduler.helpers.validators import Numbers
from quantify_scheduler.device_under_test.device_element import DeviceElement
from quantify_scheduler.operations import (
    pulse_factories,
    pulse_library,
    measurement_factories,
)


class Ports(InstrumentChannel):
    """
    Submodule containing the ports.
    """

    def __init__(self, parent: InstrumentBase, name: str, **kwargs: Any) -> None:
        super().__init__(parent=parent, name=name)

        self.microwave = Parameter(
            name="microwave",
            instrument=self,
            initial_cache_value=kwargs.get("microwave", f"{parent.name}:mw"),
            set_cmd=False,
        )
        """Name of the element's microwave port."""

        self.flux = Parameter(
            name="flux",
            instrument=self,
            initial_cache_value=kwargs.get("flux", f"{parent.name}:fl"),
            set_cmd=False,
        )
        """Name of the element's flux port."""

        self.readout = Parameter(
            name="readout",
            instrument=self,
            initial_cache_value=kwargs.get("readout", f"{parent.name}:res"),
            set_cmd=False,
        )
        """Name of the element's readout port."""


class ClocksFrequencies(InstrumentChannel):
    """
    Submodule containing the clock frequencies specifying the transitions to address.
    """

    def __init__(self, parent: InstrumentBase, name: str, **kwargs: Any) -> None:
        super().__init__(parent=parent, name=name)

        self.f01 = ManualParameter(
            name="f01",
            instrument=self,
            label="Qubit frequency",
            unit="Hz",
            initial_value=kwargs.get("f01", float("nan")),
            vals=Numbers(min_value=0, max_value=1e12, allow_nan=True),
        )
        """Frequency of the 01 clock"""

        self.f12 = ManualParameter(
            name="f12",
            instrument=self,
            label="Frequency of the |1>-|2> transition",
            unit="Hz",
            initial_value=kwargs.get("f12", float("nan")),
            vals=Numbers(min_value=0, max_value=1e12, allow_nan=True),
        )
        """Frequency of the 12 clock"""

        self.readout = ManualParameter(
            name="readout",
            instrument=self,
            label="Readout frequency",
            unit="Hz",
            initial_value=kwargs.get("readout", float("nan")),
            vals=Numbers(min_value=0, max_value=1e12, allow_nan=True),
        )
        """Frequency of the ro clock. """


class IdlingReset(InstrumentChannel):
    """
    Submodule containing parameters for doing a reset by idling.
    """

    def __init__(self, parent: InstrumentBase, name: str, **kwargs: Any) -> None:
        super().__init__(parent=parent, name=name)

        self.duration = ManualParameter(
            name="duration",
            instrument=self,
            initial_value=kwargs.get("duration", 200e-6),
            unit="s",
            vals=validators.Numbers(min_value=0, max_value=1),
        )
        """Duration of the passive qubit reset (initialization by relaxation)."""


class RxyDRAG(InstrumentChannel):
    """
    Submodule containing parameters for performing an Rxy operation
    using a DRAG pulse.
    """

    def __init__(self, parent: InstrumentBase, name: str, **kwargs: Any) -> None:
        super().__init__(parent=parent, name=name)
        self.amp180 = ManualParameter(
            name="amp180",
            instrument=self,
            label=r"$\pi-pulse amplitude$",
            initial_value=kwargs.get("amp180", float("nan")),
            unit="V",
            vals=Numbers(min_value=-10, max_value=10, allow_nan=True),
        )
        r"""Amplitude required to perform a $\pi$ pulse."""

        self.motzoi = ManualParameter(
            name="motzoi",
            instrument=self,
            initial_value=kwargs.get("motzoi", 0),
            unit="",
            vals=validators.Numbers(min_value=-1, max_value=1),
        )
        """Ratio between the Gaussian Derivative (D) and Gaussian (G)
        components of the DRAG pulse."""

        self.duration = ManualParameter(
            name="duration",
            instrument=self,
            initial_value=kwargs.get("duration", 20e-9),
            unit="s",
            vals=validators.Numbers(min_value=0, max_value=1),
        )
        """Duration of the control pulse."""


class DispersiveMeasurement(InstrumentChannel):
    """
    Submodule containing parameters to perform a measurement using
    :func:`~quantify_scheduler.operations.measurement_factories.dispersive_measurement`
    """

    def __init__(self, parent: InstrumentBase, name: str, **kwargs: Any) -> None:
        super().__init__(parent=parent, name=name)

        pulse_types = validators.Enum("SquarePulse")
        self.pulse_type = ManualParameter(
            name="pulse_type",
            instrument=self,
            initial_value=kwargs.get("pulse_type", "SquarePulse"),
            vals=pulse_types,
        )
        """Envelope function that defines the shape of the readout pulse prior to
        modulation."""

        self.pulse_amp = ManualParameter(
            name="pulse_amp",
            instrument=self,
            initial_value=kwargs.get("pulse_amp", 0.25),
            unit="V",
            vals=validators.Numbers(min_value=0, max_value=2),
        )
        """Amplitude of the readout pulse."""

        self.pulse_duration = ManualParameter(
            name="pulse_duration",
            instrument=self,
            initial_value=kwargs.get("pulse_duration", 300e-9),
            unit="s",
            vals=validators.Numbers(min_value=0, max_value=1),
        )
        """Duration of the readout pulse."""

        self.acq_channel = ManualParameter(
            name="acq_channel",
            instrument=self,
            initial_value=kwargs.get("acq_channel", 0),
            unit="#",
            vals=validators.Ints(min_value=0),
        )
        """Acquisition channel of to this device element."""

        self.acq_delay = ManualParameter(
            name="acq_delay",
            instrument=self,
            initial_value=kwargs.get("acq_delay", 0),  # float("nan"),
            unit="s",
            # in principle the values should be a few 100 ns but the validator is here
            # only to protect against silly typos that lead to out of memory errors.
            vals=validators.Numbers(min_value=0, max_value=100e-6),
        )
        """Delay between the start of the readout pulse and the start of
        the acquisition. Note that some hardware backends do not support
        starting a pulse and the acquisition in the same clock cycle making 0
        delay an invalid value."""

        self.integration_time = ManualParameter(
            name="integration_time",
            instrument=self,
            initial_value=kwargs.get("integration_time", 1e-6),
            unit="s",
            # in principle the values should be a few us but the validator is here
            # only to protect against silly typos that lead to out of memory errors.
            vals=validators.Numbers(min_value=0, max_value=100e-6),
        )
        """Integration time for the readout acquisition."""

        self.reset_clock_phase = ManualParameter(
            name="reset_clock_phase",
            instrument=self,
            initial_value=kwargs.get("reset_clock_phase", True),
            vals=validators.Bool(),
        )
        """The phase of the measurement clock will be reset by the
        control hardware at the start of each measurement if
        ``reset_clock_phase=True``."""

        self.acq_weights_a = ManualParameter(
            name="acq_weights_a",
            instrument=self,
            initial_value=kwargs.get("acq_weights_a", None),
            vals=validators.Arrays(),
        )
        """The weights for the I path. Used when specifying the
        ``"NumericalWeightedIntegrationComplex"`` acquisition protocol."""

        self.acq_weights_b = ManualParameter(
            name="acq_weights_b",
            instrument=self,
            initial_value=kwargs.get("acq_weights_b", None),
            vals=validators.Arrays(),
        )
        """The weights for the Q path. Used when specifying the
        ``"NumericalWeightedIntegrationComplex"`` acquisition protocol."""

        self.acq_weights_sampling_rate = ManualParameter(
            name="acq_weights_sampling_rate",
            instrument=self,
            initial_value=kwargs.get("acq_weights_sampling_rate", None),
            vals=validators.Numbers(min_value=1, max_value=10e9),
        )
        """The sample rate of the weights arrays, in Hertz. Used when specifying the
        ``"NumericalWeightedIntegrationComplex"`` acquisition protocol."""

        ro_acq_weight_type_validator = validators.Enum("SSB", "Numerical")
        self.acq_weight_type = ManualParameter(
            name="acq_weight_type",
            instrument=self,
            initial_value=kwargs.get("acq_weight_type", "SSB"),
            vals=ro_acq_weight_type_validator,
        )


class BasicTransmonElement(DeviceElement):
    """
    A device element representing a single fixed-frequency transmon qubit coupled to a
    readout resonator.
    """

    def __init__(self, name: str, **kwargs):
        """
        Parameters
        ----------
        name
            The name of the transmon element.
        kwargs
            Can be used to pass submodule initialization data by using submodule name
            as keyword and as argument a dictionary containing the submodule parameter
            names and their value.
        """
        submodules_to_add = {
            "reset": IdlingReset,
            "rxy": RxyDRAG,
            "measure": DispersiveMeasurement,
            "ports": Ports,
            "clock_freqs": ClocksFrequencies,
        }
        submodule_data = {
            sub_name: kwargs.pop(sub_name, {}) for sub_name in submodules_to_add.keys()
        }
        super().__init__(name, **kwargs)

        for sub_name, sub_class in submodules_to_add.items():
            self.add_submodule(
                sub_name,
                sub_class(
                    parent=self, name=sub_name, **submodule_data.get(sub_name, {})
                ),
            )

        self.reset: IdlingReset
        """Submodule :class:`~.IdlingReset`."""
        self.rxy: RxyDRAG
        """Submodule :class:`~.RxyDRAG`."""
        self.measure: DispersiveMeasurement
        """Submodule :class:`~.DispersiveMeasurement`."""
        self.ports: Ports
        """Submodule :class:`~.Ports`."""
        self.clock_freqs: ClocksFrequencies
        """Submodule :class:`~.ClocksFrequencies`."""

    def __getstate__(self):
        """
        Serializes `BasicTransmonElement` by obtaining relevant information from
        :func:`~Instrument.snapshot()`. The relevant information consists of the name
        of the transmon element and a dictionary for each submodule containing its
        parameter names and corresponding values.
        """
        snapshot = self.snapshot()

        data = {"name": snapshot["name"]}
        for submodule_name, submodule_data in snapshot["submodules"].items():
            parameter_dict = {}
            for parameter_name, parameter_data in submodule_data["parameters"].items():
                parameter_dict[parameter_name] = parameter_data["value"]
            data[submodule_name] = parameter_dict

        state = {
            "deserialization_type": self.__class__.__name__,
            "mode": "__init__",
            "data": data,
        }
        return state

    def _generate_config(self) -> Dict[str, Dict[str, OperationCompilationConfig]]:
        """
        Generates part of the device configuration specific to a single qubit.

        This method is intended to be used when this object is part of a
        device object containing multiple elements.
        """
        qubit_config = {
            f"{self.name}": {
                "reset": OperationCompilationConfig(
                    factory_func=pulse_library.IdlePulse,
                    factory_kwargs={
                        "duration": self.reset.duration(),
                    },
                ),
                # example of a pulse with a parametrized mapping, using a factory
                "Rxy": OperationCompilationConfig(
                    factory_func=pulse_factories.rxy_drag_pulse,
                    factory_kwargs={
                        "amp180": self.rxy.amp180(),
                        "motzoi": self.rxy.motzoi(),
                        "port": self.ports.microwave(),
                        "clock": f"{self.name}.01",
                        "duration": self.rxy.duration(),
                    },
                    gate_info_factory_kwargs=[
                        "theta",
                        "phi",
                    ],  # the keys from the gate info to pass to the factory function
                ),
                # the measurement also has a parametrized mapping, and uses a
                # factory function.
                "measure": OperationCompilationConfig(
                    factory_func=measurement_factories.dispersive_measurement,
                    factory_kwargs={
                        "port": self.ports.readout(),
                        "clock": f"{self.name}.ro",
                        "pulse_type": self.measure.pulse_type(),
                        "pulse_amp": self.measure.pulse_amp(),
                        "pulse_duration": self.measure.pulse_duration(),
                        "acq_delay": self.measure.acq_delay(),
                        "acq_duration": self.measure.integration_time(),
                        "acq_channel": self.measure.acq_channel(),
                        "acq_protocol_default": "SSBIntegrationComplex",
                        "reset_clock_phase": self.measure.reset_clock_phase(),
                        "acq_weights_a": self.measure.acq_weights_a(),
                        "acq_weights_b": self.measure.acq_weights_b(),
                        "acq_weights_sampling_rate": self.measure.acq_weights_sampling_rate(),
                    },
                    gate_info_factory_kwargs=["acq_index", "bin_mode", "acq_protocol"],
                ),
            }
        }
        return qubit_config

    def generate_device_config(self) -> DeviceCompilationConfig:
        """
        Generates a valid device config for the quantify-scheduler making use of the
        :func:`~.circuit_to_device.compile_circuit_to_device` function.

        This enables the settings of this qubit to be used in isolation.

        .. note:

            This config is only valid for single qubit experiments.
        """
        cfg_dict = {
            "backend": "quantify_scheduler.backends"
            ".circuit_to_device.compile_circuit_to_device",
            "elements": self._generate_config(),
            "clocks": {
                f"{self.name}.01": self.clock_freqs.f01(),
                f"{self.name}.12": self.clock_freqs.f12(),
                f"{self.name}.ro": self.clock_freqs.readout(),
            },
            "edges": {},
        }
        dev_cfg = DeviceCompilationConfig.parse_obj(cfg_dict)

        return dev_cfg
