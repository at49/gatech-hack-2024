import pandas as pd
import pdb

from transformers import pipeline
from sampleData import sampleData1, geoffSamplePapers


# Asks a Model based on full string
def askToModel(in_string):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    summary = summarizer(
        in_string,
        max_length=2000,
        min_length=50,
        do_sample=False,
    )
    sum_out = summary[0]["summary_text"]
    return sum_out


"""Tests"""

#
# def geoffTest():
#     # Test Setup for one Author
#     longDesc, longArr = geoffSamplePapers()
#     myBoi = AuthorObject("Geoff Hinton")
#     for p in longArr:
#         myBoi.abstractList.append(p)
#     summary = askToModel(myBoi.getStringOfAbstracts())
#     print(summary[0]["summary_text"])


# def loadTestData():
#     myDF = sampleData1()
#     return myDF


# def dummyInputTest():
#     # GPT Approach
#     # question = formatQuestionForGPT(myBoi)
#     # response = askGPTAQuestion(question, apiKey)
#     df = loadTestData()
#     return summarize(df)


""""""


# USES TENSORFLOW
# Input = Data Frame that contains columns for:
#           Author, Date, Abstract, Author Interests
# Output = A Condensed Dataframe with one entry per author that includes a summary column
def summarize_tensor(df):
    out_list = []
    out_columns = ["name", "affiliation", "interests", "summary"]
    # Split out by unique author
    for n_val in df["name"].unique():
        df_temp = df.loc[df["name"] == n_val]
        full_desc_string = df_temp["description"].str.cat(sep=" ")
        summary = askToModel(full_desc_string)
        author_row = [
            n_val,
            df_temp["affiliations"][df_temp.index[0]],
            df_temp["interests"][df_temp.index[0]],
            summary,
        ]
        out_list.append(author_row)

    new_df = pd.DataFrame(out_list, columns=out_columns)
    return new_df


# Input = Data Frame that contains columns for:
#           Author, Date, Abstract, Author Interests
# Output = A Condensed Dataframe with one entry per author that includes a summary column
def summarize(df):
    out_list = []
    out_columns = ["name", "affiliation", "interests", "title"]
    # Split out by unique author
    for n_val in df["name"].unique():
        df_temp = df.loc[df["name"] == n_val]
        # Titles
        df_title_list = df_temp["title"].tolist()
        author_row = [
            n_val,
            df_temp["affiliations"][df_temp.index[0]],
            df_temp["interests"][df_temp.index[0]],
            df_title_list,
        ]
        out_list.append(author_row)

    new_df = pd.DataFrame(out_list, columns=out_columns)
    return new_df
