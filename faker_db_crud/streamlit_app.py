# streamlit_app.py
# Streamlit 프론트엔드 - Library Dashboard

import requests
import streamlit as st
import pandas as pd

API_URL = "http://127.0.0.1:8000"


def fetch_books():
    resp = requests.get(f"{API_URL}/books")
    if resp.status_code == 200:
        return resp.json()
    return []


st.title("📚 Library Management Dashboard")

st.sidebar.header("Actions")
action = st.sidebar.radio("Select action", ["View books", "Add book"])

if action == "View books":
    st.subheader("Book List")
    books = fetch_books()
    if books:
        df = pd.DataFrame(books)
        st.dataframe(df)

        st.subheader("Update or Delete")
        selected_id = st.number_input(
            "Book ID", min_value=1, step=1, format="%d", value=1
        )
        if st.button("Load book"):
            book_resp = requests.get(f"{API_URL}/books/{selected_id}")
            if book_resp.status_code == 200:
                book = book_resp.json()
                title = st.text_input("Title", value=book["title"])
                author = st.text_input("Author", value=book["author"])
                year = st.number_input("Year", value=book["year"], step=1)
                available = st.selectbox(
                    "Available", options=[1, 0], index=0 if book["available"] == 1 else 1
                )

                if st.button("Save changes"):
                    update_payload = {
                        "title": title,
                        "author": author,
                        "year": int(year),
                        "available": int(available),
                    }
                    put_resp = requests.put(
                        f"{API_URL}/books/{selected_id}", json=update_payload
                    )
                    if put_resp.status_code == 200:
                        st.success("Book updated.")
                    else:
                        st.error("Update failed.")

                if st.button("Delete book"):
                    del_resp = requests.delete(f"{API_URL}/books/{selected_id}")
                    if del_resp.status_code == 200:
                        st.success("Book deleted.")
                    else:
                        st.error("Delete failed.")
            else:
                st.error("Book not found.")
    else:
        st.info("No books found.")

elif action == "Add book":
    st.subheader("Add new book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", step=1, min_value=0, value=2024)
    if st.button("Create"):
        payload = {"title": title, "author": author, "year": int(year)}
        resp = requests.post(f"{API_URL}/books", json=payload)
        if resp.status_code == 200:
            st.success("Book created.")
        else:
            st.error("Create failed.")
