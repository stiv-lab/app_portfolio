# data/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class MarketInstrument(Base):
    __tablename__ = 'market_instruments'
    id = Column(Integer, primary_key=True)
    secid = Column(String, unique=True, nullable=False)  # Код ценной бумаги (тикер)
    shortname = Column(String)  # Краткое наименование инструмента
    regnumber = Column(String)  # Номер государственной регистрации инструмента
    name = Column(String, nullable=False)  # Полное наименование инструмента
    isin = Column(String)  # Международный идентификационный номер ценной бумаги (ISIN)
    is_traded = Column(Integer, nullable=False)  # Флаг, указывающий, торгуется ли инструмент
    type = Column(String)  # Тип инструмента
    group = Column(String)  # Группа, к которой принадлежит инструмент
    primary_boardid = Column(String)  # Основной идентификатор режима торгов
    marketprice_boardid = Column(String)  # Идентификатор режима торгов для рыночной цены
    market_type = Column(String, default=None)  # Тип рынка для запросов к iss

class LatestPrice(Base):
    __tablename__ = 'latest_prices'
    id = Column(Integer, primary_key=True)
    secid = Column(String, ForeignKey('market_instruments.secid'), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    instrument = relationship("MarketInstrument", back_populates="latest_price")

class PriceArchive(Base):
    __tablename__ = 'price_archive'
    id = Column(Integer, primary_key=True)
    secid = Column(String, ForeignKey('market_instruments.secid'), nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    instrument = relationship("MarketInstrument", back_populates="price_archive")

class TradeIdea(Base):
    __tablename__ = 'trade_ideas'
    id = Column(Integer, primary_key=True)
    secid = Column(String, ForeignKey('market_instruments.secid'), nullable=False)
    description = Column(String, nullable=False)  # Описание идеи
    open_time = Column(DateTime, nullable=False)  # Время открытия идеи
    status = Column(String, nullable=False)  # Статус идеи
    open_price = Column(Float, nullable=False)  # Цена открытия идеи
    target_price = Column(Float, nullable=False)  # Целевая цена
    stop_loss = Column(Float, nullable=False)  # Стоп лосс
    close_time = Column(DateTime, nullable=True)  # Время закрытия идеи
    close_price = Column(Float, nullable=True)  # Цена закрытия идеи
    comment = Column(String, nullable=True)  # Комментарий
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
