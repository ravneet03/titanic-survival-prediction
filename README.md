# Titanic Survival Prediction

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

## About The Project

### Built With

- Python
- Docker
- GitLab CI

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have the following installed:

- Docker
- Git

### Installation

1. **Clone the repo**

   ```bash
   git clone https://gitlab.com/mygroup18094828/first.git
   ```

2. **Navigate to the project directory**

   ```bash
   cd first
   ```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples, and demos work well in this space. You may also link to more resources.

## Folder Structure

```plaintext
first/
├── api/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── app.py
│   ├── models/
│   │   └── titanic_model.pkl
│   ├── templates/
│   │   └── form.html
│   ├── __init__.py
│   ├── kserve.yaml
│   ├── __pycache__/
│   │   ├── app.cpython-312.pyc
│   │   └── __init__.cpython-312.pyc
├── cli_tool.py
├── .gitlab-ci.yml
├── data/
│   ├── processed/
│   │   └── titanic_processed.csv
│   └── raw/
│       ├── titanic-.csv
│       └── titanic.csv
├── deploy_serve/.gitlab-ci.yml
├── deploy_train/.gitlab-ci.yml
├── Dockerfile.train
├── README.md
├── requirements.txt
├── titanic/
│   ├── config.py
│   ├── dataset.py
│   ├── features.py
│   ├── __init__.py
│   ├── modeling/
│   │   ├── __init__.py
│   │   ├── predict.py
│   │   └── train.py
│   └── plots.py
```

### Running the Application

Follow these steps to run the entire application:

1. **Train the model locally:**
    ```sh
    python cli_tool.py train-local
    ```

2. **Train the model in Docker:**
    ```sh
    python cli_tool.py train-deployment
    ```

3. **Start the local server for the model endpoint:**
    ```sh
    python cli_tool.py service-local
    ```

4. **Run model serving on Docker:**
    ```sh
    python cli_tool.py service-deploy
    ```


### GitLab CI/CD Pipelines

Pipelines will be automatically triggered whenever changes are merged to the exp or main branches.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. **Fork the Project**
2. **Create your Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```

3. **Commit your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```

5. **Open a Pull Request**

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact

Your Name - [Ravneet Singh]- ravneetsingh290@gmail.com

Project Link: [https://gitlab.com/mygroup18094828/first](https://gitlab.com/mygroup18094828/first)


