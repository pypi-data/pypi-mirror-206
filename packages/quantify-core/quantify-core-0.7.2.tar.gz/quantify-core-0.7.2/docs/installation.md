```{highlight} console
```

# Installation

## Stable release

This is the preferred method to install Quantify, as it will always install the most recent stable release.
If you want to contribute to Quantify, see {ref}`Setting up for local development`.

### On Windows and macOS (Anaconda)

{mod}`quantify-core` has third party dependencies that can have environment-specific problems.
We recommend using the [Anaconda](https://www.anaconda.com/products/individual#Downloads) Python distribution which works out of the box on most systems.

If you are familiar with software development (package manager, git, terminal, Python, etc.) the following should get you running in no time. Otherwise, follow the {ref}`Detailed instructions` and learn a few productivity tips on your way.

1. Install [Anaconda](https://www.anaconda.com/products/individual#Downloads).

2. Install Quantify (and JupyterLab) in a new conda environment, see also the [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html).

   > ```{admonition} Supported Python versions
   > Check the supported Python versions on PyPi: [quantify-core](https://pypi.org/project/quantify-core/) | [quantify-scheduler](https://pypi.org/project/quantify-scheduler/)
   > ```

   > N.B. If you are interested to contribute to {mod}`quantify-core` and/or {mod}`quantify-scheduler` you should {ref}`set them up for local development instead <Setting up for local development>`.
   >
   > ```
   > $ # run the following commands step by step!
   >
   > $ conda create --name quantify-env python=3.8
   > $ conda activate quantify-env
   > $ conda install -c conda-forge jupyterlab
   > $ python -m ipykernel install --user --name=quantify-env  --display-name="Python 3 Quantify Env"
   > $ pip install quantify-core
   >
   > $ # (Optionally) install quantify-scheduler:
   >
   > $ pip install quantify-scheduler
   > $ jupyter labextension install jupyterlab-plotly --no-build
   > $ # this might take a few minutes
   > $ jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget
   > ```

3. You are good to go! Head over to the {ref}`User guide <user-guide>` to get started.

#### Detailed instructions

1. Install [Anaconda](https://www.anaconda.com/products/individual#Downloads).

   > On Windows, during the installation, we recommend to select the options:
   >
   > - Install for `All Users (requires admin privileges)`; and
   > - `Add Anaconda3 the system PATH environment variable`.
   >
   > ``````{admonition} Instructions: Anaconda install (Windows)
   > :class: dropdown, info
   >
   > ```{figure} /images/install/conda_install.gif
   > :name: conda_install
   > :width: 500
   > ```
   > ``````

2. (Windows only) Install [Git BASH](https://gitforwindows.org/) to have a unix-like bash terminal (default options during installation should work well on most setups).

   > ```{tip}
   > Users can right click any folder in windows and open Git BASH in that location.
   > ```
   >
   > ```{note}
   > Be aware that a unix-like terminal on windows has some caveats. To avoid them, we recommend to run any Python code using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) (installation steps below).
   > ```

3. (Windows only) Add {code}`source /path/to/Anaconda3/etc/profile.d/conda.sh` in the `.bashrc` (or in the `.bash_profile`) to expose the anaconda in bash terminal (see instruction below if you need help).

   > ```{tip}
   > If you followed the default anaconda installation the path to it will be similar to
   > {code}`/c/Users/<YOUR_USERNAME>/anaconda3/etc/profile.d/conda.sh` or {code}`/c/ProgramData/Anaconda3/etc/profile.d/conda.sh`.
   >
   > Pro tip: you can drag and drop a file from the file explorer into the terminal and get the path of the file (instead of typing it manually).
   > ```
   >
   > ``````{admonition} Instructions: expose anaconda in the bash terminal
   > :class: dropdown, info
   >
   > Below we illustrate this process in Git Bash. You can find detailed step-by-step instructions [here](https://superuser.com/a/602896).
   >
   > ```{figure} /images/install/conda_source_installed_all_users.gif
   > :name: conda_source
   > :width: 500
   > ```
   > ``````
   >
   > ```{note}
   > To confirm you have a functional installation of anaconda, run {code}`conda` in the terminal. This will print the conda help message which is an indication of a working installation.
   > ```

4. Create a conda environment, see also the [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html).

   > ```
   > $ conda create --name quantify-env python=3.8   # create the conda environment, you can replace `quantify-env` if you wish
   > $ conda activate quantify-env                   # activates the conda environment
   > ```
   >
   > ```{tip}
   > You can add {code}`conda activate quantify-env` at the end of the `.bashrc` (or `.bash_profile`) if you wish for this environment to be activated automatically in the terminal when it is opened (see instructions below).
   > ```
   >
   > ``````{admonition} Instructions: create conda env and auto-activate (Windows)
   > :class: dropdown, info
   >
   > ```{figure} /images/install/conda_activate.gif
   > :name: conda_activate
   > :width: 500
   > ```
   > ``````

5. Install `jupyter-lab` in the new environment using:

   ```
   $ conda install -c conda-forge jupyterlab  # install jupyter lab
   $ # add the environment as an available kernel for jupyter notebook within jupyter-lab.
   $ python -m ipykernel install --user --name=quantify-env  --display-name="Python 3 Quantify Env"
   ```

6. Install {mod}`quantify-core` from pypi

   > If you are interested to contribute to Quantify-core you should {ref}`set it up for local development instead <Setting up for local development>`.
   >
   > ```
   > $ pip install quantify-core
   > ```
   >
   > ```{note}
   > We currently do not have a conda recipe for installation, instead we refer to the default pip installation within a conda environment.
   > ```

7. (Optionally) install {mod}`quantify-scheduler`

   > If you are interested to contribute to {mod}`quantify-scheduler` you should {ref}`set it up for local development instead <Setting up for local development>`. You only need to replace {mod}`quantify-core` with {mod}`quantify-scheduler` in the provided commands.
   >
   > ```
   > $ pip install quantify-scheduler
   > $ jupyter labextension install jupyterlab-plotly --no-build
   > $ # this might take a few minutes
   > $ jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget
   > ```

### Other operating systems

Confirm that you have a compatible working Python interpreter by running the following in your terminal of choice:
```
$ python --version
Python 3.8.10
```
```{admonition} Supported Python versions
Check the supported Python versions on PyPi: [quantify-core](https://pypi.org/project/quantify-core/) | [quantify-scheduler](https://pypi.org/project/quantify-scheduler/)
```

Install Quantify:

```
$ pip install quantify-core
```

If you don't have [pip] installed, this [Python installation guide] can guide
you through the process.

## Update to the latest version

To update Quantify to the latest version:

```
$ pip install quantify-core
```

## Setting up for local development

Ready to contribute? Here's how to set up Quantify for local development.

00. Follow the {ref}`Installation` steps for your system skipping the last step ({code}`pip install ...`).

01. Fork the `quantify-core` repo on GitLab.

02. Clone your fork locally:

    ```
    $ git clone git@gitlab.com:your_name_here/quantify-core.git
    ```

03. Install {mod}`quantify-core` locally:

    ```
    $ cd quantify-core/
    $ pip install -e ".[dev]"
    ```

04. (Optional) Install `pre-commit` which will automatically format the code using [black](https://github.com/psf/black):

    > ```
    > $ pre-commit install
    > ```
    >
    > ```{note}
    > When the code is not well formatted a `git commit` will fail. You only need to run it again. This second time the code will be already *black*-compliant.
    > ```

05. Create a branch for local development:

    ```
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

06. To ensure good quality code run [pylint](https://pylint.readthedocs.io/en/latest/index.html) on your code and address any reasonable code quality issues. See [Editor and IDE integration](https://pylint.readthedocs.io/en/latest/user_guide/ide-integration.html) for tips on how to integrate pylint in your editor or IDE.

07. When you are done making changes, auto-format the repository with `black` and ensure test coverage

    > ```
    > $ black .
    > $ pytest --cov
    > ```
    >
    > ``````{tip}
    > Running parts of the test suite
    >
    > To run only parts of the test suite, specify the folder in which to look for
    > tests as an argument to pytest. The following example
    >
    > ```
    > $ py.test tests/measurement --cov quantify_core/measurement
    > ```
    >
    > will look for tests located in the tests/measurement directory and report test coverage of the quantify_core/measurement module.
    > ``````
    >
    > ``````{tip}
    > Speed up tests with parallel execution
    >
    > ```
    > $ py.test -n 2 # where 2 is the number of cores of your CPU
    > ```
    > ``````

08. Building the documentation

    > If you have worked on documentation or [docstrings](https://www.python.org/dev/peps/pep-0257/) you need to review how your docs look locally and ensure *no error or warnings are raised*.
    > You can build the docs locally using:
    >
    > ```
    > $ cd docs
    >
    > $ # unix
    > $ make html
    >
    > $ # windows
    > $ ./make.bat html
    > ```
    >
    > The docs will be located in `quantify_core/docs/_build`.
    >
    > ``````{tip}
    > If you are working on documentation it can be useful to automatically rebuild the docs after every change.
    > This can be done using the `sphinx-autobuild` package. Through the following command:
    >
    > ```
    > $ sphinx-autobuild docs docs/_build/html
    > ```
    >
    > The documentation will then be hosted on `localhost:8000`
    > ``````
    >
    > ```{tip}
    > Building the tutorials can be time consuming, if you are not editing them, feel free to delete your local copy of the `quantify-core/docs/tutorials` to skip their build. You can recover the files using git (do not commit the deleted files).
    > ```

09. Commit your changes and push your branch to GitLab:

    ```
    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

10. Review the {ref}`Merge Request Guidelines` and submit a merge request through the GitLab website.

11. Add a short entry in the `CHANGELOG.md` under `Unreleased`, commit and push.

## Troubleshooting

If for some reason you are not able to install or use Quantify using the prescribed ways indicated above, make sure you have a working Python environment (e.g. you can run an `IPython` terminal). Follow the next steps that aim at installing Quantify from source and running its tests.

0. Uninstall {mod}`quantify-core`:

   ```
   $ pip uninstall quantify-core
   ```

1. Install from source (run line by line):

   ```
   $ git clone https://gitlab.com/quantify-os/quantify-core.git; cd quantify-core
   $ pip install --upgrade --upgrade-strategy eager ".[dev]"
   $ pytest -v
   ```

2. The tests will either pass or not. In any case, please report your experience and which test do not pass by creating a `New issue` on the [issue tracker](https://gitlab.com/quantify-os/quantify-core/-/issues), your efforts are much appreciated and will help us to understand the problems you might be facing.

### Downgrade to a specific version

If for any reason you require a specific version of the package, e.g. 0.3.0, run:

```
$ pip install --upgrade quantify-core==0.3.0
```

### Potential issues: PyQtGraph and PyQt5

{mod}`quantify-core` has a dependency on the `PyQt5` package, which itself has a dependency on the `Qt5` runtime.
On most systems, the standard installation process will correctly install Qt.
The Anaconda installation should resolve issues with installation on Windows or macOS.
You may need to consult a search engine if you have a more exotic system.

[pip]: https://pip.pypa.io
[python installation guide]: http://docs.python-guide.org/en/latest/starting/installation/
