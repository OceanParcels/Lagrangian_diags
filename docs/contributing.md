# Contributing

## Adding a notebook

```{note}
TODO: Add instructions on how to add a new notebook.
- Things to consider:
  - How to name the notebook
  - What structure to follow (metadata to include at top (version info, packages installed), sectioning). Is there a template notebook?
  - Whether to include data files in the repository
```

## Development setup

To get started contributing to Lagrangian Diags:

- `fork the repo <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository>`\_
- Clone your fork to your local machine
- Install this projects dependencies so that you can build the documentation.

Assuming you have conda installed, you can create a development environment called `diags` with the following command:

```bash
conda env create -n diags -f docs/environment_docs.yml
```

Then you can build the documentation with:

```bash
sphinx-autobuild docs docs/_build
```

## Credits

Thank you to our contributors who make this project possible:

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
