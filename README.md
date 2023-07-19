Based on the requirements, here are the core classes, functions, and methods that will be necessary:

1. `app.py` (Entrypoint file)
   - `generate_cover_prompt(plot)`: Generates a cover prompt based on the book's plot using OpenAI's ChatCompletion API.
   - `create_cover_image(plot)`: Creates a cover image based on the provided plot using the Stability AI API.
   - `create_epub(title, author, chapters, cover_image_path='cover.png')`: Creates an EPUB book file with the given title, author, chapters, and cover image.

2. `utils.py`
   - `print_step_costs(response, model)`: Prints the step costs for the OpenAI models.
   - `generate_plots(prompt)`: Generates fantasy novel plots based on a given prompt using OpenAI's ChatCompletion API.
   - `select_most_engaging(plots)`: Selects the most engaging plot from a list of generated plots using OpenAI's ChatCompletion API.
   - `improve_plot(plot)`: Improves a given plot using OpenAI's ChatCompletion API.
   - `get_title(plot)`: Generates a title for a given plot using OpenAI's ChatCompletion API.
   - `write_first_chapter(plot, first_chapter_title, writing_style)`: Writes the first chapter of a novel based on the plot, first chapter title, and writing style using OpenAI's ChatCompletion API.
   - `write_chapter(previous_chapters, plot, chapter_title)`: Writes the next chapter of a novel based on the previous chapters, plot, and chapter title using OpenAI's ChatCompletion API.
   - `generate_storyline(prompt, num_chapters)`: Generates a storyline with chapters and high-level details for a fantasy novel based on a given prompt and number of chapters using OpenAI's ChatCompletion API.
   - `write_to_file(prompt, content)`: Writes the output for a given prompt to a file.

3. `website.html` (Static HTML file)
   - Contains the HTML structure and input fields for the website.

4. `styles.css` (Static CSS file)
   - Contains the CSS styles for the website.

5. `script.js` (Static JavaScript file)
   - Contains the JavaScript code to handle user input and interaction on the website.

Now, let's output the content of each file:

`app.py`
