import openai
import random
import json
import ast

def print_step_costs(response, model):
    input = response['usage']['prompt_tokens']
    output = response['usage']['completion_tokens']

    if model == "gpt-4" or model == "gpt-4-0613":
        input_per_token = 0.00003
        output_per_token = 0.00006
    if model == "gpt-3.5-turbo-16k":
        input_per_token = 0.000003
        output_per_token = 0.000004
    if model == "gpt-4-32k-0613" or model == "gpt-4-32k":
        input_per_token = 0.00006
        output_per_token = 0.00012
    if model == "gpt-3.5-turbo" or model == "gpt-3.5-turbo-0613":
        input_per_token = 0.0000015
        output_per_token = 0.000002

    input_cost = int(input) * input_per_token
    output_cost = int(output) * output_per_token

    total_cost = input_cost + output_cost
    print('step cost:', total_cost)

def generate_plots(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a creative assistant that generates engaging fantasy novel plots."},
            {"role": "user", "content": f"Generate 10 fantasy novel plots based on this prompt: {prompt}"}
        ]
    )

    print_step_costs(response, "gpt-4-0613")

    return response['choices'][0]['message']['content'].split('\n')

def select_most_engaging(plots):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are an expert in writing fantastic fantasy novel plots."},
            {"role": "user", "content": f"Here are a number of possible plots for a new novel: {plots}\n\n--\n\nNow, write the final plot that we will go with. It can be one of these, a mix of the best elements of multiple, or something completely new and better. The most important thing is the plot should be fantastic, unique, and engaging."}
        ]
    )

    print_step_costs(response, "gpt-4-0613")

    return response['choices'][0]['message']['content']

def improve_plot(plot):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are an expert in improving and refining story plots."},
            {"role": "user", "content": f"Improve this plot: {plot}"}
        ]
    )

    print_step_costs(response, "gpt-4-0613")

    return response['choices'][0]['message']['content']

def get_title(plot):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": "You are an expert writer."},
            {"role": "user", "content": f"Here is the plot: {plot}\n\nWhat is the title of this book? Just respond with the title, do nothing else."}
        ]
    )

    print_step_costs(response, "gpt-3.5-turbo-16k")

    return response['choices'][0]['message']['content']

def write_first_chapter(plot, first_chapter_title, writing_style):
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a world-class fantasy writer."},
            {"role": "user", "content": f"Here is the high-level plot to follow: {plot}\n\nWrite the first chapter of this novel: `{first_chapter_title}`.\n\nMake it incredibly unique, engaging, and well-written.\n\nHere is a description of the writing style you should use: `{writing_style}`\n\nInclude only the chapter text. There is no need to rewrite the chapter name."}
        ]
    )

    print_step_costs(response, "gpt-4-0613")

    improved_response = openai.ChatCompletion.create(
        model="gpt-4-32k-0613",
        messages=[
            {"role": "system", "content": "You are a world-class fantasy writer. Your job is to take your student's rough initial draft of the first chapter of their fantasy novel, and rewrite it to be significantly better, with much more detail."},
            {"role": "user", "content": f"Here is the high-level plot you asked your student to follow: {plot}\n\nHere is the first chapter they wrote: {response['choices'][0]['message']['content']}\n\nNow, rewrite the first chapter of this novel, in a way that is far superior to your student's chapter. It should still follow the exact same plot, but it should be far more detailed, much longer, and more engaging. Here is a description of the writing style you should use: `{writing_style}`"}
        ]
    )

    print_step_costs(response, "gpt-4-32k-0613")

    return improved_response['choices'][0]['message']['content']

