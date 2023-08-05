from typing import Union, TypeVar, Iterable, Type
import io
import pyarrow
from .tables import TableBase

GenericTable = TypeVar("GenericTable", bound=TableBase)


def streaming_read(
    source: Union[bytes, pyarrow.NativeFile, io.BinaryIO], table_class: Type[GenericTable]
) -> Iterable[GenericTable]:
    batch_reader = pyarrow.ipc.RecordBatchStreamReader(source)
