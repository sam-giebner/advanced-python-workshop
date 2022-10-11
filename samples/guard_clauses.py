"""
This is an example of how to reduce indentation levels
"""

# Too many indentation levels !
def probaly_not_disney_v1(movie_title):
    if movie_title:
        if 'STAR WARS' not in movie_title.upper():
            if 'TOY STORY' not in movie_title.upper():
                if 'PIRATES' not in movie_title.upper():
                    return True
    return False

def probaly_not_disney_v2(movie_title):
    
    # Guard clause
    if not movie_title:
        return False

    # Guard clause
    if ('STAR WARS' in movie_title.upper() 
        and 'TOY STORY' in movie_title.upper() 
        and 'PIRATES' in movie_title.upper()):
        return False

    return True

def probaly_not_disney_v3(movie_title):

    # Guard clause 
    if not movie_title:
        return False

    major_disney_titles = ['STAR WARS','TOY STORY','PIRATES']
    
    # List comprehension guard clause super combo
    if [title for title in major_disney_titles if title in movie_title.upper()]:
        return False
    
    return True