from __future__ import annotations

from typing import Any, Callable, Dict, Generator, Optional, Type


class KMessageType:
    """Kelvin Message Type representation"""

    _SUBTYPES: Dict[str, Type[KMessageType]] = {}
    _TYPE: str = ""

    msg_type: str
    components: Dict[str, str]

    def __init_subclass__(cls) -> None:
        if cls._TYPE:
            KMessageType._SUBTYPES[cls._TYPE] = cls

    def __init__(self, msg_type: str, components: Optional[Dict[str, str]]) -> None:
        self.msg_type = msg_type
        self.components = components or {}

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., Any], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> KMessageType:
        if isinstance(v, str):
            return cls.from_string(v)

        if isinstance(v, KMessageType):
            return v

        raise TypeError('Invalid type for KMessageType. KMessageType or string required.')

    @classmethod
    def from_krn(cls, msg_type: str, components: Optional[Dict[str, str]]) -> KMessageType:
        T = KMessageType._SUBTYPES.get(msg_type, None)
        if T is not None:
            return T.from_krn(msg_type, components)

        return cls(msg_type, components)

    @classmethod
    def from_string(cls, v: str) -> KMessageType:
        if not isinstance(v, str):
            raise TypeError('string required')

        msg_type, *components = v.split(";")
        components_dict = {}
        for component in components:
            try:
                key, value = component.split("=", 1)
            except ValueError:
                raise ValueError(f"Invalid type '{v}'. Expected format '<type>;<key>=<value>'")
            components_dict[key] = value

        return cls.from_krn(msg_type, components_dict)

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other):
            return False

        return self.msg_type == other.msg_type and self.components == other.components

    def __str__(self) -> str:
        return ";".join(
            [self.msg_type, *[f"{key}={value}" for key, value in self.components.items() if value]]
        )

    def __repr__(self) -> str:
        components_str = ";".join(f"{key}={value}" for key, value in self.components.items())
        return f"{self.__class__.__name__}('{self.msg_type}', '{components_str}')"

    def encode(self) -> str:
        return str(self)


class KMessageTypeICD(KMessageType):
    """Common class to KTypes that use ICD"""

    icd: Optional[str] = None

    def __init__(self, icd: Optional[str] = None) -> None:
        super().__init__(self._TYPE, {"icd": icd} if icd else None)
        self.icd = icd

    @classmethod
    def from_krn(cls, msg_type: str, components: Optional[Dict[str, str]]) -> KMessageTypeICD:
        icd = components.get("icd", None) if components else None
        if msg_type != cls._TYPE:
            raise ValueError(
                f"Error parsing {cls.__class__.__name__}. Expected {cls._TYPE}, got {msg_type}"
            )
        return cls(icd)


class KMessageTypeData(KMessageTypeICD):
    _TYPE = "data"


class KMessageTypeControl(KMessageTypeICD):
    _TYPE = "control"


class KMessageTypeControlStatus(KMessageTypeICD):
    _TYPE = "control-status"
