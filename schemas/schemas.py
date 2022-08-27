from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class Society(BaseModel):
    id: Optional[int] | None
    name: str
    lat: float
    long: float
    address: str
    manager_id: int
    description: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Manager(BaseModel):
    id: Optional[int] | None
    name: str
    email: str
    phone: str
    profilePic: str
    password: str
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Block(BaseModel):
    id: int
    name: str
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Flat(BaseModel):
    id: int
    name: str
    block_id: int
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Guard(BaseModel):
    id: int
    name: str
    phone: str
    flat_id: int
    society_id: int
    device_token: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Notification(BaseModel):
    id: int
    title: str
    image: str
    description: str
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Visitor(BaseModel):
    id: int
    name: str
    phone: str
    flat_id: int
    society_id: int
    allowed: bool = False
    photo: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Resident(BaseModel):
    id: int
    name: str
    phone: str
    device_token: str
    verified: bool = False
    flat_id: int
    society_id: int
    allowed: bool = False
    photo: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Vehicle(BaseModel):
    id: int
    name: str
    vehicle_type: str
    vehicle_number: str
    resident_id: int
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class MessageToGuard(BaseModel):
    id: int
    message: str
    guard_id: int
    resident_id: int
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PreApprovedGuest(BaseModel):
    id: int
    name: str
    phone: str
    otp: int
    resident_id: int
    flat_id: int
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class PreApprovedThirdParty(BaseModel):
    id: int
    name: str
    phone: str
    vehicleType: str
    vehicleNumber: str
    otp: int
    resident_id: int
    flat_id: int
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class DailyHelps(BaseModel):
    id: int
    name: str
    workType: str
    resident_id: int
    society_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class EmergencyNos(BaseModel):
    id: int
    name: str
    phone: str
    society_id: int
    image: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class HelpDesk(BaseModel):
    id: int
    name: str
    phone: str
    resident_id: int
    requestType: str
    requestMessage: str
    society_id: int
    image: str
    resolvedStatus: bool = False
    resolvedComment: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
