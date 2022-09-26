import cfbd
from private.config import CFBToken



class cfb_api:

    def __init__(self):
        
        self.configuraion = cfbd.Configuration()
        self.configuraion.api_key['Authorization'] = CFBToken
        self.configuraion.api_key_prefix['Authorization'] = 'Bearer'

    def get_rankings(self) -> list:
        api_instance = cfbd.RankingsApi(cfbd.ApiClient(self.configuraion))
        rankings = api_instance.get_rankings(2022)
        rankss = rankings[len(rankings) - 1].polls[0]
        ranks = []
        for schools in rankss.ranks:
            ranks.insert(int(schools.rank), schools.school) 
        return ranks


def main():
    cfb_obj = cfb_api()
    ranks = cfb_obj.get_rankings()[0].polls[0]
    print(len(ranks.ranks))

if __name__ == "__main__":
    main()