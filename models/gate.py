from config.db import Base
import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Float, Text, Enum, UniqueConstraint, func
from sqlalchemy.orm import relationship


class Society(Base):
    __tablename__ = 'society'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    lat = Column(Float, index=2)
    long = Column(Float, index=3)
    address = Column(String(150), index=4)
    manager_id = Column(Integer, ForeignKey('manager.id'), index=5)
    manager = relationship('Manager', back_populates='society')
    description = Column(String(100), index=6)
    created_at = Column(DateTime, index=7, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=8)


class Manager(Base):
    __tablename__ = 'manager'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    email = Column(String(50), index=2)
    phone = Column(String(50), index=3)
    profilePic = Column(String(255), index=4)
    password = Column(String(50), index=5)
    society_id = Column(Integer, ForeignKey('society.id'), index=6)
    society = relationship('Society', back_populates='manager')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=7)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=8)


class Block(Base):
    __tablename__ = 'block'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    society_id = Column(Integer, ForeignKey('society.id'), index=2)
    society = relationship('Society', back_populates='block')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=3)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=4)


class Flat(Base):
    __tablename__ = 'flat'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    block_id = Column(Integer, ForeignKey('block.id'), index=2)
    block = relationship('Block', back_populates='flat')
    society_id = Column(Integer, ForeignKey('society.id'), index=3)
    society = relationship('Society', back_populates='flat')
    device_token = Column(String(255), index=4)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=5)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=6)


class Guard(Base):
    __tablename__ = 'guard'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    phone = Column(String(50), index=2)
    flat_id = Column(Integer, ForeignKey('flat.id'), index=3)
    flat = relationship('Flat', back_populates='guard')
    society_id = Column(Integer, ForeignKey('society.id'), index=4)
    society = relationship('Society', back_populates='guard')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=5)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=6)


class Notification(Base):
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    title = Column(String(50), index=1)
    image = Column(String(255), index=2, default=None)
    description = Column(String(255), index=2)
    society_id = Column(Integer, ForeignKey('society.id'), index=3)
    society = relationship('Society', back_populates='notification')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=4)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=5)


class Visitor(Base):
    __tablename__ = 'visitor'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    phone = Column(String(50), index=2)
    flat_id = Column(Integer, ForeignKey('flat.id'), index=3)
    flat = relationship('Flat', back_populates='visitor')
    society_id = Column(Integer, ForeignKey('society.id'), index=4)
    society = relationship('Society', back_populates='visitor')
    allowed = Column(Boolean, index=5, default=False)
    photo = Column(String(255), index=6, default=None)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=7)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=8)


class Resident(Base):
    __tablename__ = 'resident'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    phone = Column(String(50), index=2)
    device_token = Column(String(255), index=3)
    verified = Column(Boolean, index=4, default=False)
    flat_id = Column(Integer, ForeignKey('flat.id'), index=5)
    flat = relationship('Flat', back_populates='resident')
    society_id = Column(Integer, ForeignKey('society.id'), index=6)
    society = relationship('Society', back_populates='resident')
    allowed = Column(Boolean, index=5, default=False)
    photo = Column(String(255), index=6, default=None)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=7)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=8)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    vehicle_type = Column(String(50), index=2)
    vehicle_number = Column(String(50), index=3)
    resident_id = Column(Integer, ForeignKey('resident.id'), index=4)
    resident = relationship('Resident', back_populates='vehicle')
    society_id = Column(Integer, ForeignKey('society.id'), index=5)
    society = relationship('Society', back_populates='vehicle')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=6)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=7)


class MessageToGuard(Base):
    __tablename__ = 'message_to_guard'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    message = Column(String(255), index=1)
    guard_id = Column(Integer, ForeignKey('guard.id'), index=2)
    guard = relationship('Guard', back_populates='message_to_guard')
    resident_id = Column(Integer, ForeignKey('resident.id'), index=3)
    resident = relationship('Resident', back_populates='message_to_guard')
    society_id = Column(Integer, ForeignKey('society.id'), index=4)
    society = relationship('Society', back_populates='message_to_guard')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=5)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=6)


class PreApprovedGuest(Base):
    __tablename__ = 'pre_approved_guest'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    phone = Column(String(50), index=2)
    otp = Column(Integer, index=3, default=0000)
    resident_id = Column(Integer, ForeignKey('resident.id'), index=4)
    resident = relationship('Resident', back_populates='pre_approved_guest')
    flat_id = Column(Integer, ForeignKey('flat.id'), index=5)
    flat = relationship('Flat', back_populates='pre_approved_guest')
    society_id = Column(Integer, ForeignKey('society.id'), index=6)
    society = relationship('Society', back_populates='pre_approved_guest')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=7)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=8)


class PreApprovedThirdParty(Base):
    __tablename__ = 'pre_approved_third_party'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(50), index=1)
    phone = Column(String(50), index=2, default=None)
    vehicleType = Column(String(50), index=3)
    vehicleNumber = Column(String(50), index=4)
    otp = Column(Integer, index=5, default=0000)
    resident_id = Column(Integer, ForeignKey('resident.id'), index=6)
    resident = relationship('Resident', back_populates='pre_approved_third_party')
    flat_id = Column(Integer, ForeignKey('flat.id'), index=7)
    flat = relationship('Flat', back_populates='pre_approved_third_party')
    society_id = Column(Integer, ForeignKey('society.id'), index=8)
    society = relationship('Society', back_populates='pre_approved_third_party')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=9)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=10)


class DailyHelps(Base):
    __tablename__ = 'daily_helps'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(100), index=1)
    workType = Column(String(100), index=2)
    resident_id = Column(Integer, ForeignKey('resident.id'), index=3)
    resident = relationship('Resident', back_populates='daily_helps')
    society_id = Column(Integer, ForeignKey('society.id'), index=4)
    society = relationship('Society', back_populates='daily_helps')
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=5)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=6)


class EmergencyNos(Base):
    __tablename__ = 'emergency_nos'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(100), index=1)
    phone = Column(String(100), index=2)
    society_id = Column(Integer, ForeignKey('society.id'), index=3)
    society = relationship('Society', back_populates='emergency_nos')
    image = Column(String(255), index=4)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=5)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=6)


class HelpDesk(Base):
    __tablename__ = 'help_desk'
    id = Column(Integer, primary_key=True, autoincrement=True, index=0)
    name = Column(String(100), index=1)
    phone = Column(String(100), index=2)
    resident_id = Column(Integer, ForeignKey('resident.id'), index=3)
    resident = relationship('Resident', back_populates='help_desk')
    requestType = Column(String(100), index=4)
    requestMessage = Column(String(255), index=5)
    society_id = Column(Integer, ForeignKey('society.id'), index=6)
    society = relationship('Society', back_populates='help_desk')
    image = Column(String(255), index=7)
    resolvedStatus = Column(Boolean, index=8, default=False)
    resolvedComment = Column(String(255), index=9)
    created_at = Column(DateTime, default=datetime.datetime.utcnow(), index=10)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now, index=11)
