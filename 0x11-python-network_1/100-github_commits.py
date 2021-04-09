#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[2]
    repo_name = sys.argv[1]
    url = "https://api.github.com/repos/" + username + '/' + repo_name + '/commits'
    r = requests.get(url)
    Dict = r.json()
    new_dict = {}
    for commit in Dict:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        date = commit['commit']['author']['date']
        new_dict[date] = [sha, author_name]
    dictionary_items = new_dict.items()
    sorted_dict = sorted(dictionary_items, reverse=True)
    i = 0
    for elem in sorted_dict:
        print("{}: {}".format(elem[1][0], elem[1][1]))
        i += 1
        if i == 10:
            break
