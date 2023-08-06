import logging

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship

from domain.equipments_group import EquipmentsGroup
from output.database.database_base import Base, engine


class EquipmentsGroupData(Base, EquipmentsGroup):
    __tablename__ = "EquipmentsGroup"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    equipment = relationship("EquipmentsData", back_populates="group", cascade="all, delete-orphan")

    @staticmethod
    def get_group_equipment_by_id(id_group):
        try:
            with sessionmaker(bind=engine)() as session:
                return session.query(EquipmentsGroupData).filter(EquipmentsGroupData.id == id_group).first()
        except Exception as e:
            logging.error(e)

    def create(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.add(self)
                session.commit()
                logging.info("Equipment Group database : create : ok")
        except Exception as e:
            logging.error(e)

    def update(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.merge(self)
                session.commit()
                logging.info("Equipment Group database : update : ok")
        except Exception as e:
            logging.error(e)

    def delete(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.delete(self.get_group_equipment_by_id(self.id))
                session.commit()
                logging.info("Equipment Group database : delete : ok")
        except Exception as e:
            logging.error(e)

