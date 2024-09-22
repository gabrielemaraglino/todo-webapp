# Minimalistic Todo-App

A simple, web-based to-do list application built using Python and Streamlit. This app allows users to manage tasks in a minimalistic interface, improving productivity through a simple task-tracking system.

**Live Demo**: You can try the live app [here](https://gabrielemaraglino-todo-webapp-web-ktyohu.streamlit.app/).

## Features

- Add new tasks to your to-do list
- Remove completed tasks by checking them off
- Data persistence through `todos.txt`, ensuring tasks are saved across sessions
- Minimalistic and easy-to-use interface

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/minimalistic-todo-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd minimalistic-todo-app
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the application:
    ```bash
    streamlit run web.py
    ```

## Usage

Once the app is running (locally or via the deployed version), you can interact with it through a browser window:

- **Add a Task**: Use the input field to add a new task to your list.
- **Complete a Task**: Check off a task to remove it from the list.

The app is designed to help you stay organized with a simple, distraction-free interface.

## File Structure

- **`web.py`**: The main Streamlit app file. Handles the UI and interaction logic.
- **`functions.py`**: Contains helper functions for reading and writing tasks to a `todos.txt` file.
- **`todos.txt`**: The file used to store the to-do items. Automatically created if not present.



