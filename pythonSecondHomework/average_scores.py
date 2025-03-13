def compute_average_scores(scores):  
    num_students = len(scores[0])  
    average_scores = []  
    for i in range(num_students):  
        total_score = 0  
        for subject_scores in scores:  
            total_score += subject_scores[i]  
        average_score = total_score / len(scores)  
        average_scores.append(round(average_score, 1))  
    return average_scores  

if __name__ == '__main__':  
    N, X = map(int, input().split())  
    scores = []  
    for _ in range(X):  
        subject_scores = tuple(map(float, input().split()))  
        scores.append(subject_scores)  

    average_scores = compute_average_scores(scores)  
    for score in average_scores:  
        print(score)  