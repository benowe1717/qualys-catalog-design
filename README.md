# Qualys Catalog Design

This repository houses the Qualys SumTotal Learn Catalog design artifacts and build process. The catalog page was made using a combination of HTML and CSS (through Tailwind CSS v3) built by Python3 using Jinja2 templates.

Courses, classes, and exams are laid out in Learning Paths, which can be found in either the `core_learning_paths.json` file and the `application_learning_paths.json` file. Core Learning Paths are displayed first, followed by the Application Learning Paths.

Python 3.10+ will preserve the order of dictionaries, which is why we use a JSON file for each learning path and still retain the ordering we want.

The program will read in the JSON files from the given config file and will loop through each path and build out the appropriate Jinja2 template based on the action, which specifies which environment you want the index.html file built for. You can configure how each environment works in the config file. Once the templates have been built, a single HTML file is created, with minified HTML content, and written to the desired location.

## Prerequisites

Before you begin, ensure you have met the following software requirements:

### Python Requirements

- Python 3.10.12+: If your system is not already on Python3.10.12, you can still use this project by installing Python 3.10.12 into a Virtual Environment. You will need to use a virtual environment for this project anyways.
- Linux/Unix: I did not test this on a Windows device, so some of the path and OS modules may function differently. If you need to use this on a Windows machine, file an issue with the request and I'll adjust accordingly.

### Tailwind CSS Requirements:

- v3: This Tailwind CSS design was done only using v3, so make sure that's the version you install.

### Other

This project assumes that you have a basic understanding of HTML, CSS, Tailwind, Python, and Jinja2 templating and does not attempt to teach these concepts. To read or learn more about each assumption, you can check out the links here:
- [HTML](https://www.freecodecamp.org/news/introduction-to-html-basics/)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Tutorials)
- [Tailwind CSS v3](https://v3.tailwindcss.com/docs/utility-first)
- [Python3](https://docs.python.org/3/tutorial/index.html)
- [Jinja2](https://realpython.com/primer-on-jinja-templating/)

## Installing

To install the necessary Python dependencies, follow these steps:

1. Check out the repository on a machine with `Python 3.10.12+` installed:
`git clone https://github.com/benowe1717/qualys-catalog-design.git`

2. Create a python virtual environment:
`python3.10 -m venv .venv`

If your default version is already on python 3.10+:
`python3 -m venv .venv`

3. Activate the newly created virtual environment:
`source .venv/bin/activate`

4. Install any required dependencies:
`python3 -m pip install -r requirements.txt`

If you had to install python3.10.12 separately, make sure you use the python binary from your virtual environment like this:
`.venv/bin/python3 -m pip install -r requirements.txthttps://v3.tailwindcss.com/docs/installation`

To install the necessary Tailwind dependencies, follow these steps:

1. Install `npm` from: [NodeJS Docs](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#using-a-node-installer-to-install-nodejs-and-npm)

2. Follow the rest of the instructions from Tailwind's Documentation: [v3 Install](https://v3.tailwindcss.com/docs/installation)
NOTE: Use the `Tailwind CLI` install steps

For more information on virtual environments, see below:
- https://docs.python.org/3/library/venv.html
- https://www.pythonguis.com/tutorials/python-virtual-environments/

## Using

To use this application, make sure that you have correctly filled in the config file. I suggest not editing the config file found in the default path of `./src/configs/config.yaml` as any new updates to this repository, requiring you to `git pull`, risks clobbering your config. My recommendation is to take a copy of the config and place it inside of the `./data/` folder. This folder will never be clobbered during a `git pull`.

To do this:
`cp ./src/configs/config.yaml ./data/`

You will then need to edit the config.yaml file and fill in the appropriate URLs for each environment. Here's a good thought process for the environments:
- `local`: This is for testing new design changes or bug fixes. It should reference local file paths or relative file paths.
- `stage`: This is for testing within the LMS Staging environment. All of the paths should reference staging-specific URLs
- `prod`: This is for deploying to production. All of the paths should reference prod-specific URLs

Now that your config file is filled in, you can run a build by:
1. Activate the virtual environment:
`source .venv/bin/activate`

2. Run the program:
`python3 main.py --config-file /path/to/config.yaml --action local`

NOTE: If you needed to install another version of python, be sure to use the virtual environment's binary instead:
`.venv/bin/python3 main.py --config-file /path/to/config.yaml --action local`

The newly created index.html file will be stored in the path you choose, which by default, is in the `./output/` folder.

For help or more information on the available parameters, you can run:
`python3 main.py --help`

## Contributing

1. Fork this repository
2. Create a branch: `git checkout -b <branch_name>`
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the Pull Request

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

- [@benowe1717](https://github.com/benowe1717)

## Contact

For help or support on this repository, follow these steps:

- [Create an issue](https://github.com/benowe1717/qualys-catalog-design/issues)

## License

This project uses the following license: GNU GPLv3.

## Sources

- https://github.com/scottydocs/README-template.md/blob/master/README.md
- https://choosealicense.com/
- https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
