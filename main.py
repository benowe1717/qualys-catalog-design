#!/usr/bin/env python3
"""
Build the Qualys Catalog for SumTotal Learn LMS
"""
import json
import os
import sys

import jinja2
import minify_html

from src.classes.parseargs import ParseArgs


def main() -> int:
    """
    Main program loop
    """
    parseargs = handle_args()

    template_vars = {
        'css': '',
        'logo': '',
        'background': '',
        'levels_of_training': '',
    }

    config = parseargs.config_file.yaml
    try:
        template_vars = build_template_vars(
            parseargs.action, template_vars, config['base_urls']
        )
        template_vars['learning_paths'] = []

        for _, values in config['files']['learning_paths'].items():
            try:
                json_data = load_learning_path(values['file'])
                template_vars['learning_paths'].append({
                    'title': values['title'],
                    'paths': json_data
                })
            except (json.JSONDecodeError, ValueError) as e:
                print(e)
                return -1

    except KeyError as exc:
        print(f'ERROR: {exc}')
        return -1

    try:
        html_content = render_template(
            config['files']['templates_folder'],
            template_vars
        )

    except KeyError as exc:
        print(f'ERROR: {exc}')
        return -1
    except ValueError as exc:
        print(exc)
        return -1

    if parseargs.action != 'local':
        minified_html_content = minify_html_content(html_content)
        result = write_html_file(
            config['files']['output_folder'],
            config['files']['output_file'],
            minified_html_content
        )
    else:
        result = write_html_file(
            config['files']['output_folder'],
            config['files']['output_file'],
            html_content
        )

    if not result:
        return -1

    return 0


def build_template_vars(
        action: str,
        template_vars: dict,
        config: dict
) -> dict:
    """
    Iterate over the configured values for the given action and add them
    to the template_vars dictionary

    :param action: The action to build against, either local|stage|prod
    :type action: str
    :param template_vars: The dictionary of required variables
    :type template_vars: dict
    :param config: The dictionary of values to fill in the template variables
    :type config: dict
    :raises KeyError: When the configuration is missing a required template
    variables
    :return: The template variables and their values
    :rtype: dict
    """
    for key, _ in template_vars.items():
        try:
            template_vars[key] = config[action][key]
        except KeyError as err:
            raise KeyError(f'Missing Key: {err}') from err
    return template_vars


def handle_args() -> ParseArgs:
    """
    Handle the passed arguments to the script and return the ParseArgs
    class object

    :return: The ParseArgs class
    :rtype: ParseArgs
    """
    args = sys.argv[1:]
    parseargs = ParseArgs(args)
    return parseargs


def load_learning_path(file: str) -> dict:
    """
    Read and return JSON data as a Dictionary from the given file

    :param file: The file
    :type file: str
    :raises ValueError: When the file does not exist
    :raises json.JSONDecodeError: When the file is invalid JSON
    :return: The dictionary of JSON data
    :rtype: dict
    """
    if not os.path.exists(file):
        raise ValueError(f'ERROR: {file} does not exist!')
    with open(file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as exc:
            raise ValueError(f'ERROR: {file} is not valid JSON!') from exc


def render_template(template_dir: str, template_vars: dict) -> str:
    """
    Get the template directory from the config file, build, render, and
    return the HTML content

    :param template_dir: The directory containing all HTML templates
    :type template_dir: str
    :param template_vars: A dictionary where all keys are vars in the template
    :type template_vars: dict
    :raises ValueError: If the template directory is empty or cannot be found
    :return: The rendered HTML content
    :rtype: str
    """
    try:
        environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_dir),
            trim_blocks=True,
            lstrip_blocks=True)
        template = environment.get_template('base.html.j2')
        return template.render(template_vars)
    except jinja2.TemplateNotFound as exc:
        raise ValueError(f'ERROR: {exc}') from exc


def minify_html_content(content: str) -> str:
    """
    Take the unminified and potentially unformatted HTML string and return
    a minified and properly formatted HTML str

    :param content: The HTML content
    :type content: str
    :return: The minified HTML content
    :rtype: str
    """
    return minify_html.minify(content)


def write_html_file(output_dir: str, output_file: str, content: str) -> bool:
    filepath = os.path.join(os.getcwd(), output_dir, output_file)
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
    return True


if __name__ == '__main__':
    RESULT = main()
    if RESULT != 0:
        sys.exit(1)
    sys.exit(0)
