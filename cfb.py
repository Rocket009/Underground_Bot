import cfbd
from private.config import CFBToken
from datetime import datetime


class cfb_api:

    def __init__(self):
        
        self.configuraion = cfbd.Configuration()
        self.configuraion.api_key['Authorization'] = CFBToken
        self.configuraion.api_key_prefix['Authorization'] = 'Bearer'
        self.currentyear = datetime.now().year

    def get_rankings(self) -> list:
        api_instance = cfbd.RankingsApi(cfbd.ApiClient(self.configuraion))
        rankings = api_instance.get_rankings(self.currentyear)
        rankss = rankings[len(rankings) - 1].polls[0]
        ranks = []
        for schools in rankss.ranks:
            ranks.insert(int(schools.rank), schools.school) 
        return ranks

    def get_ranking_week_ranks(self) -> list[cfbd.RankingWeekRanks]:
        api_instance = cfbd.RankingsApi(cfbd.ApiClient(self.configuraion))
        rankings = api_instance.get_rankings(self.currentyear)
        rankss = rankings[len(rankings) - 1].polls[0]
        return rankss.ranks

    def check_rank(self, team : str, ranks : list[cfbd.RankingWeekRanks]) -> bool:
        for rank in ranks:
            if rank.school == team:
                return True
        return False

    def get_rank(self, team : str, ranks : list[cfbd.RankingWeekRanks]) -> int:
        if not self.check_rank(team, ranks):
            return None
        for schools in ranks:
            if schools.school.lower() == team.lower():
                return int(schools.rank)

    def getcurrentweek(self) -> int:
        api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration=self.configuraion))
        calenderlist = api_instance.get_calendar(self.currentyear)
        for week in calenderlist:
            firstgame = week.last_game_start
            firstgamed = firstgame[:firstgame.find("T")]
            datef = datetime.strptime(firstgamed, '%Y-%m-%d')
            if (datetime.now() <= datef) and ((datef - datetime.now()).days <= 7):
                return week.week

    def getgoodgames(self) -> list[str]:
        api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration=self.configuraion))
        games = api_instance.get_games(self.currentyear, week=self.getcurrentweek())
        goodgames = []
        ranks = self.get_ranking_week_ranks()
        for game in games:
            if self.check_rank(game.home_team, ranks):
                if self.check_rank(game.away_team, ranks):
                    goodgames.append(f"#{self.get_rank(game.away_team, ranks)} {game.away_team} at #{self.get_rank(game.home_team, ranks)} {game.home_team}")
        return goodgames

    def searchgame(self, team : str) -> str:
        api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration=self.configuraion))
        games = api_instance.get_games(self.currentyear, week=self.getcurrentweek())
        for game in games:
            if game.home_team.lower() == team.lower():
                return f"{game.home_team} plays {game.away_team} at home"
            elif game.away_team.lower() == team.lower():
                return f"{game.away_team} plays {game.home_team} away"
        return f"{team} does not play this week or does not exist"


def main():
    cfb_obj = cfb_api()
    print(cfb_obj.getgoodgames())
if __name__ == "__main__":
    main()