#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gdata.docs.data
import gdata.docs.client
import gdata.docs.service

# Create a client class which will make HTTP requests with Google Docs server.
client = gdata.docs.client.DocsClient(source='docsapitest-yamazaki')
client.ssl = True
client.http_client.debug = False
# Authenticate using your Google Docs email address and password.
client.ClientLogin('[your mail address]', '[password]', client.source)

# Create an empty document
new_doc = client.Create(gdata.docs.data.DOCUMENT_LABEL, 'My Doc')
print 'Document "%s" created' % new_doc.title.text

# Create an empty spreadsheet. By default, the writers_can_invite setting is True.
new_spreadsheet = client.Create(gdata.docs.data.SPREADSHEET_LABEL, 'My Spreadsheet', writers_can_invite=False)
print 'Spreadsheet "%s" created' % new_spreadsheet.title.text

# Create an empty presentation
new_preso = client.Create(gdata.docs.data.PRESENTATION_LABEL, 'My Presentation')
print 'Presentation "%s" created' % new_preso.title.text
