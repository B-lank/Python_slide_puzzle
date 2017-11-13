def get_rank(user_id):
    f = open('slidepuzzle.txt', 'r')
    if user_id in 'slidepuzzle.txt':
        rank = set_rank()
        highest_score = f.user_id
        return rank, highest_score

    else:
        rank = 0
        highest_score = 0
        return rank, highest_score
    f.close()
def set_rank(user_id, highest_score):
    f = open("slidepuzzle.txt", 'r')
    if user_id in f.slidepuzzle.txt:
        highest_score = highest_score.replce( )
        rank = f.rank.replace()

    else:
        user_id = "%d" %user_id
        f.write(user_id)
        highest_score = "%d점" %highest_score
        f.write(highest_score)
    f.close()
