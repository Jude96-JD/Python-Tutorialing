# Write a program to fill in the letter template given below with name and date

# letter = '''
#       Dear <|Name|>,
#       You are selected!
#       <|Date|>
#           '''


letter = '''Dear <|Name|>,
        You are selected!
        <|Date|> '''

print(letter.replace("<|Name|>", "Jude").replace("<|Date|>", "7th February, 2026"))