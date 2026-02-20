import argparse
from .objs import QueryManager, StartHelper, CSVManager

parser = argparse.ArgumentParser(add_help = False)
subparsers = parser.add_subparsers(help='subcommand help', dest='cmd')
parser.add_argument("--config", help="Config file location.")

fetch_players_parser = subparsers.add_parser('fetch-players', help = 'fetch-players help')
fetch_players_parser.add_argument('url', help = "Event URL")
fetch_players_parser.add_argument('outpath', help = "File to save output to")

def fetch_players(url: str, config_file, outpath) :
    qm = QueryManager(config_file)
    event_id = qm.get_event_id(StartHelper.strip_event_name(url))
    players = qm.get_event_players(event_id)
    CSVManager.save_players_to_file(players, outpath)

def main():
    print("Hello from startgg-player-fetch!")

def entry():
    args = parser.parse_args()

    if args.cmd == "fetch-players" :
        fetch_players(args.url, args.config, args.outpath)
    
    else :
        main()

if __name__ == "__main__":
    args = parser.parse_args()

    if args.cmd == "fetch-players" :
        fetch_players(args.url, args.config, args.outpath)
    
    else :
        main()
    