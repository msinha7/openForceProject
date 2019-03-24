from openforce_app.models import ratings


def getRatingsDB(quote, uname, session):
    ratingsRow = ratings.objects.all().filter(quote=quote)
    avgrate = 0
    for r in ratingsRow:
        avgrate += r.rating

    avgrate /= len(ratingsRow)
    isRated = False

    isRatedList = ratings.objects.all().filter(quote=quote, username=uname, session=session)
    if not isRatedList:
        isRated = True

    return (avgrate, isRated)
