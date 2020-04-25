import re

def get_words(source_text):
    
    tokens = re.findall(r"[a-zA-Z]+", source_text)
    tokens = [t.lower() for  t in tokens]
    tokens = list(set(tokens))

    return tokens
