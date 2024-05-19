import streamlit as st
import pandas as pd

from streamlit_card import card
from summarizeWithModel import summarize

from scholar import get_top_pubs


def getResults(user_input):
    with st.spinner("Loading Data..."):

        # code that generates search results and returns authors + pubs
        df = get_top_pubs(user_input)
        df2 = summarize(df)
    return df2


def renderCards(df):
    for row in df.values:
        author = row[0]
        affiliation = row[1]
        interests = row[2]
        title = row[3]

        st.subheader(f"{author}")
        st.write(f"Affiliation: {affiliation}")
        st.write(f"Specializations: {', '.join(interests)}")
        st.write(f"Recent Papers: {', '.join(title)}")


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


if __name__ == "__main__":
    main()
