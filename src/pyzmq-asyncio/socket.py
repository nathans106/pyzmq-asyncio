from typing import Optional, Self

import zmq
from zmq.sugar.socket import _SocketContext, _SocketType


class Socket:
    def __init__(
        self,
        ctx_or_socket: zmq.Context,
        socket_type: int,
        *,
        shadow: Optional[int] = 0,
        copy_threshold: Optional[int] = None,
    ):
        self.__socket: zmq.Socket = zmq.Socket(
            ctx_or_socket, socket_type, shadow=shadow, copy_threshold=copy_threshold
        )

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.__socket.close()

    def bind(self, addr: str) -> _SocketContext[_SocketType]:
        return self.__socket.bind(addr)

    def connect(self, addr: str) -> _SocketContext[_SocketType]:
        return self.__socket.connect(addr)

    def fileno(self) -> int:
        return self.__socket.fileno()

    def subscribe(self, topic: str | bytes) -> None:
        self.__socket.subscribe(topic)

    def unsubscribe(self, topic: str | bytes) -> None:
        self.__socket.unsubscribe(topic)
