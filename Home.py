import streamlit as st
import streamlit.components.v1 as components

# Define the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Onboarding Page</title>
    <style>
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #0E1117;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: #0E1117;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            max-width: 900px;
            width: 90%;
            color: #fff;
            text-align: center;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            color: #ffffff; /* Sky blue color */
        }
        .header p {
            font-size: 1.2em;
            color: #CCC;
        }
        .features {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-top: 30px;
        }
        .feature {
            background: #353942;
            padding: 20px;
            border-radius: 10px;
            transition: transform 0.3s, background-color 0.3s;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .feature:hover {
            transform: translateY(-10px);
            background-color: #333;
        }
        .feature h2 {
            margin-top: 0;
            font-size: 1.5em;
            color: #ffffff; /* Sky blue color */
        }
        .feature p {
            font-size: 1em;
            color: #AAA;
            margin: 0;
        }
        a {
            text-decoration: none;
            color: inherit;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Welcome to the Researcher</h1>
        </div>
        <div class="features">
            <div class="feature">
                <h2>Brainstorming</h2>
                <p>Generate creative research ideas based on keywords.</p>
            </div>
            <div class="feature">
                <h2>Data Analysis</h2>
                <p>Analyze complex datasets through natural language commands.</p>
            </div>
            <div class="feature">
                <h2>Data Visualization</h2>
                <p>Manipulate data visualizations in real time using natural language.</p>
            </div>
            <div class="feature">
                <h2>Mind Mapper</h2>
                <p>Transform Your PDFs into Dynamic Mind Maps</p>
            </div>
            <div class="feature">
                <h2>Multilingual Translation</h2>
                <p>Translate research content to foster international collaboration.</p>
            </div>
            <div class="feature">
                <h2>PDF Analyser</h2>
                <p>Seamlessly Transform your PDFs into Insightful Content.</p>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Render the HTML in Streamlit
components.html(html_content, height=800, width=800)
