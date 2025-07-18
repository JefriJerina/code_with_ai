import streamlit as st
import re

def check_password_requirements(password):
    """
    Check if password meets basic requirements
    Returns a dictionary with requirement status
    """
    requirements = {
        'min_length': len(password) >= 8,
        'has_uppercase': bool(re.search(r'[A-Z]', password)),
        'has_lowercase': bool(re.search(r'[a-z]', password)),
        'has_digit': bool(re.search(r'\d', password)),
        'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    return requirements

def get_password_strength(requirements):
    """
    Calculate password strength based on requirements met
    """
    score = sum(requirements.values())
    
    if score <= 2:
        return "Weak", "🔴"
    elif score <= 3:
        return "Fair", "🟡"
    elif score <= 4:
        return "Good", "🟢"
    else:
        return "Strong", "🟢"

def main():
    # Page configuration
    st.set_page_config(
        page_title="Simple Password Checker",
        page_icon="🔐",
        layout="centered"
    )
    
    # Title and description
    st.title("🔐 Simple Password Checker")
    st.markdown("Check if your password meets basic security requirements")
    
    # Password input
    password = st.text_input(
        "Enter your password:",
        type="password",
        placeholder="Type your password here..."
    )
    
    # Check password if input is provided
    if password:
        requirements = check_password_requirements(password)
        strength, strength_icon = get_password_strength(requirements)
        
        # Display password strength
        st.markdown("---")
        st.subheader("Password Strength")
        st.markdown(f"### {strength_icon} {strength}")
        
        # Display requirements checklist
        st.subheader("Requirements Checklist")
        
        col1, col2 = st.columns([1, 4])
        
        with col1:
            st.markdown("✅" if requirements['min_length'] else "❌")
            st.markdown("✅" if requirements['has_uppercase'] else "❌")
            st.markdown("✅" if requirements['has_lowercase'] else "❌")
            st.markdown("✅" if requirements['has_digit'] else "❌")
            st.markdown("✅" if requirements['has_special'] else "❌")
        
        with col2:
            st.markdown("At least 8 characters")
            st.markdown("Contains uppercase letter (A-Z)")
            st.markdown("Contains lowercase letter (a-z)")
            st.markdown("Contains number (0-9)")
            st.markdown("Contains special character (!@#$%^&*)")
        
        # Progress bar
        progress = sum(requirements.values()) / len(requirements)
        st.progress(progress)
        
        # Additional feedback
        if all(requirements.values()):
            st.success("🎉 Excellent! Your password meets all requirements!")
        else:
            unmet_requirements = [req for req, met in requirements.items() if not met]
            st.warning(f"⚠️ Password needs improvement. Missing: {len(unmet_requirements)} requirement(s)")
    
    else:
        # Show instructions when no password is entered
        st.info("👆 Enter a password above to check its strength")
        
        # Display requirements info
        st.markdown("---")
        st.subheader("Password Requirements")
        st.markdown("""
        A strong password should have:
        - **Minimum 8 characters** - Longer passwords are harder to crack
        - **Uppercase letters** - Mix of capital letters (A-Z)
        - **Lowercase letters** - Mix of small letters (a-z)
        - **Numbers** - Include digits (0-9)
        - **Special characters** - Symbols like !@#$%^&*
        """)
        
        st.markdown("---")
        st.markdown("💡 **Tip**: Use a combination of words, numbers, and symbols to create a strong password!")

if __name__ == "__main__":
    main()