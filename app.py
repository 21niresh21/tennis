import streamlit as st
import pandas as pd

tab1, tab2, tab3 = st.tabs(["Matches", "Standings", "Admin"])

with tab1:
    # Sample data
    player1 = "Player A"
    player2 = "Player B"
    placeholder_image_url = "https://img.freepik.com/premium-vector/empty-face-icon-avatar-with-black-hair-vector-illustration_601298-13402.jpg"
    match_info = "Upcoming match on Jan 10, 2025"

    # Creating a container for the layout
    with st.container():
        # Create columns
        col1, col2, col3 = st.columns([1, 1, 2])

        # First row
        with col1:
            st.image(placeholder_image_url, width=50)
            st.write(player1)
        with col2:
            st.image(placeholder_image_url, width=50)
            st.write(player2)

        # Third column spanning two rows
        with col3:
            st.write(match_info)


    with st.container():
        # Create columns
        col1, col2, col3 = st.columns([1, 1, 2])

        # First row: Player 1
        with col1:
            st.image(placeholder_image_url, width=50)
            st.write(player1)
        
        # Second row: Player 2
        with col2:
            st.image(placeholder_image_url, width=50)
            st.write(player2)

        # Third column spanning two rows: Match info
        with col3:
            st.write("\n")
            st.write("\n")
            st.write(match_info)

    with st.container():
        # Create columns
        col1, col2, col3 = st.columns([1, 1, 2])

        # First row: Player 1
        with col1:
            st.image(placeholder_image_url, width=50)
            st.write(player1)
        
        # Second row: Player 2
        with col2:
            st.image(placeholder_image_url, width=50)
            st.write(player2)

        # Third column spanning two rows: Match info
        with col3:
            st.write("\n")
            st.write("\n")
            st.write("6-2")

with tab2:
    tab1, tab2, tab3 = st.tabs(["Singles", "Doubles", "Kids"])

    with tab1:
        # Sample data for standings
        standings_data = {
            "Name": ["Player A", "Player B", "Player C", "Player D", "Player E", "Player F", "Player G", "Player H"],
            "Matches": [5, 5, 5, 5, 5, 5, 5, 5],
            "Wins": [3, 2, 3, 1, 2, 1, 4, 0],
            "Losses": [2, 3, 2, 4, 3, 4, 1, 5],
            "Game Diff": [10, -5, 8, -10, 4, -7, 12, -15],
        }

        # Convert to DataFrame
        standings_df = pd.DataFrame(standings_data)

        # Display title
        st.title("Tennis Tournament - Standings")

        # Container for styling
        with st.container():
            # Table header
            header_col1, header_col2, header_col3, header_col4, header_col5 = st.columns([2, 1, 1, 1, 1])
            header_col1.markdown("<b>Name</b>", unsafe_allow_html=True)
            header_col2.markdown("<b>Matches</b>", unsafe_allow_html=True)
            header_col3.markdown("<b>Wins</b>", unsafe_allow_html=True)
            header_col4.markdown("<b>Losses</b>", unsafe_allow_html=True)
            header_col5.markdown("<b>Game Diff</b>", unsafe_allow_html=True)

            # Table rows
            for index, row in standings_df.iterrows():
                col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
                col1.markdown(f"<p style='font-size: 16px;'>{row['Name']}</p>", unsafe_allow_html=True)
                col2.markdown(f"<p style='font-size: 16px;'>{row['Matches']}</p>", unsafe_allow_html=True)
                col3.markdown(f"<p style='font-size: 16px;'>{row['Wins']}</p>", unsafe_allow_html=True)
                col4.markdown(f"<p style='font-size: 16px;'>{row['Losses']}</p>", unsafe_allow_html=True)
                col5.markdown(f"<p style='font-size: 16px;'>{row['Game Diff']}</p>", unsafe_allow_html=True)
