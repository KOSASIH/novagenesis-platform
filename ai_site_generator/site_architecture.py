import json
import nltk
from nltk.tokenize import word_tokenize

# Define a function to generate site architecture
def generate_site_architecture(user_input):
    # Tokenize user input
    tokens = word_tokenize(user_input)

    # Extract keywords and entities from user input
    keywords = [token for token in tokens if token.isalpha()]
    entities = [token for token in tokens if token.startswith('@')]

    # Generate site architecture based on keywords and entities
    site_architecture = {
        'layout': 'esponsive',
        'pages': []
    }

    for keyword in keywords:
        if keyword == 'blog':
            site_architecture['pages'].append({'type': 'blog', 'title': 'Blog'})
        elif keyword == 'portfolio':
            site_architecture['pages'].append({'type': 'portfolio', 'title': 'Portfolio'})

    for entity in entities:
        if entity == '@contact':
            site_architecture['pages'].append({'type': 'contact', 'title': 'Contact'})

    return site_architecture

# Test the function
user_input = "I want a website with a blog, portfolio, and contact page."
site_architecture = generate_site_architecture(user_input)
print(json.dumps(site_architecture, indent=4))
