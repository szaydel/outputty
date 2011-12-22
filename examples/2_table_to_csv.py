#!/usr/bin/env python
# coding: utf-8
# title = Exporting to a CSV File
# output = 'my-data.csv'
#Using plugins we can import and export `Table` data to CSV (really, to and
#from a lot of formats). Let's export Python `list` and `dict` to a CSV file.

from outputty import Table

my_table = Table(headers=['First name', 'Last name'])
my_table.rows.append({'First name': 'Álvaro', 'Last name': 'Justen'})
my_table.rows.append(('Flávio', 'Amieiro'))
my_table.write('csv', 'my-data.csv')
