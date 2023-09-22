# ReadMe - Running the Application

This ReadMe file provides instructions on how to set up and run the application using the provided commands. The application utilizes Python and various libraries to perform its functions. Please follow the steps below to get the application up and running.

## Prerequisites

Before running the application, ensure you have the following prerequisites installed on your system:

1. **Python**: Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **pip**: Pip is a package manager for Python. It is usually included with Python installation. You can check if it's installed by running `pip --version` in your command prompt or terminal.

## Installation Steps

Follow these steps to set up and run the application:

### 1. Create a Virtual Environment

We recommend creating a virtual environment to manage the application's dependencies. This ensures that the application's dependencies do not interfere with your system-wide Python packages.

```shell
pip3 install virtualenv
python -m virtualenv env
```

### 2. Activate the Virtual Environment (Windows)

Activate the virtual environment using the following command if you are using Windows:

```shell
.\env\Scripts\activate.ps1
```

### 3. Install Required Packages

Use `pip` to install the necessary Python packages:

```shell
pip install openai
pip install python-dotenv
pip install openai
```

### 4. Run the Application

Now that you have set up the virtual environment and installed the required packages, you can run the application. Make sure you are still within the virtual environment.

```shell
python .\clean_conversation.py
python app.py
```

The first command runs the `clean_conversation.py` script, and the second command runs the `app.py` script, which presumably starts the application.

## Note

- If you encounter any errors related to missing packages or dependencies, ensure that you have correctly activated the virtual environment and installed the packages within it.

- Make sure your system meets the minimum requirements for running the application, and you have the necessary permissions to execute the provided commands.

- If you have any specific configuration or environment variables required for the application, please refer to the application's documentation or consult with the developer.

With these steps, you should be able to set up and run the application successfully. If you encounter any issues or need further assistance, please consult the application's documentation or seek help from the developer or community support.