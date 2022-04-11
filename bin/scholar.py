#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 17:27:31 2018

@author: fabrizzio
"""

from scholarly import scholarly

#def install_and_import(package):
#    import importlib
#    try:
#        importlib.import_module(package)
#    except ImportError:
#        import pip
#        pip.main(['install', package])
#    finally:
#        globals()[package] = importlib.import_module(package)



class Author:
    def __init__(self, author = None):

        if (author == None):
            raise ValueError('Missing author.')

        self.hIndex = 0;
        self.gIndex = 0;
        self.citations = 0;
        self.author = author
        self.publication = []
        self.__extractScholar(author)

    def __extractScholar(self,author):

        author1 = scholarly.search_author_id('Lu-BjV4AAAAJ')
        author1 = scholarly.fill(author1, sections=['basics', 'indices', 'counts', 'publications'])

        for publication in author1['publications']:
            url = "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=Lu-BjV4AAAAJ&citation_for_view=" + str(publication['author_pub_id'])
            bib = publication['bib']
            self.publication.append({"id": publication['author_pub_id'], "name": bib['title'], "url": url, "citecount" : publication['num_citations']})

        self.citations = author1['citedby']
        self.hIndex = author1['hindex']
        self.gIndex = author1['i10index']
