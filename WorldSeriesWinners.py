def main():
    infile = open('WorldSeriesWinners.txt', 'r') #read the Al.txt file object assigned to infile variable
    
    world_series_won = {}
    years_won = {}
    count = 1903
    for team in infile: # Each line represents a team name that won the world series starting in 1903
        #***years_won logic***
        # Take the current year, and use that as a key with the team that won that year as the value
        if count == 1994 or count == 1904:
            count += 1
        years_won[count] = team.strip()
        count += 1

        


        #***world_series_won logic***
        if world_series_won.get(team.strip()): #if team is a key in the dictionary, inriment key's value
            world_series_won[team.strip()] += 1
        else: #if the team is not a key in the dictionary, create a key for that string and set its value to 1
            world_series_won[team.strip()] = 1
    

    for i in years_won:
        print(i, ": ", years_won[i], sep='')
        # print(years_won[i])
    


    infile.close()

main()