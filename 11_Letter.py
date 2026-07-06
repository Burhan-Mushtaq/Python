letter = ''' 
    Dear <|Name|>, 
    You are selected! 
    <|Date|> '''

print(letter.replace("<|Name|>", "Burhan").replace("<|Date|>" , "06 July 2026"))