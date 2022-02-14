def main():
    infile = open('WorldSeriesWinners.txt', 'r') #read the Al.txt file object assigned to infile variable
    
    world_series_won = {} # Dict using team names as keys, and number of years won as value {team_name : num_yrs_won}
    years_won = {} # Dict using World Series year as key, the team that won that year as the value
    count = 1903
    for team in infile: # Each line represents a team name that won the world series starting in 1903
        #***years_won logic***
        # Take the current year, and use that as a key with the team that won that year as the value
        if count == 1994 or count == 1904:
            count += 1
        years_won[count] = team.strip()
        count += 1

        #***world_series_won logic***
        if world_series_won.get(team.strip()): #if team is a key in the dictionary, incriment key's value
            world_series_won[team.strip()] += 1
        else: #if the team is not a key in the dictionary, create a key for that string and set its value to 1
            world_series_won[team.strip()] = 1
    


    infile.close()

    #prompt user to input a year for the world sieries from 1903 to 2009
    input_year = int(input('Enter World Series Year: '))
    print('World Series champion:', years_won.get(input_year) )
    print('Number of World Series won:', world_series_won.get(years_won.get(input_year)) )
    

    # I am using THIS dict, with the KEY xxxx, to get this TYPE of value

main()