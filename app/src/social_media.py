import praw


def reddit_comments(username: str, limit: int = 50) -> list[str]:
    """
    Gets comments of reddit user for analysis

    username: reddit username (does not include /u/)
    limit: max number of comments to scrape (default 50)
    returns: list of comments as strings for analysis
    """
    reddit = praw.Reddit("isitabot")
    comments = reddit.redditor(username).comments.new(limit=limit)
    return [comment.body for comment in comments]
