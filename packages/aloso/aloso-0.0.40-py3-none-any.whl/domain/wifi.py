import logging
from dataclasses import dataclass

import config
from domain.equipment_management import Equipments

logging.basicConfig(level=config.debug_level,
                    format='%(asctime)s %(levelname)s %(pathname)s %(funcName)s %(lineno)d : %(message)s',
                    datefmt='%d/%m/%Y %H:%M:%S',
                    filename=config.logs_file_path,
                    filemode='a')


@dataclass
class Wifi:
    id: int = None
    equipments: Equipments = None
    building: str = ""

    @staticmethod
    def equipment_to_dict(equipment: Equipments) -> dict:
        pass

    def create_building(self):
        pass

    def delete_building(self):
        pass

    def update_building(self):
        pass

    @staticmethod
    def get_building_by_name(name: str):
        pass

    @staticmethod
    def get_building_by_id(b_id: int):
        pass

    @staticmethod
    def get_buildings():
        pass

    def link_equipment_to_building(self, equipment: Equipments):
        pass

    def unlink_equipment_from_building(self, equipment: Equipments):
        pass

    def execute(self, *args):
        pass
