#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gdata.docs.client


# Create a client class which will make HTTP requests with Google Docs server.
client = gdata.docs.client.DocsClient(source='docsapitest-yamazaki')
client.ssl = True
client.http_client.debug = False
# Authenticate using your Google Docs email address and password.
client.ClientLogin('[your mail address]', '[password]', client.source)

# Query the server for an Atom feed containing a list of your documents.
feed = client.GetDocList(uri='/feeds/default/private/full/')
# Loop through the feed and extract each document entry.
for doc in feed.entry:
    # Display the title of the document on the command line.
    print doc.title.text