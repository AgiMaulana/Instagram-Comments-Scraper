import pandas as pd
from pandas import ExcelWriter
import os.path

def export(names, comments):
    fname = 'comments.xlsx'
    temp = {}
    temp_names = []
    temp_comments = []
    if os.path.isfile(fname):
        saved = pd.read_excel(fname)
        temp_names.extend(saved['name'])
        temp_comments.extend(saved['comment'])
    temp_names.extend(names)
    temp_comments.extend(comments)
    temp.update({'name': temp_names, 'comment': temp_comments})
    df = pd.DataFrame(temp)
    writer = ExcelWriter(fname)
    df.to_excel(writer, 'comments', index=False)
    writer.save()
