import streamlit as st

def find_maximum(numbers):
    """
    Find the largest number in a list without using max() function.
    
    Args:
        numbers: List of numbers
        
    Returns:
        The largest number in the list
    """
    if not numbers:
        return None
    
    maximum = numbers[0]  # Assume first element is the largest
    
    for num in numbers:
        if num > maximum:
            maximum = num
    
    return maximum

def main():
    st.title("🔢 List Maximum Finder")
    st.markdown("Find the largest number in a list without using the built-in `max()` function!")
    
    # Create tabs for different input methods
    tab1, tab2 = st.tabs(["Manual Input", "Predefined Examples"])
    
    with tab1:
        st.subheader("Enter Numbers Manually")
        
        # Text input for numbers
        numbers_input = st.text_input(
            "Enter numbers separated by commas (e.g., 5, 12, 8, 23, 1):",
            placeholder="5, 12, 8, 23, 1"
        )
        
        if numbers_input:
            try:
                # Parse the input string into a list of numbers
                numbers = [float(x.strip()) for x in numbers_input.split(',')]
                
                # Display the input list
                st.write("**Input List:**", numbers)
                
                # Find maximum
                result = find_maximum(numbers)
                
                if result is not None:
                    st.success(f"**Maximum Value:** {result}")
                    
                    # Show the process
                    with st.expander("Show Algorithm Steps"):
                        st.write("**Algorithm Process:**")
                        st.write("1. Start with the first element as the current maximum")
                        st.write("2. Compare each element with the current maximum")
                        st.write("3. If an element is larger, update the maximum")
                        st.write("4. Continue until all elements are checked")
                        
                        # Demonstrate step by step
                        st.write("\n**Step-by-step execution:**")
                        maximum = numbers[0]
                        st.write(f"Initial maximum: {maximum}")
                        
                        for i, num in enumerate(numbers[1:], 1):
                            if num > maximum:
                                st.write(f"Step {i}: {num} > {maximum}, update maximum to {num}")
                                maximum = num
                            else:
                                st.write(f"Step {i}: {num} ≤ {maximum}, keep maximum as {maximum}")
                        
                        st.write(f"Final maximum: {maximum}")
                
            except ValueError:
                st.error("Please enter valid numbers separated by commas!")
    
    with tab2:
        st.subheader("Try Predefined Examples")
        
        examples = {
            "Positive Numbers": [5, 12, 8, 23, 1, 15],
            "Mixed Numbers": [-5, 10, -2, 7, 0, 3],
            "Negative Numbers": [-10, -5, -15, -2, -8],
            "Decimal Numbers": [3.14, 2.71, 1.41, 9.87, 5.55],
            "Single Element": [42],
            "Large Numbers": [1000, 5000, 2500, 7500, 3000]
        }
        
        selected_example = st.selectbox("Choose an example:", list(examples.keys()))
        
        if st.button("Find Maximum", key="example_button"):
            numbers = examples[selected_example]
            
            st.write("**Input List:**", numbers)
            
            result = find_maximum(numbers)
            st.success(f"**Maximum Value:** {result}")
            
            # Show comparison with built-in max (for verification)
            st.info(f"Verification with built-in max(): {max(numbers)}")
    
    # Algorithm explanation section
    st.markdown("---")
    st.subheader("📚 Algorithm Explanation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **How it works:**
        1. Initialize the first element as the current maximum
        2. Iterate through the remaining elements
        3. Compare each element with the current maximum
        4. Update maximum if a larger element is found
        5. Return the final maximum value
        """)
    
    with col2:
        st.markdown("""
        **Time Complexity:** O(n) - Linear time
        
        **Space Complexity:** O(1) - Constant space
        
        **Edge Cases Handled:**
        - Empty list returns None
        - Single element list
        - All negative numbers
        - Mixed positive/negative numbers
        """)
    
    # Code display
    with st.expander("View Source Code"):
        st.code("""
def find_maximum(numbers):
    if not numbers:
        return None
    
    maximum = numbers[0]  # Assume first element is the largest
    
    for num in numbers:
        if num > maximum:
            maximum = num
    
    return maximum
        """, language="python")

if __name__ == "__main__":
    main()