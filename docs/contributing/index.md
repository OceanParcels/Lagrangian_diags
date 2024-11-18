# Contributing

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

## Roadmap

<div><iframe width="600" height="400" frameBorder="0" src="https://www.mindmeister.com/maps/public_map_shell/2706147482/how-to-quantify-differences-in-lagrangian-statistics-from-two-different-oceanic-flow-fields?width=600&height=400&z=auto&no_share=1&no_logo=1" scrolling="no" style="overflow:hidden;margin-bottom:5px">Your browser is not able to display frames. Please visit <a href="https://www.mindmeister.com/2706147482/how-to-quantify-differences-in-lagrangian-statistics-from-two-different-oceanic-flow-fields" target="_blank">How to quantify differences in Lagrangian statistics from two different oceanic flow fields?</a> on MindMeister.</iframe></div>
