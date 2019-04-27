import csv

splitted_lines = []

with open('Stod_001_Reykjavik.ManMedal.txt') as f:
    for line in f:
        splitted_lines.append(line.split())

f.close()

with open('reykjavik_man_medal.csv', "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(splitted_lines)
