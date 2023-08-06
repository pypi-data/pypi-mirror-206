import logging

import config
from domain.wifi import Wifi
from output.shell.shell import Shell


class WifiAnsible(Wifi):

    def execute(self, *args):
        conn = Shell.ssh_connection(host=config.ansible_host,
                                    username=config.ansible_username,
                                    password=config.ansible_password,
                                    port=config.ansible_port)
        inventory = args[0]
        playbook = args[1]
        self.building = args[2]

        cmd = f"ansible-playbook -i {inventory} {playbook} -e building='{self.building}'"

        try:
            with conn:
                conn.run(cmd)
            logging.info(f"Playbook {playbook} executé avec succès sur le batiment {self.building}")
        except Exception as e:
            logging.error(f"Erreur d'execution du playbook : {e} sur le batiment {self.building}")
