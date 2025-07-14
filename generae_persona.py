import re
import praw
import json
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
from mistralai import Mistral

load_dotenv()
API_KEY = os.environ["MISTRAL_API_KEY"]
client = Mistral(api_key=API_KEY)

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def extract_username_from_url(url):
    parsed = urlparse(url)
    parts = parsed.path.strip("/").split("/")
    return parts[1] if len(parts) > 1 else None

def scrape_user_data(username, post_limit=30, comment_limit=30):
    user = reddit.redditor(username)
    posts, comments = [], []

    for submission in user.submissions.new(limit=post_limit):
        posts.append({
            "type": "post",
            "title": submission.title,
            "text": submission.selftext,
            "subreddit": str(submission.subreddit),
            "score": submission.score,
            "url": submission.url,
        })

    for comment in user.comments.new(limit=comment_limit):
        comments.append({
            "type": "comment",
            "text": comment.body,
            "subreddit": str(comment.subreddit),
            "score": comment.score,
            "url": f"https://www.reddit.com{comment.permalink}",
        })

    return posts + comments

def build_prompt(user_content):
    prompt = (
        "You are an expert in user research. Based on the following Reddit posts and comments, "
        "generate a structured User Persona. For each attribute (like Name, Age Estimate, Occupation Guess, etc.), "
        "cite the specific post or comment (quote it briefly) you used as evidence.\n\n"
        "USER DATA:\n"
    )
    for i, item in enumerate(user_content, start=1):
        if item["type"] == "post":
            prompt += f"\n[{i}] POST: {item['title']} - {item['text'][:200]} (r/{item['subreddit']})"
        else:
            prompt += f"\n[{i}] COMMENT: {item['text'][:250]} (r/{item['subreddit']})"
    return prompt

def generate_user_persona(prompt):
    model = "devstral-small-latest"
    
    chat_response = client.chat.complete(
            model=model,
            messages=[
                {"role": "system", "content": "You analyze Reddit profiles to create realistic user personas with citations."},
                {"role": "user", "content": prompt}
            ],
        )

    return chat_response.choices[0].message.content

def save_to_file(content, username):
    filename = f"{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"User persona saved to: {filename}")

def main():
    url = input("Enter Reddit profile URL: ").strip()
    username = extract_username_from_url(url)
    if not username:
        print("Invalid Reddit URL.")
        return

    print(f"Scraping data for user: {username} ...")
    user_data = scrape_user_data(username)
    if not user_data:
        print("No posts/comments found.")
        return

    prompt = build_prompt(user_data)
    persona = generate_user_persona(prompt)

    save_to_file(persona, username)

if __name__ == "__main__":
    main()