import streamlit

streamlit.set_page_config(page_title="My webpage", page_icon=":tada:", layout="wide")

with streamlit.container():
    streamlit.subheader("Hi, I am Sanskriti :wave:")
    streamlit.title("A Software Engineer From Nepal")
    streamlit.write("I am passionate about finding different ways to use NLP and machine learning models to improve SaaS products.")
    streamlit.write("[Contact Me >](https://www.linkedin.com/in/sanskriti-timseena)")

with streamlit.container():
    streamlit.write("---")
    left_column, right_column = streamlit.columns(2)
    with left_column:
        streamlit.header("What I do")
        streamlit.write("##")