#!usr/bin/python3

import requests
import json
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        posts_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]
        
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
        print("Posts saved to posts.csv")
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")