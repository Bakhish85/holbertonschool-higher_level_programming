#!/usr/bin/python3
"""
This module contains functions to fetch and process posts from JSONPlaceholder.

The JSONPlaceholder API provides a simple RESTful API for testing and prototyping. 
These functions interact with the /posts endpoint of the JSONPlaceholder API.

Functions:
    - fetch_and_print_posts: Fetches posts from JSONPlaceholder and prints their titles.
    - fetch_and_save_posts: Fetches posts from JSONPlaceholder and saves them to a CSV file.
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder and prints their titles.

    This function sends a GET request to JSONPlaceholder API to fetch posts.
    If the request is successful (status code 200), it prints the titles of all the fetched posts.

    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    # Print the status code
    print("Status Code:", response.status_code)

    # Check if the request was succesful
    if response.status_code == 200:
        #Parse the JSON data
        data = response.json()

        # Iterate through the posts and print titles:
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.

    This function sends a GET request to JSONPlaceholder API to fetch posts.
    If the request is successful (status code 200), it structures the data into a list of dictionaries,
    where each dictionary represents a post with keys 'id', 'title', and 'body'.
    It then writes this data into a CSV file named 'posts.csv'.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    #Check if the request was succesful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Define the field names for the CSV file
        fieldnames = ['id', 'title', 'body']

        # Open the CSV file in write mode and write the data.
        with open('posts.csv', "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the header row
            writer.writerheader()

            # Write each post as a row in the CSV file
            for post in data:
                writer.writerow({'id': post['id'], 'title': post['title'], 'body': post['body']})
