# Lagrangian_diags
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
[![Documentation Status](https://readthedocs.org/projects/lagrangian-diags/badge/?version=latest)](https://lagrangian-diags.readthedocs.io/en/latest/?badge=latest)

Side-project lead by Siren and Laura to work on Lagrangian diagnostics.
This is WORK IN PROGRESS, EVERYONE IS WELCOME TO CONTRIBUTE! 

## Goal of the project
Starting from the general question how to quantify differences in Lagrangian statistics between 
various flow fields, we collect Lagrangian diagnostics commonly used (have a look at this Mindmap and feel free to add 
new info: https://www.mindmeister.com/map/2233459860?t=C9g9yYis4P), and test and compare different methods used to derive 
those diagnostic via python code.

## How to contribute
You are welcome to contribute by improving the code for already existing methods or by adding new code for additional methods and diagnostics. In general, we aim to provide the code for the different methods as functions (see here: [./Diagnostics/Functions](https://github.com/OceanParcels/Lagrangian_diags/tree/main/Diagnostics/Functions)), that are then applied and explained in jupyter notebooks (see here: [./Diagnostics/](https://github.com/OceanParcels/Lagrangian_diags/tree/main/Diagnostics/)) by making use of the output of a set of very basic exemplary particle simulations (to be found here: [./Simulations/](https://github.com/OceanParcels/Lagrangian_diags/tree/main/Simulations)). Please let us know in case the particle trajectory sets/simulations are inadequate for your diagnostic, so that we can adjust or expand our data sets. 

On the technical side, given how deeply you want to get involved, we offer 2 options for contributing:
1. Become developer and add changes via developer branch
2. Fork repository and send pull request to main branch

Please contact us in case you would like to contribute via the first option.

### Option 1: Become developer

1. Get added by project owner to project as collaborator
   
2. Clone repository
   
3. Create a working branch
-  ```git init``` (initialize GIT on your local machine)
-  ```git branch``` (check branch on your local machine)
-  ```git branch <branch_name>``` (create new working branch "branch_name" on your local machine: dev-<your_initials>)
-  ```git checkout <branch_name>``` (switch into the new working branch)
-  ```git push origin <branch_name>``` (create remote version of working branch)

4. Change existing code or add new code - do not forget to regularly commit your changes!
- do changes in local working branch
- ```git add <new_or_changed_file>``` (add files that you changed to stage them for version tracking)
- ```git commit -m "<short_message_on_change>``` (commit staged changes to update local working branch)
- ```git push origin <branch_name>``` (update remote version of working branch)
- repeat as often as required
  
5. Create a pull request (and potentially [link to issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) if you are solving one)
- ```git checkout main``` (switch to main branch on local machine)
- ```git pull main``` (update local main branch to capture potential new features of other contributors)
- ```git checkout <branch_name>``` (switch back to local working branch)
- ```git merge main``` (merge latest changes from local main into local working branch, eventually need to solve conflicts if other contributors worked on same files; ensure that the merged changes are commited to the local working branch)
- ```git push origin <branch_name>``` (update remote working branch with latest changes)
- create a pull request to add new features from <branch_name> to main: go to https://github.com/OceanParcels/Lagrangian_diags/tree/main and click on pull request to add your pull request (appears at top of page).  You can mention somebody to review your pull request.
  
### Option 2: Fork repository
1. Fork repository (e.g. using [GitHub Desktop](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop) or via [command line](https://docs.github.com/en/get-started/quickstart/fork-a-repo#fork-an-example-repository))
2. Create developer branch (identical to step 3 in option 1)
3. Change existing code or add new code (identical to step 4 in option 1)
4. Create pull request (identical to step 5 in option 1)
5. Create an additional pull request to add your feature branch to the original repository (make sure to check/merge updates from main in the original repository with procedure similar to step 5 in option 1)


## Style guide
All python code should be written following the [PEP8 style guide](https://peps.python.org/pep-0008/) as closely as possible. Functions should be implemented following the [numpy doctstring convention](https://numpydoc.readthedocs.io/en/latest/format.html), and - to enable a good documentation - should contain the following sections:
- Short description (one line of information saying what the function does)
- Parameters
- Returns
- Extended description (more detailed information on what the function does, could include mathematical equations)
- See also (similar diagnostics, alternative methods for same disgnostic)
- Notes (information on when (not) to use the function) 
- References (literature where method is introduced)
- Examples (refer to notebook and give minimum example) 


## Contributors

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
