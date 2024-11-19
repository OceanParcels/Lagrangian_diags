# Contributing

## Project structure

You are welcome to contribute by improving the code for already existing methods or by adding new code for additional methods and diagnostics. In general, we aim to provide the code for the different methods as functions (see here: [./Diagnostics/Functions](https://github.com/OceanParcels/Lagrangian_diags/tree/main/Diagnostics/Functions)), that are then applied and explained in jupyter notebooks (see here: [./docs/tutorials/](https://github.com/OceanParcels/Lagrangian_diags/tree/main/docs/tutorials/)) by making use of the output of a set of very basic example particle simulations (to be found here: [./Simulations/](https://github.com/OceanParcels/Lagrangian_diags/tree/main/Simulations)). Please let us know in case the particle trajectory sets/simulations are inadequate for your diagnostic, so that we can adjust or expand our data sets.

If the provided example particle trajectory datasets or simulations are inadequate for your diagnostic, please inform us so we can update or expand the datasets.

### Adding a notebook

```{note}
TODO: Add instructions on how to add a new notebook.
- Things to consider:
  - How to name the notebook
  - What structure to follow (metadata to include at top (version info, packages installed), sectioning). Is there a template notebook?
  - Whether to include data files in the repository
```

## Development workflow

To get started contributing to Lagrangian Diags:

1. [Fork the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository)

2. Clone the repository and `cd` into the project folder

```
git clone <fork_url>
cd <project_folder>
```

3. Create a working branch

```
git branch <branch_name>
git checkout <branch_name>
```

4. Change existing code or add new code - do not forget to regularly commit your changes!

5. Push your changes and make a pull request

```
git push -u origin <branch_name>
```

```{note}
If you have write access to the Lagrangian Diags repository, you don't have to create a fork. You just need to clone the repository and create a working branch. Just make sure that your working branch has a good naming so that others are aware of its contents (e.g., `<your_initials>-dispersion`).
```

### OPTIONAL: Install documentation dependencies

If you want to build the documentation locally, you will need to install the dependencies in the `docs/environment_docs.yml` file. You can create this environment (called `diag-docs` with the following command):

```bash
conda env create -n diag-docs -f docs/environment_docs.yml
```

Then you can build the documentation with:

```bash
sphinx-autobuild docs docs/_build
```

### Style guide and pre-commit tooling

This project has automated workflows to help with code quality and adhering to Python style conventions (this tooling is detailed in the `.pre-commit-config.yaml` file). To use this tooling locally (optional, as this is already run automatically in the cloud), you will need to install the pre-commit package and then install the hooks. You can do this by running the following commands:

```
conda install -c conda-forge pre-commit
pre-commit install
```

```{note}
TODO: Add all items in this section to pre-commit tooling, and then trim down this section (no need to excessively document it if its enforced by the tooling).

---

All python code should be written following the [PEP8 style guide](https://peps.python.org/pep-0008/) as closely as possible. Functions should be implemented following the [numpy doctstring convention](https://numpydoc.readthedocs.io/en/latest/format.html), and - to enable a good documentation - should contain the following sections:

- Short description (one line of information saying what the function does)
- Parameters
- Returns
- Extended description (more detailed information on what the function does, could include mathematical equations)
- See also (similar diagnostics, alternative methods for same diagnostic)
- Notes (information on when (not) to use the function)
- References (literature where method is introduced)
- Examples (refer to notebook and give minimum example)
```

## Credits

Thank you to our contributors who make this project possible 🎉

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LauraGomezNavarro"><img src="https://avatars.githubusercontent.com/u/20359692?v=4?s=100" width="100px;" alt="Laura Gomez Navarro"/><br /><sub><b>Laura Gomez Navarro</b></sub></a><br /><a href="https://github.com/OceanParcels/Lagrangian_diags/commits?author=LauraGomezNavarro" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jimena-medinarubio"><img src="https://avatars.githubusercontent.com/u/101462540?v=4?s=100" width="100px;" alt="Jimena Medina"/><br /><sub><b>Jimena Medina</b></sub></a><br /><a href="https://github.com/OceanParcels/Lagrangian_diags/commits?author=jimena-medinarubio" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/sruehs"><img src="https://avatars.githubusercontent.com/u/33282992?v=4?s=100" width="100px;" alt="sruehs"/><br /><sub><b>sruehs</b></sub></a><br /><a href="#ideas-sruehs" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/OceanParcels/Lagrangian_diags/commits?author=sruehs" title="Code">💻</a> <a href="#projectManagement-sruehs" title="Project Management">📆</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.uu.nl/staff/BAltena"><img src="https://avatars.githubusercontent.com/u/64000582?v=4?s=100" width="100px;" alt="Bas Altena"/><br /><sub><b>Bas Altena</b></sub></a><br /><a href="https://github.com/OceanParcels/Lagrangian_diags/commits?author=dicaearchus" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
