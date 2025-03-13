
def find_second_highest_scorers():  

    n = int(input())  
    records = []  


    for _ in range(n):  
        name = input()  
        score = float(input())  
        records.append([name, score])  

    scores = sorted(set([score for name, score in records]))  


    if len(scores) < 2:  
        return  

    second_highest_score = scores[-2]  


    second_highest_scorers = [name for name, score in records if score == second_highest_score]  


    second_highest_scorers.sort()  


    for name in second_highest_scorers:  
        print(name)  


find_second_highest_scorers()  