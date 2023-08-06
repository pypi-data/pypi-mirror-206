from sqlalchemy import Column, Integer, String, ForeignKey
import logging

from sqlalchemy.orm import sessionmaker, relationship

from domain.equipment_management import Equipments
from output.database.database_base import Base, engine
from output.models.equipments_group_database import EquipmentsGroupData


class EquipmentsData(Base, Equipments):
    __tablename__ = "Equipments"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    ip = Column(String(50))
    version = Column(String(50), default='V1.0')
    id_group = Column(Integer, ForeignKey('EquipmentsGroup.id', ondelete='CASCADE'))
    group = relationship("EquipmentsGroupData", back_populates="equipment")

    @staticmethod
    def get_all():
        try:
            with sessionmaker(bind=engine)() as session:
                data_groups = session.query(EquipmentsGroupData).all()
                data_equipments = session.query(EquipmentsData).all()
                json_all_equipments = []
                json_all_groups = {}

                for group in data_groups:
                    for equipment in data_equipments:
                        if equipment.id_group == group.id:
                            my_equipment = {
                                "name": equipment.name,
                                "ip": equipment.ip,
                                "version": equipment.version,
                                "id_group": equipment.id_group,
                            }
                            json_all_equipments.append(my_equipment)
                    json_all_groups[group.name] = json_all_equipments
                    json_all_equipments = []

                return json_all_groups
        except Exception as e:
            logging.error(e)

    @staticmethod
    def get_equipment_by_id(id_equipment):
        try:
            with sessionmaker(bind=engine)() as session:
                return session.query(EquipmentsData).filter(EquipmentsData.id == id_equipment).first()
        except Exception as e:
            logging.error(e)

    @staticmethod
    def get_equipments_by_group_id(id_group):
        try:
            with sessionmaker(bind=engine)() as session:
                return session.query(EquipmentsData).filter(EquipmentsData.id_group == id_group).all()
        except Exception as e:
            logging.error(e)

    def create(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.add(self)
                session.commit()
                logging.info("Equipment database : create : ok")
        except Exception as e:
            logging.error(e)

    def update(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.merge(self)
                session.commit()
                logging.info("Equipment database : update : ok")
        except Exception as e:
            logging.error(e)

    def delete(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.delete(self.get_equipment_by_id(self.id))
                session.commit()
                logging.info("Equipment database : delete : ok")
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    '''
    equipmentG1 = EquipmentsGroupData(name='Switchs')
    equipmentG2 = EquipmentsGroupData(name='Bornes')

    switch1 = EquipmentsData(name='switch1', ip='localhost', version='V1.0')
    switch2 = EquipmentsData(name='switch2', ip='localhost', version='V1.0')
    switch3 = EquipmentsData(name='switch3', ip='localhost', version='V1.0')
    borne1 = EquipmentsData(name='borne1', ip='235.45.78.93', version='V1.0')
    borne2 = EquipmentsData(name='borne2', ip='235.45.78.93', version='V1.0')
    borne3 = EquipmentsData(name='borne3', ip='235.45.78.93', version='V1.0')
    borne4 = EquipmentsData(name='borne4', ip='235.45.78.93', version='V1.0')
    borne5 = EquipmentsData(name='borne5', ip='235.45.78.93', version='V1.0')

    switch1.group = equipmentG1
    switch2.group = equipmentG1
    switch3.group = equipmentG1

    borne1.group = equipmentG2
    borne2.group = equipmentG2
    borne3.group = equipmentG2
    borne4.group = equipmentG2
    borne5.group = equipmentG2

    
    equipmentG1.create()
    switch1.create()
    switch2.create()
    switch3.create()
    borne1.create()
    borne2.create()
    borne3.create()
    borne4.create()
    borne5.create()
    equipmentG2.create()
    '''
    # print(EquipmentsData.get_all())
    # print(EquipmentsData.get_equipments_by_group_id(1))
    ...
