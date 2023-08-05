import enum
from typing import Optional

import attrs
from attrs.validators import instance_of, optional


class ZMQType(enum.Enum):
    inproc = "inproc"
    ipc = "ipc"
    tcp = "tcp"


@attrs.define
class ZMQConfig:
    type: ZMQType = attrs.field(validator=instance_of(ZMQType), converter=ZMQType)
    host: str = attrs.field(validator=instance_of(str))
    port: Optional[int] = attrs.field(validator=optional(instance_of(int)), default=None)

    def __attrs_post_init__(self):
        if self.type == ZMQType.inproc and self.port is not None:
            raise ValueError("inproc type should not have `port`")

    def to_address(self):
        if self.type == ZMQType.tcp:
            return f"tcp://{self.host}:{self.port}"

        if self.type in {ZMQType.inproc, ZMQType.ipc}:
            return f"{self.type.value}://{self.host}"

        raise TypeError(f"Unsupported ZMQ type: {self.type}")

    @staticmethod
    def from_string(string: str) -> "ZMQConfig":
        if "://" not in string:
            raise ValueError(f"valid ZMQ config should be like tcp://127.0.0.1:12345")

        socket_type, host_port = string.split("://", 1)
        allowed_types = {member.value for member in ZMQType}
        if socket_type not in allowed_types:
            raise ValueError(f"supported ZMQ types are: {allowed_types}")

        socket_type = ZMQType(socket_type)
        if socket_type in {ZMQType.inproc, ZMQType.ipc}:
            host = host_port
            port = 0
        else:
            host, port = host_port.split(":")

        return ZMQConfig(ZMQType(socket_type), host, int(port))
