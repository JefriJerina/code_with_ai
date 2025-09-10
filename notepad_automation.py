from flask import Flask, request, jsonify
import pyautogui
import subprocess
import time
import os

app = Flask(__name__)

# Configuration
folder_path = r"C:\Users\nelso\OneDrive\Desktop\UI_AUTOMATION_N8N"
file_name = "demoai.txt"
file_path = os.path.join(folder_path, file_name)

@app.route('/write-message', methods=['POST'])
def write_message():
    data = request.get_json()

    if not data or 'message' not in data:
        return jsonify({"error": "Missing 'message' in request body"}), 400

    user_input = data['message']

    try:
        # Launch Notepad
        subprocess.Popen(["notepad.exe"])
        time.sleep(1.5)

        # Case 1: File Exists
        if os.path.exists(file_path):
            pyautogui.hotkey('ctrl', 'o')
            time.sleep(1.2)

            pyautogui.typewrite(file_path)
            pyautogui.press('enter')
            time.sleep(1.5)

            pyautogui.hotkey('ctrl', 'end')
            pyautogui.press('enter')
            pyautogui.typewrite(user_input)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 's')

        # Case 2: File Doesn't Exist
        else:
            pyautogui.typewrite(user_input)
            time.sleep(0.3)
            pyautogui.hotkey('ctrl', 's')
            time.sleep(1.2)

            pyautogui.typewrite(file_path)
            pyautogui.press('enter')

        return jsonify({
            "status": "success",
            "message": "File saved or updated successfully",
            "file_path": file_path
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
