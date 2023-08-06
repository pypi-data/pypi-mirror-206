from __future__ import annotations

import ctypes


class GoStr(ctypes.Structure):
    _fields_ = [("p", ctypes.c_char_p), ("n", ctypes.c_int64)]

    @classmethod
    def from_param(cls, value: str) -> GoStr:
        """
        Converts a python string to a GoStr
        :param value: raw python string
        :return: golang string
        """
        byte_value = value.encode()
        return cls(byte_value, len(byte_value))

    def __str__(self) -> str:
        return ctypes.string_at(self.p, self.n).decode()
