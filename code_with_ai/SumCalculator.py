import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import time
import math

def sum_using_for_loop(n):
    """Calculate sum using for loop."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_using_while_loop(n):
    """Calculate sum using while loop."""
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total

def sum_using_formula(n):
    """Calculate sum using mathematical formula: n(n+1)/2."""
    return n * (n + 1) // 2

def sum_using_recursion(n):
    """Calculate sum using recursion."""
    if n <= 1:
        return n
    return n + sum_using_recursion(n - 1)

def measure_execution_time(func, n):
    """Measure execution time of a function."""
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, (end_time - start_time) * 1000  # Convert to milliseconds

def main():
    st.set_page_config(
        page_title="Sum Calculator",
        page_icon="🧮",
        layout="wide"
    )
    
    st.title("🧮 Sum Calculator (1 to n)")
    st.markdown("Calculate the sum of all numbers from 1 to n using different methods!")
    
    # Sidebar for input
    st.sidebar.header("Input Parameters")
    
    # Number input
    n = st.sidebar.number_input(
        "Enter the value of n:",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )
    
    # Method selection
    methods = st.sidebar.multiselect(
        "Select calculation methods:",
        ["For Loop", "While Loop", "Mathematical Formula", "Recursion"],
        default=["For Loop", "While Loop", "Mathematical Formula"]
    )
    
    # Performance comparison option
    show_performance = st.sidebar.checkbox("Show Performance Comparison", value=True)
    
    # Show step-by-step for small numbers
    show_steps = st.sidebar.checkbox("Show Step-by-step (for n ≤ 20)", value=False)
    
    if not methods:
        st.warning("Please select at least one calculation method.")
        return
    
    # Main content
    st.subheader(f"Calculating Sum from 1 to {n}")
    
    # Results storage
    results = {}
    execution_times = {}
    
    # Calculate using selected methods
    if "For Loop" in methods:
        if n <= 1000 or st.sidebar.button("Calculate with For Loop (may be slow for large n)"):
            result, exec_time = measure_execution_time(sum_using_for_loop, n)
            results["For Loop"] = result
            execution_times["For Loop"] = exec_time
    
    if "While Loop" in methods:
        if n <= 1000 or st.sidebar.button("Calculate with While Loop (may be slow for large n)"):
            result, exec_time = measure_execution_time(sum_using_while_loop, n)
            results["While Loop"] = result
            execution_times["While Loop"] = exec_time
    
    if "Mathematical Formula" in methods:
        result, exec_time = measure_execution_time(sum_using_formula, n)
        results["Mathematical Formula"] = result
        execution_times["Mathematical Formula"] = exec_time
    
    if "Recursion" in methods:
        if n <= 100:
            result, exec_time = measure_execution_time(sum_using_recursion, n)
            results["Recursion"] = result
            execution_times["Recursion"] = exec_time
        else:
            st.warning("Recursion method skipped for n > 100 to avoid stack overflow.")
    
    # Display results
    if results:
        st.subheader("Results")
        
        # Create columns for results
        cols = st.columns(len(results))
        
        for i, (method, result) in enumerate(results.items()):
            with cols[i]:
                st.metric(
                    method,
                    f"{result:,}",
                    delta=f"{execution_times[method]:.3f}ms"
                )
        
        # Verification
        expected_result = sum_using_formula(n)
        all_correct = all(result == expected_result for result in results.values())
        
        if all_correct:
            st.success("✅ All methods produced the correct result!")
        else:
            st.error("❌ Some methods produced incorrect results!")
        
        # Performance comparison
        if show_performance and len(results) > 1:
            st.subheader("Performance Comparison")
            
            # Create performance dataframe
            perf_df = pd.DataFrame({
                'Method': list(execution_times.keys()),
                'Execution Time (ms)': list(execution_times.values())
            })
            
            # Bar chart for execution times
            fig_bar = px.bar(
                perf_df,
                x='Method',
                y='Execution Time (ms)',
                title='Execution Time Comparison',
                color='Method'
            )
            st.plotly_chart(fig_bar, use_container_width=True)
            
            # Performance table
            st.table(perf_df)
        
        # Step-by-step calculation for small numbers
        if show_steps and n <= 20:
            st.subheader("Step-by-step Calculation")
            
            # Show for loop steps
            if "For Loop" in results:
                st.write("**For Loop Steps:**")
                steps = []
                running_sum = 0
                
                for i in range(1, n + 1):
                    running_sum += i
                    steps.append(f"Step {i}: {running_sum - i} + {i} = {running_sum}")
                
                step_text = "\n".join(steps)
                st.text(step_text)
            
            # Show mathematical breakdown
            st.write("**Mathematical Formula:**")
            st.latex(r"Sum = \frac{n(n+1)}{2}")
            st.latex(f"Sum = \\frac{{{n}({n}+1)}}{{2}} = \\frac{{{n} \\times {n+1}}}{{2}} = \\frac{{{n*(n+1)}}}{{2}} = {n*(n+1)//2}")
    
    # Visualization section
    if results:
        st.subheader("Visualization")
        
        # Create sequence visualization for small n
        if n <= 100:
            # Line chart showing cumulative sum
            numbers = list(range(1, n + 1))
            cumulative_sums = []
            running_sum = 0
            
            for num in numbers:
                running_sum += num
                cumulative_sums.append(running_sum)
            
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(
                x=numbers,
                y=cumulative_sums,
                mode='lines+markers',
                name='Cumulative Sum',
                line=dict(color='blue', width=2)
            ))
            
            fig_line.update_layout(
                title='Cumulative Sum from 1 to n',
                xaxis_title='Number',
                yaxis_title='Cumulative Sum',
                showlegend=True
            )
            
            st.plotly_chart(fig_line, use_container_width=True)
        
        # Comparison with different values of n
        st.subheader("Sum Growth Pattern")
        
        # Generate data for different values of n
        n_values = list(range(1, min(n + 1, 101)))
        sum_values = [sum_using_formula(i) for i in n_values]
        
        fig_growth = go.Figure()
        fig_growth.add_trace(go.Scatter(
            x=n_values,
            y=sum_values,
            mode='lines+markers',
            name='Sum = n(n+1)/2',
            line=dict(color='red', width=2)
        ))
        
        fig_growth.update_layout(
            title='Sum Growth Pattern (Quadratic Growth)',
            xaxis_title='n',
            yaxis_title='Sum (1 to n)',
            showlegend=True
        )
        
        st.plotly_chart(fig_growth, use_container_width=True)
    
    # Educational section
    st.subheader("About the Methods")
    
    with st.expander("Method Explanations"):
        st.markdown("""
        **1. For Loop Method:**
        ```python
        total = 0
        for i in range(1, n + 1):
            total += i
        ```
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        - Iterates through each number and adds to total
        
        **2. While Loop Method:**
        ```python
        total = 0
        i = 1
        while i <= n:
            total += i
            i += 1
        ```
        - Time Complexity: O(n)
        - Space Complexity: O(1)
        - Similar to for loop but uses while condition
        
        **3. Mathematical Formula:**
        ```python
        return n * (n + 1) // 2
        ```
        - Time Complexity: O(1)
        - Space Complexity: O(1)
        - Direct calculation using Gauss's formula
        
        **4. Recursion Method:**
        ```python
        if n <= 1:
            return n
        return n + sum_using_recursion(n - 1)
        ```
        - Time Complexity: O(n)
        - Space Complexity: O(n) due to call stack
        - Recursive approach (limited to small n)
        """)
    
    with st.expander("Mathematical Background"):
        st.markdown("""
        The sum of first n natural numbers can be calculated using the formula:
        
        **Sum = n(n+1)/2**
        
        This formula was discovered by Carl Friedrich Gauss as a young student.
        
        **Proof:**
        - Let S = 1 + 2 + 3 + ... + n
        - Also S = n + (n-1) + (n-2) + ... + 1
        - Adding both: 2S = (n+1) + (n+1) + ... + (n+1) [n times]
        - Therefore: 2S = n(n+1)
        - So: S = n(n+1)/2
        """)
    
    # Examples section
    st.subheader("Common Examples")
    
    examples = [
        (10, "Small number"),
        (100, "Medium number"),
        (1000, "Large number"),
        (5050, "Famous example (sum 1 to 100 = 5050)")
    ]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Quick Examples:**")
        for example_n, description in examples:
            if example_n <= 5050:
                result = sum_using_formula(example_n)
                st.write(f"n = {example_n} ({description}): {result:,}")
    
    with col2:
        st.write("**Pattern Recognition:**")
        st.write("- Sum of 1 to 1 = 1")
        st.write("- Sum of 1 to 2 = 3")
        st.write("- Sum of 1 to 3 = 6")
        st.write("- Sum of 1 to 4 = 10")
        st.write("- Sum of 1 to 5 = 15")
        st.write("- Pattern: 1, 3, 6, 10, 15... (Triangular numbers)")

if __name__ == "__main__":
    main()