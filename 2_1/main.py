from enum import Enum


class Play(str, Enum):
    Rock = "A"
    Paper = "B"
    Scissors = "C"


class Response(str, Enum):
    Rock = "X"
    Paper = "Y"
    Scissors = "Z"


response_score_map = {
    Response.Rock: 1,
    Response.Paper: 2,
    Response.Scissors: 3,
}


class Outcome(int, Enum):
    Loss = 0
    Draw = 3
    Win = 6


def get_outcome(play, response):
    if any((
        play == Play.Rock and response == Response.Paper,
        play == Play.Scissors and response == Response.Rock,
        play == Play.Paper and response == Response.Scissors,

    )):
        return Outcome.Win

    if any((
        play == Play.Rock and response == Response.Rock,
        play == Play.Paper and response == Response.Paper,
        play == Play.Scissors and response == Response.Scissors,
    )):
        return Outcome.Draw

    return Outcome.Loss


if __name__ == '__main__':
    with open("input") as f:
        encrypted_strategy_guide = f.read().splitlines()

    score = 0

    for x in encrypted_strategy_guide:
        _play, _response = x.split()

        # Map value to enums
        play = Play(_play)
        response = Response(_response)
        outcome = get_outcome(play, response)

        # Add points for play
        score += response_score_map[response]

        # Add points for outcome
        score += outcome.value

    print(score)
