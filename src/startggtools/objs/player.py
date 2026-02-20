class Player:
    id: str
    name: str
    prefix: str | None
    discordName: str | None
    pronouns: str | None

    def __init__(self, id: str, name: str, prefix: str | None, discordName: str | None, pronouns: str | None ):
        self.id = id
        self.name = name
        self.prefix = prefix
        self.discordName = discordName
        self.pronouns = pronouns

    @classmethod
    def from_entrant_query(cls, query_res: dict) -> 'Player':
        # TODO: will break if multiple participants to an entrant, currently
        #entrant_id = query_res['id']

        part_info = query_res['participants']
        if(len(part_info) > 1) :
            raise NotImplementedError("Cannot currently handle team tournaments!")
        
        part_info = part_info[0]
        player_id = str(part_info['id'])
        name = part_info['gamerTag']

        prefix = part_info['prefix']

        connection_info = part_info['requiredConnections']
        discord_name = None
        for auth in connection_info:
            if auth['type'] == "DISCORD":
                discord_name = auth['externalUsername']

        user_info = part_info['user']
        pronouns = user_info['genderPronoun']

        return Player(id = player_id, name = name, prefix = prefix, discordName = discord_name, pronouns = pronouns)