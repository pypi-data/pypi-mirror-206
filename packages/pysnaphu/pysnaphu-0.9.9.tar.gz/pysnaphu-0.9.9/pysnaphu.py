import os
import tempfile
from typing import Any

import numpy as np
from numpy.typing import NDArray


def snaphu(
    input: NDArray[np.complex64], snaphu_bin: str = "snaphu", **snaphu_params: Any
) -> NDArray[np.float32]:
    assert len(input.shape) == 2, input.shape
    assert input.dtype == np.complex64, input.dtype

    h, w = input.shape

    with tempfile.TemporaryDirectory() as tmpdir:
        inpath = os.path.join(tmpdir, "input")
        outpath = os.path.join(tmpdir, "output")
        input.tofile(inpath)

        params = {
            "INFILEFORMAT": "COMPLEX_DATA",
            "OUTFILE": outpath,
            "OUTFILEFORMAT": "FLOAT_DATA",
            **snaphu_params,
        }
        cliparams = " ".join(f'-C "{k} {v}"' for k, v in params.items())
        cmd = f"{snaphu_bin} {cliparams} {inpath} {w}"
        assert not os.system(cmd)

        o = np.fromfile(outpath, dtype=np.float32)
        o = o.reshape(h, w)

    return o


__all__ = {"snaphu": snaphu}
