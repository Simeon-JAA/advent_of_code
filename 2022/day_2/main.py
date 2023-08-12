"""Day 2 of advent of code 2022"""


def get_file() -> list[str]:
    """Formats the input to a list of all elves with calories"""
    with open('2022\day_2\input.txt', "r") as f:
        return f.read()


def determine_score(line: str) -> int:
    """Will return the outcome of the line"""
    
    line = line.upper()
    result = line.replace(' ','')
    score_for_choice = {"X": 1,
                        "Y": 2,
                        "Z": 3}
    draw = {'AX', 'BY', 'CZ'}
    win = {'AY', 'BZ', 'CX'}
    lose = {'AZ', 'BX', 'CY'}
    if result in lose:
        return 0 + score_for_choice[result[-1]]
    elif result in draw:
        return 3 + score_for_choice[result[-1]]
    else:
        return 6 + score_for_choice[result[-1]]


def determine_score_decrypted(line: str) -> int:
    """Will return the outcome of the line after it has been decrypted"""
    
    line = line.upper()
    result = line.replace(' ','')
    
    draw = ['AX', 'BY', 'CZ']
    win = ['AY', 'BZ', 'CX']
    lose = ['AZ', 'BX', 'CY']
    # Lose
    if result[-1] == "X":
        new_input = list(filter(lambda x: x[0] == result[0], lose))[0]
        return determine_score(new_input)
    if result[-1] == "Y":
        new_input = list(filter(lambda x: x[0] == result[0], draw))[0]
        return determine_score(new_input)
    if result[-1] == "Z":
        new_input = list(filter(lambda x: x[0] == result[0], win))[0]
        return determine_score(new_input)
        

if __name__ =="__main__":

    file = get_file().split("\n")

    total_score = 0
    total_score_encrypted = 0

    for match in file:
        total_score += determine_score(match)
        total_score_encrypted += determine_score_decrypted(match)
    
    
    print(total_score, total_score_encrypted)