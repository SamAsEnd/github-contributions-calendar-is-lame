import random

# pip install gitpython
from git import Repo
from datetime import datetime, timedelta

today = datetime.today()
start = today.replace(year=2014, month=11, day=11)
repo = Repo('.')

delta_day = timedelta(days=1)
delta_sec = timedelta(seconds=10)

while start < today:
    commit = random.randint(0, 5)

    for c in range(commit):
        open('lorem ipsum.txt', 'w').write(start.ctime() + ' - ' + str(c))
        repo.git.add('lorem ipsum.txt')
        repo.git.commit(m=start.ctime() + ' commit - ' + str(c), date=start)
        start += delta_sec

    print('Commit for - ' + start.ctime())

    start += delta_day
