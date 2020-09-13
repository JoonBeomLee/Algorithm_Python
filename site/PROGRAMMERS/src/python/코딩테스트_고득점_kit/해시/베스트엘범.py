from collections import defaultdict

def solution(genres, plays):
    answer = []
    genres_plays = defaultdict(int)
    genres_songs = defaultdict(lambda: [])
    
    generes_index = 0
    for genre, play in zip(genres, plays):
        genres_plays[genre] += play
        genres_songs[genre].append((generes_index, play)) 
        generes_index += 1
        
    sorted_genres = sorted(genres_plays.items(), key=(lambda x: x[1]), reverse = True)
    
    for genre in sorted_genres: 
        sorted_g = sorted(genres_songs[genre[0]], key=(lambda x: x[1]), reverse=True) 
        answer.append(sorted_g[0][0]) 
        
        if len(sorted_g) > 1: 
            answer.append(sorted_g[1][0]) 
            
    return answer
