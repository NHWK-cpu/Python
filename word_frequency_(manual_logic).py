def count_word(text:str) -> dict:
    words: list[str] = text.split()
    _ : tuple = []
    counter: dict = {}
    for word in words:
        if word not in _:
            counter.update({word:0})
            _.append(word)
        counter[word] = counter[word] + 1
    
    return counter

def main() -> None:
    text: str = input('Input your text: ')
    counted: dict = count_word(text)
    
    for word,amount in counted.items():
        print(f'{word} : {amount}')

if __name__ == '__main__':
    main()