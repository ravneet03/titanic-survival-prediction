
<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://gitlab.com/mygroup18094828/first">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">My Project</h3>

  <p align="center">
    A brief description of what this project does and who it's for.
    <br />
    <a href="https://gitlab.com/mygroup18094828/first"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://gitlab.com/mygroup18094828/first">View Demo</a>
    ·
    <a href="https://gitlab.com/mygroup18094828/first/issues">Report Bug</a>
    ·
    <a href="https://gitlab.com/mygroup18094828/first/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents

- [About the Project](#about-the-project)
  - [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://gitlab.com/mygroup18094828/first)

Here's a blank template to get started:

### Built With

* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)
* [GitLab CI](https://about.gitlab.com/stages-devops-lifecycle/continuous-integration/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have the following installed:
* Docker
* Git

### Installation

1. Clone the repo
   ```sh
   git clone https://gitlab.com/mygroup18094828/first.git
   ```
2. Navigate to the project directory
   ```sh
   cd first
   ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples, and demos work well in this space. You may also link to more resources.

## Folder Structure

```plaintext
first/
├── data/
│   ├── raw/
│   ├── processed/
├── models/
│   ├── training/
│   ├── serving/
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   ├── models/
│   ├── titanic/
│       ├── modeling/
│           ├── train.py
├── .gitlab-ci.yml
```

## Running the Application

Follow these steps to run the entire application:

1. Build Docker Images:
   ```sh
   docker-compose build
   ```

2. Run Training and Serving Containers:
   ```sh
   docker-compose up
   ```

3. Stop and Remove Containers:
   ```sh
   docker-compose down
   ```

4. GitLab CI/CD Pipelines:
   - Pipelines will be automatically triggered whenever changes are merged to the `exp` or `main` branches.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://gitlab.com/mygroup18094828/first](https://gitlab.com/mygroup18094828/first)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [othneildrew's Best-README-Template](https://github.com/othneildrew/Best-README-Template)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)

[product-screenshot]: images/screenshot.png