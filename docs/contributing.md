# Contributing

## Adding a notebook

```{note}
TODO: Add instructions on how to add a new notebook.
- Things to consider:
  - How to name the notebook
  - What structure to follow (metadata to include at top, sectioning). Is there a template?
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
