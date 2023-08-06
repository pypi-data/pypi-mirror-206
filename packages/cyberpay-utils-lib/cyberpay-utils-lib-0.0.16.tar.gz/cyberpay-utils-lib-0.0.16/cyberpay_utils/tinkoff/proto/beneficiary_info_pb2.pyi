from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BeneficiaryAddress(_message.Message):
    __slots__ = ["address", "type"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    address: str
    type: str
    def __init__(self, type: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class BeneficiaryDocument(_message.Message):
    __slots__ = ["date", "division", "expire_date", "number", "organization", "serial", "type"]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DIVISION_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_DATE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    SERIAL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    date: str
    division: str
    expire_date: str
    number: str
    organization: str
    serial: str
    type: str
    def __init__(self, type: _Optional[str] = ..., serial: _Optional[str] = ..., number: _Optional[str] = ..., date: _Optional[str] = ..., organization: _Optional[str] = ..., division: _Optional[str] = ..., expire_date: _Optional[str] = ...) -> None: ...

class BeneficiaryInfo(_message.Message):
    __slots__ = ["addresses", "birth_date", "birth_place", "citizenship", "documents", "email", "first_name", "inn", "is_self_employed", "last_name", "middle_mame", "phone_number", "type"]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    BIRTH_PLACE_FIELD_NUMBER: _ClassVar[int]
    CITIZENSHIP_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    INN_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_EMPLOYED_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_MAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[BeneficiaryAddress]
    birth_date: str
    birth_place: str
    citizenship: str
    documents: _containers.RepeatedCompositeFieldContainer[BeneficiaryDocument]
    email: str
    first_name: str
    inn: str
    is_self_employed: bool
    last_name: str
    middle_mame: str
    phone_number: str
    type: str
    def __init__(self, type: _Optional[str] = ..., first_name: _Optional[str] = ..., middle_mame: _Optional[str] = ..., last_name: _Optional[str] = ..., is_self_employed: bool = ..., birth_date: _Optional[str] = ..., birth_place: _Optional[str] = ..., citizenship: _Optional[str] = ..., phone_number: _Optional[str] = ..., email: _Optional[str] = ..., documents: _Optional[_Iterable[_Union[BeneficiaryDocument, _Mapping]]] = ..., addresses: _Optional[_Iterable[_Union[BeneficiaryAddress, _Mapping]]] = ..., inn: _Optional[str] = ...) -> None: ...

class BeneficiaryInfoWithID(_message.Message):
    __slots__ = ["addresses", "beneficiary_id", "birth_date", "birth_place", "citizenship", "documents", "email", "first_name", "inn", "is_self_employed", "last_name", "middle_mame", "phone_number", "type"]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_ID_FIELD_NUMBER: _ClassVar[int]
    BIRTH_DATE_FIELD_NUMBER: _ClassVar[int]
    BIRTH_PLACE_FIELD_NUMBER: _ClassVar[int]
    CITIZENSHIP_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    INN_FIELD_NUMBER: _ClassVar[int]
    IS_SELF_EMPLOYED_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLE_MAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[BeneficiaryAddress]
    beneficiary_id: str
    birth_date: str
    birth_place: str
    citizenship: str
    documents: _containers.RepeatedCompositeFieldContainer[BeneficiaryDocument]
    email: str
    first_name: str
    inn: str
    is_self_employed: bool
    last_name: str
    middle_mame: str
    phone_number: str
    type: str
    def __init__(self, type: _Optional[str] = ..., first_name: _Optional[str] = ..., middle_mame: _Optional[str] = ..., last_name: _Optional[str] = ..., is_self_employed: bool = ..., birth_date: _Optional[str] = ..., birth_place: _Optional[str] = ..., citizenship: _Optional[str] = ..., phone_number: _Optional[str] = ..., email: _Optional[str] = ..., documents: _Optional[_Iterable[_Union[BeneficiaryDocument, _Mapping]]] = ..., addresses: _Optional[_Iterable[_Union[BeneficiaryAddress, _Mapping]]] = ..., inn: _Optional[str] = ..., beneficiary_id: _Optional[str] = ...) -> None: ...
