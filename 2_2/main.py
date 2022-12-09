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


class Outcome(str, Enum):
    Loss = "X"
    Draw = "Y"
    Win = "Z"


outcome_score_map = {
    Outcome.Loss: 0,
    Outcome.Draw: 3,
    Outcome.Win: 6,
}


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


def get_response_for_outcome(play, outcome):
    match play:
        case Play.Rock:
            match outcome:
                case Outcome.Win: return Response.Paper
                case Outcome.Draw: return Response.Rock
                case Outcome.Loss: return Response.Scissors
        case Play.Paper:
            match outcome:
                case Outcome.Win: return Response.Scissors
                case Outcome.Draw: return Response.Paper
                case Outcome.Loss: return Response.Rock

        case Play.Scissors:
            match outcome:
                case Outcome.Win: return Response.Rock
                case Outcome.Draw: return Response.Scissors
                case Outcome.Loss: return Response.Paper


if __name__ == '__main__':
    with open("input") as f:
        encrypted_strategy_guide = f.read().splitlines()

    score = 0

    for x in encrypted_strategy_guide:
        _play, _outcome = x.split()

        # Map value to enums
        play = Play(_play)
        outcome = Outcome(_outcome)

        response = get_response_for_outcome(play, outcome)

        # Add points for play
        score += response_score_map[response]

        # Add points for outcome
        score += outcome_score_map[outcome]

    print(score)
