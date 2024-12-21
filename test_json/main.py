import json

print('ProfileState.json')
with open("ProfileState.json", "r", encoding='utf-8-sig') as read_file: 
    data = json.load(read_file)

for i, league in enumerate(data['ServerState']['MatchHistory']['HistoryPerLeague']):
    print(f'{i}-лига:')
    print('    число игр:', league['NumberOfGamesPlayed'])
    print('    винрейт:', league['RecentWinRate'])
    print('    AVG-cubes:', league['RecentCubeEarnRate'])

# print(data['ServerState']['MatchHistory']['HistoryPerLeague'])


print()
print('GameState.json')
with open("GameState(3).json", "r", encoding='utf-8-sig') as read_file: 
    data = json.load(read_file)

for key, item in data['RemoteGame']['GameState'].items():
    print(key)

print()
print('my deck:')
for card in data['RemoteGame']['GameState']['ClientResultMessage']['GameResultAccountItems'][1]['Deck']['Cards']:
    print('    ', card['CardDefId'])

print()
print('DrawnCards:')
for card in data['RemoteGame']['GameState']['ClientResultMessage']['GameResultAccountItems'][1]['CardDefIdsDrawn']:
    print('    ', card)

print()
print('PlayedCards:')
for card in data['RemoteGame']['GameState']['ClientResultMessage']['GameResultAccountItems'][1]['CardDefIdsPlayed']:
    print('    ', card)
# print(data['RemoteGame']['GameState'])

print()
print('locations:')
for loc, res in zip(data['RemoteGame']['GameState']['ClientResultMessage']['LocationDefIdsAtEndOfGame'], data['RemoteGame']['GameState']['ClientResultMessage']['GameResultAccountItems'][1]['LocationResults']):
    try:
        print('    ', loc, res['PowerPlayed'])
    except:
        print('    ', loc)