def write_chapter(previous_chapters, plot, chapter_title):
    try:
        i = random.randint(1, 2242)
        # write_to_file(f'write_chapter_{i}', f"Plot: {plot}, Previous Chapters: {previous_chapters}\n\n--\n\nWrite the next chapter of this novel, following the plot and taking in the previous chapters as context. Here is the plan for this chapter: {chapter_title}\n\nWrite it beautifully. Include only the chapter text. There is no need to rewrite the chapter name.")
        response = openai.ChatCompletion.create(
            model="gpt-4-0613",
            messages=[
                {"role": "system", "content": "You are a world-class fantasy writer."},
                {"role": "user", "content": f"Plot: {plot}, Previous Chapters: {previous_chapters}\n\n--\n\nWrite the next chapter of this novel, following the plot and taking in the previous chapters as context. Here is the plan for this chapter: {chapter_title}\n\nWrite it beautifully. Include only the chapter text. There is no need to rewrite the chapter name."}
            ]
        )

        print_step_costs(response, "gpt-4-0613")

        return response['choices'][0]['message']['content']
    except:
        response = openai.ChatCompletion.create(
            model="gpt-4-32k-0613",
            messages=[
                {"role": "system", "content": "You are a world-class fantasy writer."},
                {"role": "user", "content": f"Plot: {plot}, Previous Chapters: {previous_chapters}\n\n--\n\nWrite the next chapter of this novel, following the plot and taking in the previous chapters as context. Here is the plan for this chapter: {chapter_title}\n\nWrite it beautifully. Include only the chapter text. There is no need to rewrite the chapter name."}
            ]
        )

        print_step_costs(response, "gpt-4-32k-0613")

        return response['choices'][0]['message']['content']

def generate_storyline(prompt, num_chapters):
    print("Generating storyline with chapters and high-level details...")
    json_format = """[{"Chapter CHAPTER_NUMBER_HERE - CHAPTER_TITLE_GOES_HERE": "CHAPTER_OVERVIEW_AND_DETAILS_GOES_HERE"}, ...]"""
    response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a world-class fantasy writer. Your job is to write a detailed storyline, complete with chapters, for a fantasy novel. Don't be flowery -- you want to get the message across in as few words as possible. But those words should contain lots of information."},
            {"role": "user", "content": f'Write a fantastic storyline with {num_chapters} chapters and high-level details based on this plot: {prompt}.\n\nDo it in this list of dictionaries format {json_format}'}
        ]
    )

    print_step_costs(response, "gpt-4-0613")

    improved_response = openai.ChatCompletion.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": "You are a world-class fantasy writer. Your job is to take your student's rough initial draft of the storyline of a fantasy novel, and rewrite it to be significantly better."},
            {"role": "user", "content": f"Here is the draft storyline they wrote: {response['choices'][0]['message']['content']}\n\nNow, rewrite the storyline, in a way that is far superior to your student's version. It should have the same number of chapters, but it should be much improved in as many ways as possible. Remember to do it in this list of dictionaries format {json_format}"}
        ]
    )

    print_step_costs(improved_response, "gpt-4-0613")

    return improved_response['choices'][0]['message']['content']

def write_to_file(prompt, content):
    # Create a directory for the prompts if it doesn't exist
    if not os.path.exists('prompts'):
        os.mkdir('prompts')

    # Replace invalid characters for filenames
    valid_filename = ''.join(c for c in prompt if c.isalnum() or c in (' ', '.', '_')).rstrip()
    file_path = f'prompts/{valid_filename}.txt'

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Output for prompt "{prompt}" has been written to {file_path}\n')

def write_fantasy_novel(prompt, num_chapters, writing_style):
    plots = generate_plots(prompt)

    best_plot = select_most_engaging(plots)

    improved_plot = improve_plot(best_plot)

    title = get_title(improved_plot)

    storyline = generate_storyline(improved_plot, num_chapters)
    chapter_titles = ast.literal_eval(storyline)

    novel = f"Storyline:\n{storyline}\n\n"

    first_chapter = write_first_chapter(storyline, chapter_titles[0], writing_style.strip())
    novel += f"Chapter 1:\n{first_chapter}\n"
    chapters = [first_chapter]

    for i in range(num_chapters - 1):
        print(f"Writing chapter {i+2}...") # + 2 because the first chapter was already added
        chapter = write_chapter(novel, storyline, chapter_titles[i+1])
        novel += f"Chapter {i+2}:\n{chapter}\n"
        chapters.append(chapter)

    return novel, title, chapters, chapter_titles
