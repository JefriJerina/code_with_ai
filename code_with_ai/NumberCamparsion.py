from playwright.sync_api import sync_playwright
import time

def compare_numbers(num1, num2):
    """Compare two numbers and return the result"""
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 < num2:
        return f"{num1} is less than {num2}"
    else:
        return f"{num1} is equal to {num2}"

def create_html_page():
    """Create HTML content for the number comparison page"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Number Comparison Tool</title>
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
                padding: 12px 24px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
                margin-top: 10px;
            }
            button:hover {
                background-color: #0056b3;
            }
            #result {
                margin-top: 20px;
                padding: 15px;
                border-radius: 5px;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                min-height: 20px;
            }
            .result-greater {
                background-color: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
            .result-lesser {
                background-color: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
            }
            .result-equal {
                background-color: #fff3cd;
                color: #856404;
                border: 1px solid #ffeaa7;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Number Comparison Tool</h1>
            <form id="compareForm">
                <div class="input-group">
                    <label for="num1">First Number:</label>
                    <input type="number" id="num1" step="any" required>
                </div>
                <div class="input-group">
                    <label for="num2">Second Number:</label>
                    <input type="number" id="num2" step="any" required>
                </div>
                <button type="submit">Compare Numbers</button>
            </form>
            <div id="result"></div>
        </div>

        <script>
            document.getElementById('compareForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const num1 = parseFloat(document.getElementById('num1').value);
                const num2 = parseFloat(document.getElementById('num2').value);
                const resultDiv = document.getElementById('result');
                
                let result;
                let className;
                
                if (num1 > num2) {
                    result = `${num1} is greater than ${num2}`;
                    className = 'result-greater';
                } else if (num1 < num2) {
                    result = `${num1} is less than ${num2}`;
                    className = 'result-lesser';
                } else {
                    result = `${num1} is equal to ${num2}`;
                    className = 'result-equal';
                }
                
                resultDiv.textContent = result;
                resultDiv.className = className;
            });
        </script>
    </body>
    </html>
    """
    return html_content

def run_playwright_test():
    """Run Playwright automation to test the number comparison functionality"""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Set to True for headless mode
        page = browser.new_page()
        
        # Create and serve HTML content
        html_content = create_html_page()
        page.set_content(html_content)
        
        print("Number Comparison Tool launched in browser")
        print("Testing different number combinations...")
        
        # Test cases
        test_cases = [
            (10, 5),    # First number greater
            (3, 8),     # First number smaller
            (7, 7),     # Numbers equal
            (-5, 2),    # Negative and positive
            (0, 0),     # Both zero
            (3.14, 2.71)  # Decimal numbers
        ]
        
        for i, (num1, num2) in enumerate(test_cases):
            print(f"\nTest {i+1}: Comparing {num1} and {num2}")
            
            # Clear previous inputs
            page.fill('#num1', '')
            page.fill('#num2', '')
            
            # Fill in the numbers
            page.fill('#num1', str(num1))
            page.fill('#num2', str(num2))
            
            # Click compare button
            page.click('button[type="submit"]')
            
            # Wait for result and get the text
            page.wait_for_selector('#result')
            result_text = page.locator('#result').text_content()
            
            # Also get the result using our Python function
            python_result = compare_numbers(num1, num2)
            
            print(f"Browser result: {result_text}")
            print(f"Python result: {python_result}")
            print(f"Results match: {result_text == python_result}")
            
            # Small delay for demonstration
            time.sleep(2)
        
        print("\nAll tests completed!")
        print("Browser will remain open for manual testing. Close it when done.")
        
        # Keep browser open for manual interaction
        input("Press Enter to close the browser...")
        
        browser.close()

def main():
    """Main function to run the number comparison tool"""
    print("Number Comparison Tool")
    print("=" * 30)
    
    # Option 1: Run command line version
    print("\n1. Command Line Version:")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = compare_numbers(num1, num2)
        print(f"Result: {result}")
    except ValueError:
        print("Please enter valid numbers.")
    
    # Option 2: Run Playwright browser version
    print("\n2. Starting Playwright Browser Version...")
    try:
        run_playwright_test()
    except Exception as e:
        print(f"Error running Playwright: {e}")
        print("Make sure Playwright is installed: pip install playwright")
        print("Then run: playwright install")

if __name__ == "__main__":
    main()