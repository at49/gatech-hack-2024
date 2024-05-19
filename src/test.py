import streamlit as st
import pandas as pd
from streamlit_card import card
from summarizeWithModel import summarize

# from scholar import get_search_keyword, get_top_pubs


def getResults(user_input):
    with st.spinner("Loading Data..."):
        df = pd.read_csv('output/test_results.csv')
        # df = dummyInputTest()
        df2 = summarize(df)
    return df2


def renderCards(df):
    for row in df.values:
        author = row[0]
        affiliation = row[1]
        interests = row[2]
        summary = row[3]

        card(
            title=f"{author} at {affiliation}",
            text=f"Their specializations include: {interests}. \n {summary} ",
            styles={
                "card": {
                    "width": "500px",
                    "height": "400px",
                    "border-radius": "60px",
                    "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
                },
                "text": {
                    "font-family": "serif",
                },
                "filter": {
                    "background-color": "rgba(98, 29, 112, 1)",
                },
            },
        )


def main():
    st.title("ResearchRadar")
    user_input = st.text_input("Research Topic Here:")
    if st.button("Submit"):
        if user_input:
            st.success(f"You searched for {user_input}!")
            df = getResults(user_input)
            renderCards(df)
        else:
            st.error(f"Must provide text")

    # code that generates seatch results and returns authors + pubs
    # top_pubs = get_top_pubs(user_input)


if __name__ == "__main__":
    main()
