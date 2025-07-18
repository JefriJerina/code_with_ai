import streamlit as st
import pandas as pd
import plotly.express as px

def count_numbers(numbers):
    """Count positive, negative, and zero numbers in a list."""
    positive_count = 0
    negative_count = 0
    zero_count = 0
    
    for num in numbers:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1
    
    return positive_count, negative_count, zero_count

def main():
    st.set_page_config(
        page_title="Number Counter",
        page_icon="🔢",
        layout="wide"
    )
    
    st.title("🔢 Number Counter")
    st.markdown("Count how many positive, negative, and zero numbers are in your list!")
    
    # Input methods
    st.sidebar.header("Input Options")
    input_method = st.sidebar.radio(
        "Choose input method:",
        ["Manual Entry", "Upload CSV", "Random Generator"]
    )
    
    numbers = []
    
    if input_method == "Manual Entry":
        st.subheader("Enter Numbers")
        
        # Text area for bulk input
        numbers_text = st.text_area(
            "Enter numbers separated by commas, spaces, or new lines:",
            placeholder="Example: 1, -2, 0, 3.5, -7, 0, 10",
            height=100
        )
        
        if numbers_text:
            try:
                # Parse the input text
                import re
                # Split by comma, space, or newline
                number_strings = re.split(r'[,\s\n]+', numbers_text.strip())
                numbers = [float(num.strip()) for num in number_strings if num.strip()]
                
                if not numbers:
                    st.warning("Please enter valid numbers.")
                    return
                    
            except ValueError:
                st.error("Please enter valid numbers separated by commas, spaces, or new lines.")
                return
    
    elif input_method == "Upload CSV":
        st.subheader("Upload CSV File")
        uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                st.write("CSV Preview:")
                st.dataframe(df.head())
                
                # Let user select which column contains numbers
                numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
                
                if numeric_columns:
                    selected_column = st.selectbox("Select the column with numbers:", numeric_columns)
                    numbers = df[selected_column].dropna().tolist()
                else:
                    st.error("No numeric columns found in the CSV file.")
                    return
                    
            except Exception as e:
                st.error(f"Error reading CSV file: {str(e)}")
                return
    
    elif input_method == "Random Generator":
        st.subheader("Generate Random Numbers")
        
        col1, col2 = st.columns(2)
        with col1:
            count = st.slider("Number of random numbers:", 10, 1000, 100)
            min_val = st.number_input("Minimum value:", value=-100.0)
        with col2:
            seed = st.number_input("Random seed (for reproducibility):", value=42, step=1)
            max_val = st.number_input("Maximum value:", value=100.0)
        
        if st.button("Generate Numbers"):
            import random
            random.seed(int(seed))
            numbers = [random.uniform(min_val, max_val) for _ in range(count)]
            # Add some zeros for demonstration
            for _ in range(count // 20):
                numbers[random.randint(0, len(numbers)-1)] = 0.0
    
    # Process and display results
    if numbers:
        st.subheader("Results")
        
        # Count the numbers
        positive_count, negative_count, zero_count = count_numbers(numbers)
        total_count = len(numbers)
        
        # Display summary statistics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Total Numbers", total_count)
        with col2:
            st.metric("Positive Numbers", positive_count, 
                     delta=f"{positive_count/total_count*100:.1f}%")
        with col3:
            st.metric("Negative Numbers", negative_count,
                     delta=f"{negative_count/total_count*100:.1f}%")
        with col4:
            st.metric("Zero Numbers", zero_count,
                     delta=f"{zero_count/total_count*100:.1f}%")
        
        # Create visualization
        col1, col2 = st.columns(2)
        
        with col1:
            # Pie chart
            counts_data = {
                'Type': ['Positive', 'Negative', 'Zero'],
                'Count': [positive_count, negative_count, zero_count],
                'Color': ['#2E8B57', '#DC143C', '#708090']
            }
            
            fig_pie = px.pie(
                counts_data, 
                values='Count', 
                names='Type',
                title='Distribution of Number Types',
                color='Type',
                color_discrete_map={
                    'Positive': '#2E8B57',
                    'Negative': '#DC143C', 
                    'Zero': '#708090'
                }
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Bar chart
            fig_bar = px.bar(
                counts_data,
                x='Type',
                y='Count',
                title='Count by Number Type',
                color='Type',
                color_discrete_map={
                    'Positive': '#2E8B57',
                    'Negative': '#DC143C',
                    'Zero': '#708090'
                }
            )
            fig_bar.update_layout(showlegend=False)
            st.plotly_chart(fig_bar, use_container_width=True)
        
        # Detailed breakdown
        st.subheader("Detailed Information")
        
        # Show some sample numbers
        if len(numbers) <= 50:
            st.write("**Your numbers:**")
            st.write(numbers)
        else:
            st.write(f"**First 25 numbers:** {numbers[:25]}")
            st.write(f"**Last 25 numbers:** {numbers[-25:]}")
        
        # Statistics table
        stats_df = pd.DataFrame({
            'Category': ['Positive', 'Negative', 'Zero', 'Total'],
            'Count': [positive_count, negative_count, zero_count, total_count],
            'Percentage': [
                f"{positive_count/total_count*100:.1f}%",
                f"{negative_count/total_count*100:.1f}%", 
                f"{zero_count/total_count*100:.1f}%",
                "100.0%"
            ]
        })
        
        st.table(stats_df)
        
        # Additional statistics
        if numbers:
            st.subheader("Additional Statistics")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Minimum Value", f"{min(numbers):.2f}")
                st.metric("Maximum Value", f"{max(numbers):.2f}")
            
            with col2:
                avg = sum(numbers) / len(numbers)
                st.metric("Average", f"{avg:.2f}")
                
                # Median
                sorted_nums = sorted(numbers)
                n = len(sorted_nums)
                median = (sorted_nums[n//2] + sorted_nums[(n-1)//2]) / 2
                st.metric("Median", f"{median:.2f}")
            
            with col3:
                positive_nums = [n for n in numbers if n > 0]
                negative_nums = [n for n in numbers if n < 0]
                
                if positive_nums:
                    st.metric("Avg Positive", f"{sum(positive_nums)/len(positive_nums):.2f}")
                if negative_nums:
                    st.metric("Avg Negative", f"{sum(negative_nums)/len(negative_nums):.2f}")
    
    else:
        st.info("Please enter some numbers to get started!")
        
        # Example section
        st.subheader("Example")
        st.write("Try entering: `1, -2, 0, 3.5, -7, 0, 10, -1, 5`")
        
        if st.button("Load Example"):
            example_numbers = [1, -2, 0, 3.5, -7, 0, 10, -1, 5]
            positive_count, negative_count, zero_count = count_numbers(example_numbers)
            
            st.write(f"**Example Result:**")
            st.write(f"Numbers: {example_numbers}")
            st.write(f"Positive: {positive_count}, Negative: {negative_count}, Zero: {zero_count}")

if __name__ == "__main__":
    main()
    