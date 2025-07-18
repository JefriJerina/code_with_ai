import streamlit as st

# Set page title
st.title("Name List with Lengths")

# Store 5 names in a list
names = ["Alice", "Benjamin", "Catherine", "David", "Elizabeth"]

# Display header
st.header("Names and Their Lengths")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Name")
with col2:
    st.subheader("Length")

# Display each name with its length
for name in names:
    col1, col2 = st.columns(2)
    with col1:
        st.write(name)
    with col2:
        st.write(len(name))

# Add some additional information
st.markdown("---")
st.info(f"Total names in the list: {len(names)}")

# Display the complete list
st.subheader("Complete Name List")
st.write(names)

# Show average name length
average_length = sum(len(name) for name in names) / len(names)
st.success(f"Average name length: {average_length:.1f} characters")