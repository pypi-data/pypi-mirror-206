import logging
from typing import Optional

from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker

import config
from domain.equipment_management import Equipments
from domain.wifi import Wifi
from output.database.database_base import Base, engine
from output.shell.shell import Shell


class WifiData(Base, Wifi):
    __tablename__ = "Wifi"

    id = Column(Integer, primary_key=True)
    building = Column(String(50))
    equipment = Column(JSON)

    def __init__(self, *args, **kwargs):
        if "equipment" in kwargs and isinstance(kwargs["equipment"], Equipments):
            kwargs["equipment"] = self.equipment_to_dict(kwargs["equipment"])
        super().__init__(*args, **kwargs)

    @staticmethod
    # Ok
    def equipment_to_dict(equipment: Equipments) -> dict:
        return {
            "name": equipment.name,
            "ip": equipment.ip,
            "mac": equipment.mac,
            "equipment_type": equipment.equipment_type.__dict__,
            "equipment_dict": equipment.equipment_dict,
            "version": equipment.version,
        }

    # Ok
    def create_building(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.add(self)
                session.commit()
                logging.info("Bâtiment ajouté dans la base de données")
        except Exception as e:
            logging.error(e)

    # Ok
    def delete_building(self):
        try:
            with sessionmaker(bind=engine)() as session:
                session.query(WifiData).filter(WifiData.id == self.id).delete()
                session.commit()
                logging.info("Bâtiment supprimé de la base de données")
        except Exception as e:
            logging.error(e)

    # Ok
    def update_building(self):
        try:
            assert self.id is not None
            with sessionmaker(bind=engine)() as session:
                session.query(WifiData).filter(WifiData.id == self.id).update({
                    WifiData.building: self.building,
                    WifiData.equipment: self.equipment
                })
                session.commit()
                logging.info(f"Bâtiment {self} mis à jour dans la base de données")
        except AssertionError:
            logging.error("Impossible de mettre à jour le bâtiment : id non renseigné")

    @staticmethod
    # Ok
    def get_building_by_name(name: str):
        try:
            with sessionmaker(bind=engine)() as session:
                return session.query(WifiData).filter(WifiData.building == name).first()
        except Exception as e:
            logging.error(e)
            return None

    @staticmethod
    # Ok
    def get_building_by_id(b_id: int):
        try:
            with sessionmaker(bind=engine)() as session:
                return session.query(WifiData).filter(WifiData.id == b_id).first()
        except Exception as e:
            logging.error(e)
            return None

    @staticmethod
    # Ok
    def get_buildings() -> Optional[dict]:

        # try:
        #     with sessionmaker(bind=engine)() as session:
        #         data = session.query(WifiData).all()
        #         json_all_buildings = {}
        #
        #         for building in data:
        #             json_all_buildings[building.id] = {
        #                 "id": building.id,
        #                 "name": building.building,
        #                 "equipment": building.equipment
        #             }
        #         return json_all_buildings
        # except Exception as e:
        #     logging.error(e)
        #     return None

        buildings_list = [{"name": "Batiment 1", "state": False},
                          {"name": "Batiment 2", "state": True},
                          {"name": "Batiment 3", "state": True},
                          {"name": "Batiment 4", "state": False},
                          {"name": "Batiment 5", "state": True},
                          {"name": "Batiment 6", "state": False},
                          {"name": "Batiment 7", "state": True},
                          {"name": "Batiment 8", "state": False},
                          {"name": "Batiment 9", "state": True},
                          {"name": "Batiment 10", "state": False},
                          {"name": "Batiment 11", "state": True},
                          {"name": "Batiment 12", "state": False}]

        return buildings_list

    # Ok
    def link_equipment_to_building(self, equipment: Equipments):
        try:
            assert self.id is not None
            building = WifiData.get_building_by_id(self.id)
            building.equipment = self.equipment_to_dict(equipment)
            building.update_building()
        except AssertionError:
            logging.error(f"Impossible de lier l'équipement {equipment} au bâtiment {self}: id non renseigné")

    # Ok
    def unlink_equipment_from_building(self):
        try:
            assert self.id is not None
            building = WifiData.get_building_by_id(self.id)
            building.equipment = None
            building.update_building()
        except AssertionError:
            logging.error(f"Impossible de dissocier l'équipement du bâtiment {self}: id non renseigné")

    # Ok
    def execute(self, *args):
        conn = Shell.ssh_connection(host=self.equipment.ip,
                                    username=config.ssh_equipment_username,
                                    password=config.ssh_equipment_password,
                                    port=config.ssh_equipment_port)

        cmd = "energywise query importance 75 name set level 10" if args[0] is None else args[0]

        try:
            with conn:
                conn.run(cmd)
            print(f"Commande {cmd} executé avec succès")
        except Exception as e:
            print(f"Erreur d'execution de la commande : {e}")


if __name__ == '__main__':
    eq = Equipments(ip="168", name="New")
    bld = WifiData(id=1)
    bld.link_equipment_to_building(eq)
    # bld.unlink_equipment_from_building()
