# Smart Device Guide
## Overview

This project predicts the price of a device (laptop or mobile phone) based on user-provided specifications. After predicting the price, it offers tailored recommendations within the user's budget and suggests devices that closely match the user's requirements. 

Additionally, a chatbot is integrated to provide users with flexible assistance and support by fetching relevant information from the database. 

## **Demo**:  
<p align="center">
  <img src="Screenshots/Screenshot 2024-12-20 153356.png" alt="Screenshot 1" width="45%">
  <img src="Screenshots/Screenshot 2024-12-20 154307.png" alt="Screenshot 2" width="45%">
</p>
<p align="center">
  <img src="Research/Screenshot 2024-12-01 144139.png" alt="Screenshot 1" width="45%">
  <img src="Research/Screenshot 2024-12-01 144216.png" alt="Screenshot 2" width="45%">
</p>

## `pyprik`

PyPi LINK : https://pypi.org/project/pyprik/

<h2>Install the Package</h2>
<pre>
<code id="install-command" style="font-size: 55px;">pip install pyprik</code>
</pre>

<p align="center">
  <img src="Research/Screenshot 2024-12-01 144717.png" alt="Screenshot 1" >
</p>

##Retrieval-Augmented Generation (RAG)

In this project, we implemented a **Retrieval-Augmented Generation (RAG)** chatbot to provide users with a conversational interface for enhanced flexibility and assistance. RAG combines the strengths of retrieval-based models and generative models to deliver accurate and contextually relevant responses. It retrieves relevant information from a knowledge base or document store and uses a generative model to craft coherent responses based on the retrieved content.


---

### RAG in the Chatbot

1. **Enhanced User Assistance**:  
   The chatbot fetches relevant device specifications and recommendations from a database, allowing users to make informed decisions based on real-time data.

2. **Conversational Recommendations**:  
   It provides tailored suggestions for devices that fit the user's budget and preferences through natural, conversational interactions.

3. **Dynamic Knowledge Integration**:  
   By converting the dataset into a document format and using a vector database, the chatbot can retrieve relevant information and generate accurate responses even as the dataset updates.

---
<p align="center">
  <img src="Screenshots/Screenshot 2024-12-26 211023.png" alt="Screenshot 1" >
</p>
### Steps

- **Data Preprocessing and Conversion**:  
   - The data was transformed into **document format** to ensure compatibility with retrieval systems. 
   - Each document represents a structured segment of the knowledge base, making it easy to query and retrieve relevant information.

- **Embedding Generation**:  
   - We used **Hugging Face embeddings** to convert textual data into high-dimensional vector representations. 
   - These embeddings capture the semantic meaning of the text, allowing for efficient similarity searches.

- **Vector Database**:  
   - **AstraDB** (powered by Cassandra) was employed as the vector database.  
   - This ensures scalable, high-performance storage and retrieval of vectorized documents. The vector database allows efficient querying for similar documents based on the user's input.

- **Model Integration with GROQ API**:  
   - To generate conversational responses, the chatbot leverages a pre-trained generative model accessed via the **GROQ API**.
   - The generative model takes the retrieved documents and crafts contextually appropriate and coherent responses.

- **Conversational Chatbot**:  
   - A fully conversational chatbot was developed to handle dynamic queries from users.  
   - The chatbot seamlessly integrates RAG to retrieve and generate responses, providing personalized assistance and enhancing user engagement.

---
