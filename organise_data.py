from mood_reader import analyse_mood

# organises the data and returns them in a list
def organise():
    # calls the mood data
    score = analyse_mood()
    dates = []
    positive = []
    negative = []

    # stores the values of the date, pos, and neg in a list for easier access
    for key, value in score.items():
        dates.append(key)
        positive.append(value['pos'])
        negative.append(value['neg'])

    return [dates, negative, positive]


if __name__ == "__main__":
    organise()