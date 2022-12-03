import requests
import json


JSON_FILE_NAME = "test.json" #change file name here

if __name__ == "__main__":
    res = requests.get("https://statsapi.mlb.com/api/v1/teams/112?hydrate=previousSchedule(date=2018-03-07,season=2018,limit=100,gameType=[E,S,R,A,F,D,L,W],team,linescore(matchup,runners),flags,review,decisions,person,stats,game(content(summary,media(epg)),tickets),seriesStatus(useOverride=true)),nextSchedule(date=2018-03-07,season=2018,limit=200,gameType=[E,S,R,A,F,D,L,W],team,linescore(matchup,runners),flags,review,decisions,person,stats,game(content(summary,media(epg)),tickets),seriesStatus(useOverride=true))&language=en%22")

    with open(JSON_FILE_NAME, "w") as f:
        data = res.json()
        f.write(json.dumps(data))
        

    # print(res.json()["teams"][0].keys())