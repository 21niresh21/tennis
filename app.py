import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["Matches", "Standings", "Admin"])

with tab1:
    # Sample data
    player1 = "Sumeet"
    player2 = "Shourya"
    placeholder_image_url = "https://img.freepik.com/premium-vector/empty-face-icon-avatar-with-black-hair-vector-illustration_601298-13402.jpg"
    match_info = "Upcoming match on Jan 10, 2025"

    matches = [
    {"player1": "Sumeet", "player2": "Shourya",
        "info": "Upcoming match on Jan 10, 2025"},
    {"player1": "Sashi", "player2": "Dilip",
        "info": "Upcoming match on Jan 11, 2025"},
    {"player1": "Sashi", "player2": "Dilip", "info": "6-2"},  # Completed match
    {"player1": "Karma Zimpa Bhutia", "player2": "Jitender Kumar", "info": "6-1"},
    {"player1": "Asif", "player2": "Rithik", "info": "6-0"},
    {"player1": "Manoj Kaushik", "player2": "Yash", "info": "6-1"},
    {"player1": "Rajesh", "player2": "Siddhanth", "info": "6-0"},
    {"player1": "Khush", "player2": "Yashraj", "info": "6-2"},
    {"player1": "Nagalia", "player2": "Ritesh", "info": "6-2"},
    {"player1": "Singhania", "player2": "Aanag", "info": "7-5"},
    {"player1": "Sashi", "player2": "Nanda", "info": "6-1"}
]


    for match in matches:
        with st.container():
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                st.image(placeholder_image_url, width=50)
                st.write(match["player1"])
            with col2:
                st.image(placeholder_image_url, width=50)
                st.write(match["player2"])
            with col3:
                st.write(match["info"])


with tab2:
    tab1, tab2, tab3 = st.tabs(["Singles", "Doubles", "Kids"])

    with tab1:
        # Sample data for standings
        standings_data = {
            "Group": ["Group A", "Group A", "Group B", "Group B", "Group C", "Group C", "Group D", "Group D"],
            "Name": ["Sumeet", "Shourya", "Pranav", "Anurag", "Bhutia", "Vinit", "Asif", "Jeet"],
            "Matches": [3, 3, 3, 3, 3, 3, 3, 3],
            "Wins": [2, 1, 2, 1, 3, 0, 1, 2],
            "Losses": [1, 2, 1, 2, 0, 3, 2, 1],
            "Game Diff": [5, -3, 4, -2, 10, -10, -5, 7],
        }

        # Convert to DataFrame
        standings_df = pd.DataFrame(standings_data)

        # Display title
        st.title("Tennis Tournament - Standings")

        # Container for the table
        with st.container():
            # Define column structure
            header_col1, header_col2, header_col3, header_col4, header_col5, header_col6 = st.columns(
                [2, 2, 1, 1, 1, 1]
            )
            header_col1.markdown("<b>Group</b>", unsafe_allow_html=True)
            header_col2.markdown("<b>Name</b>", unsafe_allow_html=True)
            header_col3.markdown("<b>Matches</b>", unsafe_allow_html=True)
            header_col4.markdown("<b>Wins</b>", unsafe_allow_html=True)
            header_col5.markdown("<b>Losses</b>", unsafe_allow_html=True)
            header_col6.markdown("<b>Game Diff</b>", unsafe_allow_html=True)

            # Track the current group for row spanning
            current_group = None
            row_span_counter = 0

            for index, row in standings_df.iterrows():
                col1, col2, col3, col4, col5, col6 = st.columns(
                    [2, 2, 1, 1, 1, 1])

                if row["Group"] != current_group:
                    # Write the group name only if it's a new group
                    col1.markdown(
                        f"<p style='font-size: 16px; font-weight: bold;'>{
                            row['Group']}</p>",
                        unsafe_allow_html=True,
                    )
                    current_group = row["Group"]
                else:
                    col1.markdown("<p></p>", unsafe_allow_html=True)

                col2.markdown(
                    f"<p style='font-size: 16px;'>{row['Name']}</p>", unsafe_allow_html=True)
                col3.markdown(
                    f"<p style='font-size: 16px;'>{row['Matches']}</p>", unsafe_allow_html=True)
                col4.markdown(
                    f"<p style='font-size: 16px;'>{row['Wins']}</p>", unsafe_allow_html=True)
                col5.markdown(
                    f"<p style='font-size: 16px;'>{row['Losses']}</p>", unsafe_allow_html=True)
                col6.markdown(
                    f"<p style='font-size: 16px;'>{row['Game Diff']}</p>", unsafe_allow_html=True)
