def calculate_love_score(name_1, name_2):
  
    
    check_name =  (name_1 + name_2).lower().strip()
    
    num_true = 0
    num_love = 0
    
    for char in "true":
        if char in name_1:
            num_true+=1

     
    for char in "love":
        if char in name_1:
            num_true+=1
            
    
    
    
    
calculate_love_score("Kanye West", "Kim Kardashian")