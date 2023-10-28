import pandas as pd
from pandas import ExcelWriter
import os.path

def export(names, comments):
    fname = 'comments.xlsx'
    temp = {}
    temp_names = []
    temp_comments = []
    # if os.path.isfile(fname):
    #     saved = pd.read_excel(fname)
    #     temp_names.extend(saved['name'])
    #     temp_comments.extend(saved['comment'])
    # temp_names.extend(names)
    # temp_comments.extend(comments)
    temp.update({'name': names, 'comment': comments})
    df = pd.DataFrame(temp)



    df.to_excel(fname)
