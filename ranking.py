def get_rank(user_id):
    rank = []
    count = 0
    who = False
    with open('rank.txt', mode='rt', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line: break
            count += 1
            rank.append(line)
    rank_id = []
    rank_score = []
    ranking = []
    for i in range(count):
        rank_id.append(rank[i].split('$')[0])
        rank_score.append(rank[i].split('$')[1])
        ranking.append(rank[i].split('$')[2].split('\n')[0])
    for i in range(count):
        if rank_id[i] == user_id:
            who = i+1
    if not who:
        return 0, 0
    return ranking[who-1], rank_score[who-1]


def set_rank(user_id, highest_score):
    rank = []
    count = 0
    with open('rank.txt', mode='rt', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line: break
            count += 1
            rank.append(line)
    rank_id = []
    rank_score = []
    is_user = False
    for i in range(count):
        rank_id.append(rank[i].split('$')[0])
        rank_score.append(int(rank[i].split('$')[1]))
    for i in range(count):
        if user_id == rank_id[i]:
            if rank_score[i] < highest_score:
                rank_score[i] = highest_score
            is_user = True
    if not is_user:
        rank_id.append(format(user_id))
        rank_score.append(highest_score)
        count += 1
    copy = []
    ranking = []
    for i in range(count):
        copy.append(rank_score[i])
    copy.sort(reverse=True)
    for i in range(count):
        ranking.append(rank_score.index(copy[i]))

    with open('rank.txt', mode='wt', encoding='utf-8') as file:
        count = 1
        for i in ranking:
            file.write("%s$%s$%s\n" % (rank_id[i], rank_score[i], count))
            count += 1