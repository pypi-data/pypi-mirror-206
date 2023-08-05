# Copyright (c) ONNX Project Contributors

# SPDX-License-Identifier: Apache-2.0
# pylint: disable=W0221

from typing import Optional, Tuple

import numpy as np

from onnx import TensorProto
from onnx.helper import np_dtype_to_tensor_dtype
from onnx.numpy_helper import float8e4m3_to_float32, float8e5m2_to_float32
from onnx.reference.custom_element_types import (
    float8e4m3fn,
    float8e4m3fnuz,
    float8e5m2,
    float8e5m2fnuz,
)
from onnx.reference.op_run import OpRun


class DequantizeLinear(OpRun):
    def get_x_type(self, x: np.ndarray) -> int:
        if x.dtype == float8e4m3fn and x.dtype.descr[0][0] == "e4m3fn":
            return TensorProto.FLOAT8E4M3FN
        if x.dtype == float8e4m3fnuz and x.dtype.descr[0][0] == "e4m3fnuz":
            return TensorProto.FLOAT8E4M3FNUZ
        if x.dtype == float8e5m2 and x.dtype.descr[0][0] == "e5m2":
            return TensorProto.FLOAT8E5M2
        if x.dtype == float8e5m2fnuz and x.dtype.descr[0][0] == "e5m2fnuz":
            return TensorProto.FLOAT8E5M2FNUZ
        return np_dtype_to_tensor_dtype(x.dtype)

    @staticmethod
    def reshape_input(
        value: np.ndarray, shape: Tuple[int, ...], axis: Optional[int]
    ) -> np.ndarray:
        if axis is None:
            raise ValueError("axis cannot be None.")
        if len(value.shape) == 0:
            return value
        dims = [1] * len(shape)
        dims[axis] = value.size
        return value.reshape(tuple(dims))

    def _run(
        self,
        x: np.ndarray,
        x_scale: np.ndarray,
        x_zero_point: Optional[np.ndarray] = None,
        axis: Optional[int] = None,
    ):  # type: ignore
        if len(x_scale.shape) > 1:
            raise RuntimeError("Input 2 must be a vector or a number.")

        x_type = self.get_x_type(x)
        if x_zero_point is not None:
            zero_type = self.get_x_type(x_zero_point)
            if x_type != zero_type:
                raise RuntimeError(
                    f"Type mismatch {x_type} != {zero_type} in DequantizeLinear."
                )
            if x_type in (
                TensorProto.FLOAT8E4M3FN,
                TensorProto.FLOAT8E4M3FNUZ,
                TensorProto.FLOAT8E5M2,
                TensorProto.FLOAT8E5M2FNUZ,
            ):
                raise RuntimeError(
                    f"x_zero_point not supported for float 8 type {x_type}."
                )

            dx = x.astype(np.float32) - DequantizeLinear.reshape_input(
                x_zero_point, x.shape, axis
            )
        else:
            if x_type == TensorProto.FLOAT8E4M3FN:
                dx = float8e4m3_to_float32(x)
            elif x_type == TensorProto.FLOAT8E4M3FNUZ:
                dx = float8e4m3_to_float32(x, uz=True)
            elif x_type == TensorProto.FLOAT8E5M2:
                dx = float8e5m2_to_float32(x)
            elif x_type == TensorProto.FLOAT8E5M2FNUZ:
                dx = float8e5m2_to_float32(x, fn=True, uz=True)
            else:
                dx = x.astype(np.float32)
        y = dx * DequantizeLinear.reshape_input(x_scale, x.shape, axis)
        return (y.astype(np.float32),)
