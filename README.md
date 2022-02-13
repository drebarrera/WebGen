<h1 align="center">WebGen</h1>
WebGen is a custom Python to User Interface compiler with the goal of making website and app design cleaner and more efficient.  WebGen uses Python classes to represent HTML elements, creating repeated structures much more reliably than copy/paste. Javascript, CSS, and PHP global files can be created and linked to pages, giving creators the ability to use the same pieces of code on every site. WebGen operates much more effectively than programming from scratch in HTML, while still presenting the customizable flexibility of creating a website through code. Created by <a href="https://www.drebarrera.com" target="_blank">Dre Barrera</a>.

<h2>Setting Up WebGen</h2>
All that is necessary to get started is to download this repository! No imported libraries necessary! There are three key files necessary to run WebGen: main.py, modules.py, and comp.py.
<ul>
<li><code>main.py</code> - This file holds the interface commands (see Programming With WebGen) used to create, organize, and export files. Run this file to start your WebGen interface and begin programming.</li>
<li><code>modules.py</code> - This file contains the modular python commands (see Programming With WebGen) used to create HTML elements with Python. To add a new custom HTML element, create a new class. Assign custom style properties, such as "position" or "background_color" (underscores are used instead of hyphens). Include a <code>c()</code> function to be called to compile the element. The <code>c()</code> function should return an HTML element as a string.</li>
<li><code>comp.py</code> - This file contains the code used to compile the Python files created in the WebGen interface into HTML. Using the <code>c()</code> functions defined in <code>modules.py</code>, the head and body of the HTML document is created, including external JavaScript, CSS, and PHP scripts.</li>
</ul>

<h2>Programming With WebGen</h2>
There are three different components to WebGen:
<ol>
<li>Interface Commands - Commands used to create, organize, and export files.</li>
<li>Modular Python Commands - Python commands used to create HTML elements and adjust style properties within files.</li>
<li>Global Programming - Programming used to implement JavaScript, CSS, and PHP into compiled webpages.</li>
</ol>

<h3>Interface Commands</h3>
Interface commands are used to create, organize, edit, delete, compile, and export files. Main Commands are used to select files, while File Commands are used when working on individual pages.
<h5>Main Commands</h5>
<ul>
<li><code>help</code> - General help command. Using this command will list the options for selection and instruction.</li>
<li><code>f(folder, filename)</code> - Open or create and open (if the file does not already exist) a file. <code>folder</code> is the project name, while <code>filename</code> is the name of the page to be created. Once opened, the WebGen interface will switch to accepting File Commands (see File Commands).</li>
<li><code>gf(folder, global_filename)</code> - Similar to <code>f(folder, filename)</code>, this command will open or create and open a global file. A global file is a file under the name <code>filename</code>, which is accessible to all of the pages within the project folder, <code>folder</code> by importing with the command <code>from global_filename import *</code> within individual Python scripts. Global files cannot be individually compiled with the <code>r</code> command (see File Commands). PHP scripts are exclusively included via global files (see FAQs).</li>
<li><code>fdir</code> - This command opens the file directory where WebGen is held.</li>
<li><code>kill(folder)</code> - The kill command is used to completely delete a project with the name <code>folder</code>. This includes all webpages, global files, and other content associated with the project. Once performed, the effects of this command are final.</li>
<li><code>exportf(folder, destination)</code> - The export command will export an entire project with the name <code>folder</code> to the file location input as <code>destination</code>. The file will be exported as a zip file. When referencing the destination path, make sure to prepend with the letter r, like so: <code>r"THIS\IS\A\PATH"</code></li>
<li><code>exit</code> - The exit command is used to exit a file and return to the WebGen interface or quit the WebGen interface and end the program.</li>
<li><code>restart</code> - The restart command is used to exit the WebGen interface and end the program.</li>
</ul>

