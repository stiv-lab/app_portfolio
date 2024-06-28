# data/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class MarketInstrument(Base):
    __tablename__ = 'market_instruments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    symbol = Column(String, unique=True, nullable=False)
    type = Column(String)

class LatestPrice(Base):
    __tablename__ = 'latest_prices'
    id = Column(Integer, primary_key=True)
    instrument_id = Column(Integer, ForeignKey('market_instruments.id'), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    instrument = relationship("MarketInstrument", back_populates="latest_price")

class PriceArchive(Base):
    __tablename__ = 'price_archive'
    id = Column(Integer, primary_key=True)
    instrument_id = Column(Integer, ForeignKey('market_instruments.id'), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    instrument = relationship("MarketInstrument", back_populates="price_archive")

class TradeIdea(Base):
    __tablename__ = 'trade_ideas'
    id = Column(Integer, primary_key=True)
    instrument_id = Column(Integer, ForeignKey('market_instruments.id'), nullable=False)
    idea = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    instrument = relationship("MarketInstrument", back_populates="trade_ideas")

class TradeIdeaStatus(Base):
    __tablename__ = 'trade_idea_statuses'
    id = Column(Integer, primary_key=True)
    trade_idea_id = Column(Integer, ForeignKey('trade_ideas.id'), nullable=False)
    status = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    trade_idea = relationship("TradeIdea", back_populates="statuses")

MarketInstrument.latest_price = relationship("LatestPrice", uselist=False, back_populates="instrument")
MarketInstrument.price_archive = relationship("PriceArchive", back_populates="instrument")
MarketInstrument.trade_ideas = relationship("TradeIdea", back_populates="instrument")
TradeIdea.statuses = relationship("TradeIdeaStatus", back_populates="trade_idea")
