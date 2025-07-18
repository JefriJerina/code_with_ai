from playwright.sync_api import sync_playwright
import time

def determine_age_category(age):
    """
    Determine age category based on age input
    
    Categories:
    - Child: 0-12 years
    - Teenager: 13-19 years
    - Adult: 20-64 years
    - Senior: 65+ years
    """
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 64:
        return "Adult"
    else:
        return "Senior"

def create_age_category_html():
    """Create HTML content for age category determination"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Age Category Determiner</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
                text-align: center;
                margin-bottom: 30px;
            }
            .input-group {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
                color: #555;
            }
            input[type="number"] {
                width: 100%;
                padding: 10px;
                border: 2px solid #ddd;
                border-radius: 5px;
                font-size: 16px;
                box-sizing: border-box;
            }
            button {
                background-color: #007bff;
                color: white;
                padding: 12px 30px;
                border: none;
                border-radius: 5px;
                font-size: 16px;
                cursor: pointer;
                width: 100%;
                margin-top: 10px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 5px;
                text-align: center;
                font-size: 18px;
                font-weight: bold;
                min-height: 20px;
            }
            .child { background-color: #e8f5e8; color: #2e7d32; }
            .teenager { background-color: #e3f2fd; color: #1976d2; }
            .adult { background-color: #fff3e0; color: #f57c00; }
            .senior { background-color: #fce4ec; color: #c2185b; }
            .invalid { background-color: #ffebee; color: #d32f2f; }
            .categories {
                margin-top: 30px;
                padding: 20px;
                background-color: #f8f9fa;
                border-radius: 5px;
            }
            .categories h3 {
                margin-top: 0;
                color: #333;
            }
            .category-item {
                margin-bottom: 10px;
                padding: 8px;
                border-left: 4px solid #007bff;
                background-color: white;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Age Category Determiner</h1>
            <div class="input-group">
                <label for="age">Enter Age:</label>
                <input type="number" id="age" min="0" max="150" placeholder="Enter age in years">
            </div>
            <button onclick="determineCategory()">Determine Category</button>
            <div id="result" class="result"></div>
            
            <div class="categories">
                <h3>Age Categories:</h3>
                <div class="category-item">
                    <strong>Child:</strong> 0-12 years
                </div>
                <div class="category-item">
                    <strong>Teenager:</strong> 13-19 years
                </div>
                <div class="category-item">
                    <strong>Adult:</strong> 20-64 years
                </div>
                <div class="category-item">
                    <strong>Senior:</strong> 65+ years
                </div>
            </div>
        </div>

        <script>
            function determineCategory() {
                const ageInput = document.getElementById('age');
                const resultDiv = document.getElementById('result');
                const age = parseInt(ageInput.value);
                
                if (isNaN(age) || age < 0) {
                    resultDiv.textContent = 'Please enter a valid age (0 or greater)';
                    resultDiv.className = 'result invalid';
                    return;
                }
                
                let category;
                let className;
                
                if (age <= 12) {
                    category = 'Child';
                    className = 'child';
                } else if (age <= 19) {
                    category = 'Teenager';
                    className = 'teenager';
                } else if (age <= 64) {
                    category = 'Adult';
                    className = 'adult';
                } else {
                    category = 'Senior';
                    className = 'senior';
                }
                
                resultDiv.textContent = `Age ${age} is categorized as: ${category}`;
                resultDiv.className = `result ${className}`;
            }
            
            // Allow Enter key to trigger calculation
            document.getElementById('age').addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    determineCategory();
                }
            });
        </script>
    </body>
    </html>
    """
    return html_content

def run_age_category_app():
    """Run the age category application using Playwright"""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Create and serve HTML content
        html_content = create_age_category_html()
        page.set_content(html_content)
        
        print("Age Category Determiner is running...")
        print("The application will demonstrate automated testing of different age inputs")
        print("Press Ctrl+C to stop the application")
        
        try:
            # Demonstrate automated testing with different ages
            test_ages = [5, 16, 25, 70, -1, 150]
            
            for age in test_ages:
                print(f"\nTesting age: {age}")
                
                # Clear previous input
                page.fill('#age', '')
                
                # Enter age
                page.fill('#age', str(age))
                
                # Click determine button
                page.click('button')
                
                # Wait for result
                time.sleep(1)
                
                # Get result text
                result_text = page.locator('#result').inner_text()
                print(f"Result: {result_text}")
                
                # Also test with Python function
                py_result = determine_age_category(age)
                print(f"Python function result: {py_result}")
                
                time.sleep(2)
            
            print("\nAutomated testing completed!")
            print("You can now manually test the application.")
            print("Press Ctrl+C to close the browser")
            
            # Keep browser open for manual testing
            while True:
                time.sleep(1)
                
        except KeyboardInterrupt:
            print("\nClosing application...")
        finally:
            browser.close()

def test_age_categories():
    """Test the age category function with various inputs"""
    test_cases = [
        (0, "Child"),
        (5, "Child"),
        (12, "Child"),
        (13, "Teenager"),
        (16, "Teenager"),
        (19, "Teenager"),
        (20, "Adult"),
        (35, "Adult"),
        (64, "Adult"),
        (65, "Senior"),
        (80, "Senior"),
        (100, "Senior"),
        (-1, "Invalid age")
    ]
    
    print("Testing age category function:")
    print("-" * 40)
    
    for age, expected in test_cases:
        result = determine_age_category(age)
        status = "✓" if result == expected else "✗"
        print(f"{status} Age {age:3d}: {result:12s} (Expected: {expected})")

if __name__ == "__main__":
    print("Age Category Determiner")
    print("=" * 30)
    
    # Run tests first
    test_age_categories()
    
    print("\n" + "=" * 50)
    print("Starting Playwright application...")
    print("=" * 50)
    
    # Run the Playwright application
    run_age_category_app()