print("WORD FREQUENCY COUNTER")
print('\n')
def frequency(text):
    words=text.lower().split()
    freq={}
    for word in words:
        word=word.strip('.,!?()')
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

text=input("Enter a paragraph of text:")
result=frequency(text)
for word,count in result.items():
    print(f"{word}:{count}")