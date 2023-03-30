from nltk.sentiment import SentimentIntensityAnalyzer
from glob import glob
from os.path import split


def analyse_mood():
    # iterates through all the diaries in the file
    folders = sorted(glob("diary/*.txt"))

    # stores all the data about diary mood
    score = {}

    # goes through all files and analyse their mood
    for folder in folders:
        file_name = split(folder)
        file_name = file_name[1].split(".")
        with open(folder, "r") as file:
            diary = file.read()
        analyser = SentimentIntensityAnalyzer()
        score[file_name[0]] = analyser.polarity_scores(diary)

    return score


if __name__ == "__main__":
    analyse_mood()
