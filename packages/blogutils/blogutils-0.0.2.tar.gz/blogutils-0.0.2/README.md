# MyBlogUtils

MyBlogUtils is a Python package for managing blog content. It provides a set of utility functions for creating and managing blog posts, generating RSS feeds, and more.

## Installation

To install MyBlogUtils, use pip:

pip install myblogutils



## Usage

Here are some examples of how to use the functions provided by MyBlogUtils:



from myblogutils import create_post,read_file, write_file, generate_slug,send_email

# Example usage of write_file function
filename = 'example.txt'
contents = 'This is some example text.'
write_file(filename, contents)


# Create a new blog post

title = "This is a blogpost "
author = "Arvind Srivastav "
tags = ["Python", "Blogging","Blog"]
filename = create_post(title, author, tags)
print(f"New post created: {filename}")

Functions
Here are the functions provided by MyBlogUtils:

create_post-
create_post(title: str, author: str, tags: List[str]) -> str

# Example usage of generate_slug function
title = 'My First Blog Post'
slug = generate_slug(title)
print(slug)  
# prints 'my-first-blog-post'


# Example usage of send_email function
to = 'recipient@example.com'
subject = 'New blog post'
body = f'A new blog post "{slug}" was published on {now}!'
send_email(to, subject, body)