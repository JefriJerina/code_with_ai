import streamlit as st

def calculate_grade_average(scores):
    """Calculate the average of test scores"""
    return sum(scores) / len(scores)

def determine_pass_fail(average, passing_grade=60):
    """Determine if student passes or fails based on average"""
    return "PASS" if average >= passing_grade else "FAIL"

def main():
    st.title("📊 Grade Average Calculator")
    st.write("Enter your 5 test scores to calculate your average and determine pass/fail status.")
    
    # Create input fields for 5 test scores
    st.subheader("Enter Test Scores")
    
    col1, col2 = st.columns(2)
    
    with col1:
        score1 = st.number_input("Test 1 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        score2 = st.number_input("Test 2 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        score3 = st.number_input("Test 3 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
    with col2:
        score4 = st.number_input("Test 4 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
        score5 = st.number_input("Test 5 Score", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
    
    # Passing grade threshold
    st.subheader("Passing Grade Settings")
    passing_grade = st.slider("Passing Grade Threshold", min_value=0, max_value=100, value=60, step=1)
    
    # Calculate button
    if st.button("Calculate Average", type="primary"):
        scores = [score1, score2, score3, score4, score5]
        
        # Display individual scores
        st.subheader("📋 Test Scores Summary")
        for i, score in enumerate(scores, 1):
            st.write(f"Test {i}: {score:.1f}")
        
        # Calculate average
        average = calculate_grade_average(scores)
        
        # Determine pass/fail
        result = determine_pass_fail(average, passing_grade)
        
        # Display results
        st.subheader("📈 Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Average Score", f"{average:.2f}")
        
        with col2:
            st.metric("Passing Grade", f"{passing_grade}")
        
        with col3:
            if result == "PASS":
                st.success(f"✅ {result}")
            else:
                st.error(f"❌ {result}")
        
        # Progress bar
        st.subheader("📊 Grade Visualization")
        progress_value = min(average / 100, 1.0)
        st.progress(progress_value)
        
        # Additional feedback
        if result == "PASS":
            if average >= 90:
                st.balloons()
                st.success("🎉 Excellent work! You achieved an A grade!")
            elif average >= 80:
                st.success("👏 Great job! You achieved a B grade!")
            else:
                st.success("👍 Good work! You passed the course!")
        else:
            points_needed = passing_grade - average
            st.warning(f"You need {points_needed:.2f} more points to pass.")
            st.info("💡 Consider reviewing the material and retaking some tests if possible.")
    
    # Display grade scale
    st.subheader("📚 Grade Scale Reference")
    grade_scale = {
        "A": "90-100",
        "B": "80-89",
        "C": "70-79",
        "D": "60-69",
        "F": "Below 60"
    }
    
    cols = st.columns(len(grade_scale))
    for i, (grade, range_val) in enumerate(grade_scale.items()):
        with cols[i]:
            st.metric(f"Grade {grade}", range_val)

if __name__ == "__main__":
    main()