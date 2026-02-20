import re

class StartHelper :
    url_prefix_reg = r"(https://)?(www.)?start.gg/"
    event_name_reg = r"(?P<name>tournament/.+/event/[a-zA-Z0-9_-]+)(/(overview|brackets|standings|matches|stats)?)?"

    slug_reg = r"[0-9a-zA-Z]+"
    
    @staticmethod
    def strip_event_name(url: str) -> str :
        re_res = re.search(StartHelper.event_name_reg, url)
        if not re_res:
            raise ValueError(f"Could not find event name in the provided url: {url}")
        
        slug = re_res.group("name")
        return slug