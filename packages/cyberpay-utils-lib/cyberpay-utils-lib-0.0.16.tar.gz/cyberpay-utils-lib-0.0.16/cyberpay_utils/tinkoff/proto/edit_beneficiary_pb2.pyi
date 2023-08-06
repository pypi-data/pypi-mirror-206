from cyberpay_utils.tinkoff.proto import beneficiary_info_pb2 as _beneficiary_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditBeneficiaryRequest(_message.Message):
    __slots__ = ["beneficiary_id", "info"]
    BENEFICIARY_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    beneficiary_id: str
    info: _beneficiary_info_pb2.BeneficiaryInfo
    def __init__(self, beneficiary_id: _Optional[str] = ..., info: _Optional[_Union[_beneficiary_info_pb2.BeneficiaryInfo, _Mapping]] = ...) -> None: ...
