import streamlit as st
import pandas as pd
from db_fxns import *
import streamlit.components.v1 as stc

HTML_BANNER = """
    <div style="background-color:#000000;padding:5px;border-radius:5px">
    <h1 style="color:white;text-align:center;">I.O.U. 1</h1>
    <p style="color:white;text-align:center;">Goodwill - gameified!</p>
    </div>
    """


def main():
    stc.html(HTML_BANNER)

    menu = ["Ask a Favour", "Favour List", "Tackle a Favour", "Erase a Favour", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()

    if choice == "Ask a Favour":
        st.subheader("Ask a Favour")
        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Your Request")


        with col2:
            task_status = "Open"
            task_due_date = st.date_input("Favour Expiry Date")
            requested_by = st.text_input("Your Name")

        if st.button("Add Favour"):
            claimed_by = "No one."
            add_data(task, task_status, task_due_date, requested_by, claimed_by)
            st.success("Added ::{} ::To Favours".format(task))


    elif choice == "Favour List":

        st.subheader("Favour List")

        result = view_all_data()

        clean_df = pd.DataFrame(result, columns=["Favour", "Status", "Expiry Date", "Requested By", "Claimed By"])
        st.dataframe(clean_df)

    elif choice == "Tackle a Favour":

        list_of_tasks = [i[0] for i in view_all_task_names()]
        selected_task = st.selectbox("Select a Favour", list_of_tasks)
        task_result = get_task(selected_task)

        if task_result:
            task = task_result[0][0]
            task_status = task_result[0][1]
            task_due_date = task_result[0][2]
            requested_by = task_result[0][3]
            claimed_by = task_result[0][4]

            col1, col2 = st.columns(2)

            with col1:
                new_task = task
                new_claimed_by = st.text_input("Your Name")
            with col2:
                new_requested_by = requested_by
                new_task_status = st.selectbox("Favour Status", ["Open", "In Progress", "Completed"])
                new_task_due_date = task_due_date

            if st.button("Update Favour"):
                edit_task_data(new_task, new_task_status, new_task_due_date, new_requested_by, new_claimed_by, task, task_status, task_due_date, requested_by, claimed_by)
                st.success("Updated ::{} ::To {}".format(task, new_task))


    elif choice == "Erase a Favour":
        st.subheader("Erase a Favour")

        unique_list = [i[0] for i in view_all_task_names()]
        delete_by_task_name = st.selectbox("Select Task", unique_list)
        if st.button("Delete"):
            delete_data(delete_by_task_name)
            st.warning("Deleted: '{}'".format(delete_by_task_name))

    elif choice == "About":
        st.subheader("About this project")
        st.text("'The Internet of Things', 'Artificial Intelligence', 'Blockchain.'")
        st.text("It's 2022, and there's really only one final thing that hasn't been optimized:")
        st.text("random acts of kindness.")
        st.text("I.O.U. 1 is a simple marketplace in which we trade favours to maximize")
        st.text("our collective productivity.")
        st.text("Dystopian? Maybe. Fun? You bet!")
        st.text("")
        st.text("_______________________________________________________________")
        st.text("")
        st.text("This page was made using Python and Streamlit by me, Nick Lam, and was submitted")
        st.text("as a final project for CS50. I referred to JCharisTech's tutorial on building a")
        st.text("CRUD app on Streamlit (https://www.youtube.com/watch?v=i6gt2OKezOQ) for a few of")
        st.text("the features used on this site.")
        st.text(" ")
        st.text("To everyone who helped me on this project - thanks! I.O.U. 1 :)")

if __name__ == '__main__':
    main()