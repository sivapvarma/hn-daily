# Use HackerNews API to get top links
import requests, ast
import json

def top_items(n):
    # return top n items from hacker news currently
    # n has to be less than 500
    ts_url = 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty'
    resp = requests.get(ts_url)
    ts_ids = ast.literal_eval(resp.text.strip())
    top_stories = []
    for ts_id in ts_ids[:n]:
        ts_url = 'https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty'.format(ts_id)
        resp = requests.get(ts_url)
        top_stories.append(resp.text)
    return top_stories

def print_json_story(s):
    story = ast.literal_eval(s)
    print('Title: {}'.format(story['title']))
    print('URL: {}'.format(story['url']))

if __name__ == '__main__':
    for item in top_items(20):
        print_json_story(item)