# ResearchRadar
Contributors: Emily Duire-Johnson, Anubha Thapliyal 

## Inspiration
- inspired by the 2024 OMSCS Conference
- how do we continue to learn (via top researchers or labs)
- Google Scholar is great, but can be overwhelming and enforces its own page ranking algorithm

## What it does
Our app simplifies the task of searching for top researchers in a particular area and summarizes their latest work

## How we built it
Our demo + supplemental slide deck provides an overview of the planning process and system design. At a high level, it is a web app that uses Streamlit for the front-end, and Python + Google Scholar + open-source LLMs for the back-end and processing of information.

## Challenges we ran into
- unable to use OpenAI's API due to limited free tier options
- open-source LLM summarization was not great
- Google Scholar also imposes a monthly limit of 100 search queries for the free tier

## Accomplishments and what we learned
- learned or got better at: working with the Google Scholar API, Canva, open-source models via Hugging Face, Streamlit, OpenAI's API, prompt engineering and python

## What's next for ResearchRadar
- scaling it up
- integrating ChatGPT
- integrating Google Patent API