<h5>File Commands</h5>
<ul>
<li><code>e</code> - The edit command, <code>e</code>, is used to edit the Python file used to define HTML elements. When using the edit command, a document window will be generated for Python coding. Every Python webfile requires the content generated on first use of the command (except for the comments). While the assignments <code>data</code> and <code>body</code> define the head and body elements of the HTML document, the comments, <code>### OBJECTS ###</code>, <code>### CONTENT ###</code>, <code>### PROPERTIES ###</code> are used to structure your code. See more below:</li>
<ul>
<li><code>### OBJECTS ###</code> - The Objects section is typically used to define the modular assignments used within the Python script. For example, <code>nav = mx.C()</code> defines a Container object referred to as <code>nav</code> and would be written in this section.</li>
<li><code>### CONTENT ###</code> - The Content section is typically where object content is assigned. Continuing from the previous example, this section would be where we would apply the code <code>body.content = [nav]</code>, placing the <code>nav</code> container within the <code>body</code> element of the page.</li>
<li><code>### PROPERTIES ###</code> - The Properties section is typically where object style properties is assigned. Continuing from the previous examples, this section would include statements such as <code>nav.background_color = "red"</code> where the style of the <code>nav</code> container includes a red background color.</li>
</ul>
<li><code>css</code> - The CSS command creates a css document to be automatically linked to the HTML page generated by the Python document. If the Python document associated with the CSS document is a global file, the global file must be imported to the main file to use the global file with the command <code>from global_filename import *</code>. (do not include file extensions)</li>
<li><code>js</code> - The JavaScript command creates a JavaScript document to be automatically linked to the HTML page generated by the Python document. If the Python document associated with the JavaScript document is a global file, the global file must be imported to the main file to use the global file with the command <code>from global_filename import *</code>. (do not include file extensions)</li>
<li><code>php</code> - The PHP command creates a PHP document associated exclusively with global files. Because the PHP document is associated with a global file, the global file must be imported to the main file to use the global file with the command <code>from global_filename import *</code> (do not include file extensions).</li>
<li><code>fdir</code> - This command opens the file directory where the project operated on is held.</li>
<li><code>images</code> - This command opens or creates and opens (if the file doesn't already exist) the file directory where images and other media elements are stored for developmental use. Use the source url "../images/image_name.jpg" to add media to elements within a Python or CSS file.</li>
<li><code>lgf</code> - This command lists all global files associated with the given project. In order to add a global file to a given webpage, use the code <code>from global_filename import *</code> in the Python document.</li>
<li><code>lm</code> - This command lists all object classes to create HTML element with Python. Classes should be prepended with <code>mx.</code> in Python files to reference the imported module file. For example, creating a text element would be done within a Python document with the code <code>text_elem = mx.T()</code>.</li>
<li><code>mod m</code> - This command lists all the default object properties associated with class <code>m</code>. To change a property's value, simply reassign the property for the given object assignment. For example, given a text element, <code>text_elem = mx.T()</code>, changing its color would be done with <code>text_elem.color = "red"</code>. Properties using hyphenation, such as <code>background-color</code> replace the hyphen with an underscore in Python scripts (ie. <code>background_color</code>).</li>
<li><code>r</code> - The refresh command, <code>r</code> compiles the Python document along with its dependencies and opens the compiled HTML webpage in a browser. This command is used to refresh the browser page when changes have been made to the Python document or its dependencies. Note: If a global file is changed, use the commands <code>import importlib</code> and <code>importlib.reload(sys.modules['global_filename'])</code> to reload global files without having to restart WebGen after each change.</li>
<li><code>kill</code> - The kill command is used to delete the webpage or global file being operated on. This does not include the global files imported to the page, but will remove the JavaScript, CSS, or PHP files directly linked to the Python document deleted. Once performed, the effects of this command are final.</li>
<li><code>export(destination)</code> - The export command will export the webpage operated on to the file location input as <code>destination</code>. The file will be exported as a zip file.</li>
<li><code>exit</code> - The exit command is used to exit a file and return to the WebGen interface or quit the WebGen interface and end the program.</li>
<li><code>restart</code> - The restart command is used to exit the WebGen interface and end the program.</li>
</ul>

<h3>Modular Commands</h3>
Modular commands refer the Python commands used to define objects and their properties. To find the modules offered by <code>modules.py</code> and the properties of said modules, use the <code>lm</code> and <code>mod m</code> commands in the WebGen interface (see File Commands above). To assign an object, follow the steps below:
<ol>
<li><code>container_elem = mx.C()</code> - Object assignment is done by assigning a variable to a class (in this example the container class, <code>C()</code>, is used). Remember to prepend the class with <code>mx.</code> to declare the object as an imported module class.</li>
<li><code>container_elem.content = [text_elem]</code> - Content assignment is done by two different methods: For container classes such as <code>C()</code> and <code>Table()</code>, the objects stored within the containers are stored within lists and are in object form (in this example, text_elem is an object within container_elem). For text-based elements, such as <code>T()</code>, the content refers to text (ie. <code> text_elem.content = "This is text"</code>).</li>
<li><code>container_elem.text_align = "center"</code> - Property assignment is done by assigning values to the style properties desired. Note that properties using hyphenation, such as <code>text-align</code> replace the hyphen with an underscore in Python scripts (ie. <code>text_align</code>). Some properties have defaults which may be overriden by reassignment. Properties such as <code>margin</code>, <code>padding</code>, and <code>width</code> are considered Dynamic Properites because they typically vary by viewport dimensions. Because style properties are fixed and cannot be adjusted with CSS after being set, Dynamic Properties are restricted from being set with style properties, but instead must be adjusted with CSS or JavaScript code.</li>
</ol>

<h5>Featured Classes</h5>
<ul>
<li><code>mx.Data()</code> - The Data element provides the different components and metadata used in the <code>head</code> element of the webpage.</li>
<ul>

  <li><code>data.title</code> - The title of the webpage.</li>
  <li><code>data.charset</code> - The charset metadata of the webpage. Default is "utf-8".</li>
  <li><code>data.description</code> - The description metadata of the webpage.</li>
  <li><code>data.keywords</code> - The keyword metadata of the webpage. List your keywords within a list: <code>data.keywords = ['these','are','keywords']</code></li>
  <li><code>data.author</code> - The author metadata of the webpage.</li>
  <li><code>data.viewport</code> - The viewport metadata of the webpage. Default is "width=device-width, initial-scale=1".</li>
  <li><code>data.jquery_script</code> - The jquery_script property enables the use of the jQuery source file imported from the WebGen directory. Default is True. To disable, reassign to False.</li>
  <li><code>data.jquery_ui_script</code> - The jquery_ui_script property enables the use of the jQuery-UI source file imported from the WebGen directory. Default is True. To disable, reassign to False.</li>
  <li><code>data.scripts</code> - The scripts property contains a list of imported scripts via source URLs. List the imported script locations like so: <code>data.scripts = ['script1_location','script2_location']</code>.</li>
</ul>
  <p></p>
<li><code>mx.Body()</code> - The Body element allows for the adjustment of the style properties and content of the <code>body</code> element of the webpage.</li>
<ul>

  <li><code>body.background_color</code> - The background color of the webpage. Default is "#ffffff".</li>
  <li><code>body.overflow_x</code> - The overflow-x property of the webpage. Default is "hidden".</li>
  <li><code>body.font_family</code> - The font-family property of the webpage. Default is "Helvetica".</li>
  <li><code>body.color</code> - The color property of the webpage. Default is "black".</li>
  <li><code>body.content</code> - The content of the webpage. Body is a container object, meaning that all content should also be objects, listed in order of priority like so: <code>body.content = [element1, element2, element3]</code>.</li>
</ul>
  <p></p>
<li><code>mx.T()</code> - The Text element generates paragraph, heading, and other text content.</li>
<ul>

  <li><code>text_elem.type</code> - The text tag represented by the element. Default is a paragraph tag, "p", but can be reassigned to "h1", "em", or other tags.</li>
  <li><code>text_elem.id</code> - The ID HTML attribute.</li>
  <li><code>text_elem.cl</code> - The Class HTML attribute.</li>
  <li><code>text_elem.content</code> - The content of the text element. Text element content is a string and can be assigned like so: <code>text_elem.content = "This is text content"</code>.</li>
</ul>
 <p></p>
<li><code>mx.Link()</code> - The Link element generates a link container around other object content.</li>
<ul>

  <li><code>link_elem.src</code> - The href source of the link. Assign a URL to this property.</li>
  <li><code>link_elem.id</code> - The ID HTML attribute.</li>
  <li><code>link_elem.cl</code> - The Class HTML attribute.</li>
  <li><code>link_elem.content</code> - The content of the link element. Link element content is a list of objects wrapped by the link like so: <code>link_elem.content = [element1, element2]</code>.</li>
</ul>
  
 <p></p>
<li><code>mx.C()</code> - The Container element generates a div container with other object content.</li>
<ul>
  <li><code>container_elem.id</code> - The ID HTML attribute.</li>
  <li><code>container_elem.cl</code> - The Class HTML attribute.</li>
  <li><code>container_elem.onclick</code> - The onclick event HTML attribute.</li>
  <li><code>container_elem.onhover</code> - The onhover event HTML attribute.</li>
  <li><code>container_elem.attr</code> - This property serves to define a custom HTML attribute.</li>
  <li><code>container_elem.background_color</code> - The background color of the container. Default is "lightblue" for visibility and identification. To override for CSS adjustment, reassign to <code>container_elem.background_color = ""</code>.</li>
  <li><code>container_elem.overflow_x</code> - The overflow-x property of the container. Default is "visible".</li>
  <li><code>container_elem.overflow_y</code> - The overflow-y property of the container. Default is "visible".</li>
  <li><code>container_elem.content</code> - The content of the container element. Container element content is a list of objects wrapped by the container like so: <code>container_elem.content = [element1, element2]</code>.</li>
</ul>
  
<p></p>
<li><code>mx.Table()</code> - The Table element generates a table with cells defined by nested lists.</li>
<ul>
  <li><code>table_elem.id</code> - The ID HTML attribute. When assigned an ID, the cells of the Table will also assume the same ID with the appended "_rowNumber_columnNumber". The default ID is "#table". Thus, row 2, column 4 will have the ID "#table_2_4" unless the ID is adjusted.</li>
  <li><code>table_elem.cl</code> - The Class HTML attribute. Default is ".table".</li>
  <li><code>table_elem.background_color</code> - The background color of the table. Default is "coral" for visibility and identification. To override for CSS adjustment, reassign to <code>table_elem.background_color = ""</code>.</li>
  <li><code>table_elem.content</code> - The content of the table element. Table element content is generated by a nested list of objects wrapped by the table like so: <code>table_elem.content = [[row1_col1_content, row1_col2_content, row1_col3_content], [row2_col1_content, row2_col2_content, row2_col3_content]]</code>.</li>
</ul>
</ul>

<h2>FAQs</h2>
<ul>
<li>Why is my content not showing on my compiled webpage?</li>
<p>If you are having a hard time seeing your content appear on your compiled webpage after using the <code>r</code> command, make sure that the desired elements have been added as content within the <code>body</code> element of the webpage or another embedded container element. Elements must be embedded in order to be properly compiled: <code>container_elem.content = [element]</code>.</p>
<li>How do I create a PHP webpage?</li>
<p>To create a PHP page, simply create a normal file with the Interface Command <code>f(folder, filename)</code> and add the HTML components (forms, containers, etc.) of the webpage. Then, use the <code>exit</code> command to return to the main interface and create a global file with the <code>gf(folder, global_filename)</code> command. Instead of using the <code>e</code> command to edit the HTML elements (forms, containers, etc.) of the page, use the <code>php</code> File Command to add PHP content. No enclosing PHP tags are needed - just start programming your PHP content.</p>
</ul>
