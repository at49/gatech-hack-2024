# ResearchRadar

Contributors: Emily Duire-Johnson, Anubha Thapliyal  
Hackathon: Developed for the 2024 hackOMSCS Competition

## Instructions to Run

1. Install all the packages listed in requirements.txt
2. Add your Google Scholar API Key into src/config.py. This API Key can be generated by visiting: https://serpapi.com/users/sign_up
3. Launch the App with the following command:
```streamlit run src/main.py```

## Inspiration

- We met and were inspired by the 2024 OMSCS Conference
- How do we continue to learn (via top researchers or labs)
- Google Scholar is great, but can be overwhelming and enforces its own page ranking algorithm

## What it does

Our app simplifies the task of searching for top researchers in a particular area and summarizes their latest work.

## How we built it

Our demo + supplemental slide deck provides an overview of the planning process and system design. At a high level, it is a web app that uses Streamlit for the front-end, and Python + Google Scholar + open-source LLMs for the back-end and processing of information.

## Challenges we ran into

- We were unable to use OpenAI's API due to limited free tier options
- Our back-up options for open-source LLM summarization did not yeild results of as high of quality as the ChatGPT results
- Google Scholar also imposes a monthly limit of 100 search queries for the free tier, which limited our testing options

## Accomplishments and what we learned

We learned or got better at working with:

- Google Scholar API
- Canva
- Open-source models via Hugging Face
- Streamlit
- OpenAI's API
- Prompt engineering

## What's next for ResearchRadar

- Scaling it up: increasing the number of authors returned in the result, and the number of papers summarized
- Integrating ChatGPT into the results
- integrating Google Patent API
