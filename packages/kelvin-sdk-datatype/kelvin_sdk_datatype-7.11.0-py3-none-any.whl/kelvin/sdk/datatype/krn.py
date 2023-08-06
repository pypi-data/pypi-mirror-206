from __future__ import annotations

from typing import Any, Callable, Dict, Generator, Optional, Type


class KRN:
    """Kelvin Resource Name representation"""

    _KRN_TYPES: Dict[str, Type[KRN]] = {}
    _NS_ID: Optional[str] = None

    ns_id: str
    ns_string: str

    def __init_subclass__(cls) -> None:
        if cls._NS_ID:
            KRN._KRN_TYPES[cls._NS_ID] = cls

    def __init__(self, ns_id: str, ns_string: str) -> None:
        self.ns_id = ns_id
        self.ns_string = ns_string

    @classmethod
    def __get_validators__(cls) -> Generator[Callable[..., Any], None, None]:
        yield cls.validate

    @classmethod
    def validate(cls, v: Any) -> KRN:
        if isinstance(v, str):
            return cls.from_string(v)

        if isinstance(v, KRN):
            return v

        raise TypeError('Invalid type for KRN. KRN or string required.')

    @classmethod
    def from_krn(cls, ns_id: str, ns_string: str) -> KRN:
        return cls(ns_id, ns_string)

    @classmethod
    def from_string(cls, v: str) -> KRN:
        try:
            krn, ns_id, ns_string = v.split(":", 2)
        except ValueError:
            raise ValueError("expected format 'krn:<nid>:<nss>'")

        if krn != "krn":
            raise ValueError("expected start by 'krn'")

        T = KRN._KRN_TYPES.get(ns_id, KRN)
        return T.from_krn(ns_id, ns_string)

    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other):
            return False

        return self.ns_id == other.ns_id and self.ns_string == other.ns_string

    def __str__(self) -> str:
        return f"krn:{self.ns_id}:{self.ns_string}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self)})"

    def encode(self) -> str:
        return str(self)


class KRNAssetMetric(KRN):
    _NS_ID: str = "am"
    """Kelvin Resource Name Asset Metric"""
    asset: str
    metric: str

    def __init__(self, asset: str, metric: str) -> None:
        super().__init__(self._NS_ID, asset + "/" + metric)
        self.asset = asset
        self.metric = metric

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(asset='{self.asset}', metric='{self.metric}')"

    @classmethod
    def from_krn(cls, ns_id: str, ns_string: str) -> KRNAssetMetric:
        if ns_id != cls._NS_ID:
            raise ValueError(
                f"Error parsing {cls.__class__.__name__}. Expected {cls._NS_ID}, got {ns_id}"
            )

        try:
            asset, metric = ns_string.split("/", 1)
        except ValueError:
            raise ValueError("expected format 'krn:am:<asset>/<metric>'")

        return cls(asset, metric)


class KRNWorkload(KRN):
    _NS_ID: str = "wl"
    """Kelvin Resource Name Asset Metric"""
    node: str
    workload: str

    def __init__(self, node: str, workload: str) -> None:
        super().__init__(self._NS_ID, node + "/" + workload)
        self.node = node
        self.workload = workload

    @property
    def node_name(self) -> str:
        "Backwards compatibility"
        return self.node

    @property
    def workload_name(self) -> str:
        "Backwards compatibility"
        return self.workload

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(node='{self.node}', workload='{self.workload}')"

    @classmethod
    def from_krn(cls, ns_id: str, ns_string: str) -> KRNWorkload:
        if ns_id != cls._NS_ID:
            raise ValueError(
                f"Error parsing {cls.__class__.__name__}. Expected {cls._NS_ID}, got {ns_id}"
            )

        try:
            node, workload = ns_string.split("/", 1)
        except ValueError:
            raise ValueError("expected format 'krn:wl:<node>/<workload>'")

        return cls(node, workload)
