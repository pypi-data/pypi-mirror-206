"""
Utilities for dealing with subprocesses
"""

from __future__ import annotations

import asyncio
import subprocess
from collections.abc import Callable, Sequence
from typing import cast, TYPE_CHECKING

from antsibull_core.logging import log

if TYPE_CHECKING:
    from _typeshed import StrOrBytesPath
    from twiggy.log import Logger

mlog = log.field(mod=__name__)


def run(
    args: Sequence[StrOrBytesPath],
    logger: Logger = mlog.fields(func="run"),
    capture_output: bool = True,
    check: bool = True,
    warn: bool = False,
    **kwargs,
) -> subprocess.CompletedProcess:
    """
    Run a command in a subprocess and log it.

    :param args: Command to run
    :param logger: Where to log command.
    :param capture_output: Whether to capture stdout and stderr. Returns text.
    :param check: Whether to raise a `subprocess.CalledProcessError` when the
                  command returns a non-zero exit code
    :param warn: Whether to log stderr as warnings. By default, stdout and
                 stderr are logged as debug
    """
    if "text" or "universal_newlines" in kwargs:
        raise ValueError("This function always returns text")
    kwargs.setdefault("errors", "surrogateescape")
    log = getattr(logger, "warning" if warn else "debug")
    log(f"Running subprocess: {args!r}")
    proc = subprocess.run(args, capture_output=capture_output, check=check, **kwargs)
    for line in (proc.stderr or "").splitlines():
        log(f"stderr: {line}")
    for line in (proc.stdout or "").splitlines():
        logger.debug(f"stdout: {line}")
    return proc


async def _stream_log(name: str, log: Callable, stream: asyncio.StreamReader) -> None:
    line = await stream.readline()
    while True:
        if not line:
            break
        log(f'{name}: {line}')
        line = await stream.readline()


async def async_run(
    args: Sequence[StrOrBytesPath],
    logger: Logger | None = None,
    check: bool = True,
    log_stderr: str | False = "debug",
    log_stdout: str | False = False,
    **kwargs,
) -> subprocess.CompletedProcess:
    """
    Asynchronously run a command in a subprocess and log it.
    For some usecass, you may still need to call
    asyncio.create_subprocess_exec() directly to have more control.

    :param args: Command to run
    :param logger: Where to log command.
    :param capture_output: Whether to capture stdout and stderr. Returns text.
    :param check: Whether to raise a `subprocess.CalledProcessError` when the
                  command returns a non-zero exit code
    :param warn: Whether to log stderr as warnings. By default, stdout and
                 stderr are logged as debug
    """
    logger = logger or mlog.fields(func="run")
    log(f"Running subprocess: {args!r}")
    proc = await asyncio.create_subprocess_exec(*args, **kwargs)

    stdout, stderr = await proc.communicate()
    if stderr is not None:
        stderr = stderr.decode("utf-8")
        for line in stderr.splitlines():
            log(f"stderr: {line}")
    if stdout is not None:
        stdout = stdout.decode("utf-8")
        for line in stdout.splitlines():
            logger.debug(f"stdout: {line}")

    completed = subprocess.CompletedProcess(
        args=args, returncode=proc.returncode or 0, stdout=stdout, stderr=stderr
    )
    if check:
        completed.check_returncode()
    return completed
