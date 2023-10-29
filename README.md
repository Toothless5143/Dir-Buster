# Description:
Dir Buster is a Python-based command-line tool designed to discover hidden directories on a target website by systematically testing a list of common directory names. It leverages the power of the `requests` library to send HTTP GET requests to different directory paths and checks the response status code for successful matches. This tool helps in identifying potentially vulnerable or unprotected directories that may exist on a web server.

# Installation:
1. Ensure that Python is installed on your system (version 3 or higher).
2. Install the `requests` library by running the following command in your terminal:
   ```
   pip install requests
   ```
3. Download or clone the Simple Directory Buster tool from the GitHub repository.
   ```
   git clone https://github.com/Toothless5143/Dir-Buster.git
   cd Dir-Buster
   ```

# Usage:
1. Open a terminal or command prompt.
2. Navigate to the directory where the tool is located.
3. Run the tool using the following command:
   ```
   python dir_buster.py -u <target_url> -w <wordlist_file>
   ```
   Replace `<target_url>` with the URL of the website you want to scan and `<wordlist_file>` with the path to your wordlist file.
4. The tool will systematically test each directory name from the wordlist against the target URL and display any discovered directories.

Features:
1. Command-line Interface: The tool provides a simple command-line interface to specify the target URL and wordlist file.
2. Customization: Users can easily modify the target URL and wordlist file without modifying the script itself.
3. Wordlist-based Testing: The tool tests a list of common directory names from the wordlist file, allowing users to easily customize and expand the list as needed.
4. HTTP Request Handling: It uses the `requests` library to send HTTP GET requests to different directory paths and captures the response status codes.
5. Result Display: The tool prints a message whenever it discovers a directory, indicating the specific directory path that was found.
6. Fast and Lightweight: The tool is implemented in Python and optimized for efficiency, making it fast and lightweight.

Note: It is essential to use this tool responsibly and ensure that you have proper authorization and permission before scanning any website. Unauthorized scanning or testing of websites or systems is illegal and unethical. Always obtain the necessary authorization and adhere to legal guidelines and ethical practices.


# License:
This tool is open source and available under the [MIT License.](/LICENSE)
