import os
import functions

# get keywords, inverted index and titles
f = open('s2-titles.txt', encoding="utf8")
titles_lines = f.readlines()
f.close()

bag_of_words = functions.get_bag_of_words(titles_lines)
keywords = functions.get_keywords(titles_lines, bag_of_words)
inverted_index = functions.get_inverted_index(keywords)
titles = functions.get_titles(titles_lines)

# run search query
query = input('Input your search query: ')
while query != '':
    query_terms = query.split()
    sorted_results = functions.get_search_results(query_terms,
                                                    keywords,
                                                    inverted_index)
    print('==> search results for query:', query)
    for result in sorted_results:
        print (result, titles[result])
    query = input('Input your search query [hit return to quit]:')

# get unit vectors
f = open('s2-categories.tsv')
categories_lines = f.readlines()
f.close()
unit_vectors = functions.get_unit_vectors(keywords, categories_lines)

# run recommendation algorithm
seed_courseid = input('Input your seed courseid: ')
while seed_courseid != '':
    sorted_results = functions.get_recommendation_results(seed_courseid,
                                                        keywords,
                                                        inverted_index,
                                                        unit_vectors)
    print ('==> recommendation results: ')
    for result in sorted_results:
        print (result, titles[result])
        print (functions.get_dot_product(seed_courseid, result, unit_vectors))
    seed_courseid = input('Input seed courseid [hit return to quit]')


