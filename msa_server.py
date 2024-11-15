# Josquin Larsen
# 8/nov/2024
# A8 - Microservice A - Wikipedia Search

import zmq
import wikipediaapi

# WikipediaAPI calls taken from https://pypi.org/project/Wikipedia-API/
# ZMQ layout based on Luis Flores' Introduction to ZeroMQ (CS361 OSU)

wiki_wiki = wikipediaapi.Wikipedia('Microservice A', 'en')


def get_wikipedia_page(artist_name):
    """
    Searches Wikipedia for artist's name
    If found, returns page,
    otherwise returns error message
    """
    
    page_search = wiki_wiki.page(artist_name)
    if page_search.exists():
        return page_search.fullurl
    
    else:
        return f"I couldn't find a page for: {artist_name}. Check your spelling and punctation and try again."
    
def main():
    """
    Server side ZMQ 
    """

    context = zmq.Context()
    # Response socket
    socket = context.socket(zmq.REP)
    #  May need to change * to local host or 127.0.0.1
    socket.bind("tcp://127.0.0.1:5555")

    print("Server is running...")

    while True:
        message = socket.recv()
        artist_name = message.decode()
        
        if len(artist_name) > 0:
            response_message = get_wikipedia_page(artist_name)
            socket.send_string(response_message)

if __name__ == '__main__':
    main()




    