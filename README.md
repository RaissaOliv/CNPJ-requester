# About the project
  CNPJ-requester is a simple personal project which takes a CNPJ from user input and tries to find it in the receitaws api, a webservice for CNPJ search. Before the search, the code treats the user input, leaving only numbers on it, and checks if it is a valid cnpj before actually doing an api request (ex: checks if the cnpj is too short)

# Prerequisites

- python

# Running the project
<h3>clone the repository</h3>
  <p><code>gh repo clone RaissaOliv/CNPJ-requester</code></p>
  
<h3>Go to folder</h3>
<p><code>cd CNPJ-requester</code></p>

<h3>Install python requests library</h3>
<p><code>python -m pip install requests</code></p>
<h3>Run the code</h3>
<p><code> python main.py </code></p>
