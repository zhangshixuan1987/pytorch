from typing import Any, Union, Optional
import torch
from torch import device as _device

_device_t = Union[_device, str, int, None]

def _get_device_index(device: _device_t, optional: bool = False) -> int:
    if isinstance(device, int):
        return device
    if isinstance(device, str):
        device = torch.device(device)
    device_index: Optional[int] = None
    if isinstance(device, torch.device):
        if torch.acc.current_accelerator() != device.type:
            raise ValueError(
                f"{device.type} doesn't match the current accelerator {torch.acc.current_accelerator()}."
            )
        device_index = device.index
    if device_index is None:
        if not optional:
            raise ValueError(
                f"Expected a torch.device with a specified index or an integer, but got:{device}"
            )
        return torch.acc.current_device()
    return device_index
