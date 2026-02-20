from .player import Player
from typing import Dict

class CSVManager:

    @staticmethod
    def save_players_to_file(players: Dict[str, Player], outpath: str):
        with open(outpath, 'w') as f:
            for _,p in players.items():
                prefix = f"\"{p.prefix}\""
                pronouns = f"\"{p.pronouns}\""
                discordname = f"\"{p.discordName}\""
                f.write(f"\"{p.name}\",{prefix if p.prefix else ''},{discordname if p.discordName else ''},{pronouns if p.pronouns else ''}\n")
        