import google.generativeai as genai
import json
from dotenv import load_dotenv
import os
import praw

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

def get_posts():
    # Set up your PRAW credentials
    reddit_client_id = os.environ.get('reddit_client_id')
    reddit_client_secret = os.environ.get('reddit_client_secret')
    reddit_user_agent = os.environ.get('reddit_user_agent')

    # Create a Reddit instance
    reddit = praw.Reddit(
        client_id=reddit_client_id,
        client_secret=reddit_client_secret,
        user_agent=reddit_user_agent
    )

    # Specify the subreddit you want to retrieve posts from
    subreddit_name = 'AskDocs'

    # Get the subreddit instance
    subreddit = reddit.subreddit(subreddit_name)

    # Fetch the latest posts from the subreddit
    latest_posts = subreddit.new(limit=20)  # Adjust the limit based on your needs
    
    post_content_list = []
    for post in latest_posts:
        # Extract relevant post information
        post_info = {
            'id': post.id,
            'title': post.title,
            'selftext': post.selftext,
            'author': post.author.name,
            'created_utc': post.created_utc,
        }

        post_content_list.append(post_info)
        
    return post_content_list


def get_results():
    posts = get_posts()

    gemini_api_key = os.environ.get('gemini_api_key')
    genai.configure(api_key=gemini_api_key)

    model = genai.GenerativeModel('gemini-pro')

    results = list()

    for post_info in posts:
        post = f"{post_info['title']}\n\n{post_info['selftext']}"
        inquiry = f"""
        Instructions: Create an output of entities from this medical inquiry text. The entities should be a possible diagnosis, drugs, symptoms, age and gender if available. 
        
        Details: Keep only short first letter uppercase names as information and make the entities as generic as possible. Gender options are "Male" and "Female".

        Make sure to create a most probable generalized diagnosis, it does not have to medically correct, this is not for real world use. 
        For example, a list of diagnoses like Ovulation Pain, Menstrual Irregularity, Heavy Menstrual Bleeding, Gastrointestinal Distress should be a single diagnosis "Menstrual Health Issues".
        
        Output format should be JSON with no additional context or description.
        Keys for JSON: diagnosis, drugs, symptoms, age and gender.

        Inquiry:

        {post}
        """

        response = model.generate_content(inquiry)

        try:
            # Check if 'parts' is present in the response
            if response.parts:
                # If 'parts' exist, use the first one (single candidate) for JSON parsing
                result_json = json.loads(response.parts[0].text.replace("```", "").replace("JSON", "").replace("json", ""))
                
                # Check if 'diagnosis' is not empty
                if result_json['diagnosis'] and result_json['drugs']:
                    # Add post-related information to the result
                    result_json['post_info'] = post_info
                    results.append(result_json)
            else:
                # Handle the case where 'parts' is not present
                print("No parts in the response. Check the prompt_feedback.")
        except ValueError as e:
            # Handle JSON parsing error
            print(f"Error parsing JSON: {e}")

    return results

if __name__ == "__main__":
    print(get_results())
