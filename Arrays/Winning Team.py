if __name__ == '__main__':
    # O(n) time, O(k) where k is the number of teams
    def tournamentWinner(competitions, results):
        # Write your code here.
        def updateDict(team, winnerTeam, winPoints, dict):
            print(team, winnerTeam, winPoints, dict)
            dict[team] += 1
            if dict[team] > winPoints:
                winnerTeam = team
                winPoints += 1
            print(team, winnerTeam, winPoints, dict)
            return winnerTeam, winPoints

        dict = {}
        for x in competitions:
            dict[x[0]] = 0
            dict[x[1]] = 0
        winnerTeam = ""
        winPoints = 0

        for x in range(len(competitions)):
            arr = competitions[x]
            result = results[x]
            if result == 0:
                # away won
                winnerTeam, winPoints = updateDict(arr[1], winnerTeam, winPoints, dict)
            # dict[arr[1]] += 1
            # if dict[arr[1]] > winPoints:
            # 	winnerTeam = arr[1]
            # 	winPoints += 1
            else:
                winnerTeam, winPoints = updateDict(arr[0], winnerTeam, winPoints, dict)
            # dict[arr[0]] += 1
            # if dict[arr[0]] > winPoints:
            # 	winnerTeam = arr[0]
            # 	winPoints += 1
        return winnerTeam

    print(tournamentWinner([
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ], [0, 0, 1]))