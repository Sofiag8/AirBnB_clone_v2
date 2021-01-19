<h1 class="gap">Project 0x04. AirBnB clone - Web framework</h1>

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions&hellip;)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>

<h2>Requirements</h2>

<h3>Python Scripts</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style (version 1.7)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).__doc__)&#39;</code>)</li>
<li>All your classes should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.__doc__)&#39;</code>)</li>
<li>All your functions (inside and outside a class) should have documentation (<code>python3 -c &#39;print(__import__(&quot;my_module&quot;).my_function.__doc__)&#39;</code> and <code>python3 -c &#39;print(__import__(&quot;my_module&quot;).MyClass.my_function.__doc__)&#39;</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>

<h3>HTML/CSS Files</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file at the root of the folder of the project is mandatory</li>
<li>Your code should be W3C compliant and validate with <a href="https://github.com/holbertonschool/W3C-Validator" title="W3C-Validator" target="_blank">W3C-Validator</a> (except for jinja template)</li>
<li>All your CSS files should be in the <code>styles</code> folder</li>
<li>All your images should be in the <code>images</code> folder</li>
<li>You are not allowed to use <code>!important</code> or <code>id</code> (<code>#...</code> in the CSS file)</li>
<li>All tags must be in uppercase</li>
<li>Current screenshots have been done on <code>Chrome 56.0.2924.87</code>. </li>
<li>No cross browsers </li>
</ul>

<h2>More Info</h2>

<h3>Install Flask</h3>

<pre><code>$ pip3 install Flask
</code></pre>


<hr class="gap">
<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Hello Flask!
</h4>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

  <h4 class="task">
    1. HBNB
</h4>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

  <h4 class="task">
    2. C is fun!
</h4>
 <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo; followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

  <h4 class="task">
    3. Python is cool!
</h4>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>


  <h4 class="task">
    4. Is it a number?
</h4>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

  <h4 class="task">
    5. Number template
</h4>
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

 <h4 class="task">
    6. Odd or even?
</h4>
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display &ldquo;Hello HBNB!&rdquo;</li>
<li><code>/hbnb</code>: display &ldquo;HBNB&rdquo;</li>
<li><code>/c/&lt;text&gt;</code>: display &ldquo;C &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display &ldquo;Python &rdquo;, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is &ldquo;is cool&rdquo;</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display &ldquo;<code>n</code> is a number&rdquo; <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: &ldquo;Number: <code>n</code> is <code>even|odd</code>&rdquo; inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

  <h4 class="task">
    7. Improve engines
</h4>
  <p>Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>

<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>

<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) <a href="/rltoken/O2mDvznV40mXE9dvTT3LJw" title="tips" target="_blank">tips</a> or <code>close()</code> on the class <code>Session</code> <a href="/rltoken/Vdh9u26tfc9fObUOb9NFzw" title="tips" target="_blank">tips</a></li>
</ul>

<p>Update <code>State</code>: (<code>models/state.py</code>) - If it&rsquo;s not already present</p>

<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>

 <h4 class="task">
    8. List of states
</h4>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/fid5cMJKYMaRJqL60PlUew" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>


  <h4 class="task">
    9. Cities by states
</h4>
  <p>Write a script that starts a Flask web application</p>

 <h4 class="task">
    10. States and State
</h4>
<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: &ldquo;States&rdquo;</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/fid5cMJKYMaRJqL60PlUew" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li><code>/states/&lt;id&gt;</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li>If a <code>State</code> object is found with this <code>id</code>:

<ul>
<li><code>H1</code> tag: &ldquo;State: <state.name>&rdquo;</li>
<li><code>H3</code> tag: &ldquo;Cities:&rdquo;</li>
<li><code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li>Otherwise: 

<ul>
<li><code>H1</code> tag: &ldquo;Not found!&rdquo;</li>
</ul></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
</ul>

 <h4 class="task">
    11. HBNB filters
</h4>
 <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/hbnb_filters</code>: display a HTML page like <code>6-index.html</code>, which was done during the project <a href="/rltoken/Xls8-KeMKOReqQ8xRa6qRw" title="0x01. AirBnB clone - Web static" target="_blank">0x01. AirBnB clone - Web static</a>

<ul>
<li>Copy files <code>3-footer.css</code>, <code>3-header.css</code>, <code>4-common.css</code> and <code>6-filters.css</code> from <code>web_static/styles/</code> to the folder <code>web_flask/static/styles</code></li>
<li>Copy files <code>icon.png</code> and <code>logo.png</code> from <code>web_static/images/</code> to the folder <code>web_flask/static/images</code></li>
<li>Update <code>.popover</code> class in <code>6-filters.css</code> to allow scrolling in the popover and a max height of 300 pixels.</li>
<li>Use <code>6-index.html</code> content as source code for the template <code>10-hbnb_filters.html</code>:

<ul>
<li>Replace the content of the <code>H4</code> tag under each filter title (<code>H3</code> States and <code>H3</code> Amenities) by <code>&amp;nbsp;</code></li>
</ul></li>
<li><code>State</code>, <code>City</code> and <code>Amenity</code> objects must be loaded from <code>DBStorage</code> and <strong>sorted by name</strong> (A-&gt;Z)</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/10-hbnb_filters.sql" title="10-dump" target="_blank">10-dump</a> to have some data</li>
</ul>
