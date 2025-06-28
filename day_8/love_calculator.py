def calculate_love_score(name_1, name_2):
    name = (name_1 + name_2).lower().replace(" ","")
    score_1 = 0
    score_2 = 0

    for char in name:
        if char == "t":
            score_1+=1
        elif char == 'r':
            score_1+=1
        elif char == 'u':
            score_1+=1
        elif char == 'e':
            score_1+=1
            score_2+=1
        elif char == 'l':
            score_2+=1
        elif char == 'o':
            score_2+=1
        elif char == 'v':
            score_2+=1
        else:
            continue
    
    print(f"{score_1}{score_2}")
            
    
    
calculate_love_score("Kanye West", "Kim Kardashian")