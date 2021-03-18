# HPC/Exascale Centre of Excellence in Personalised Medicine

## Sample Application using Building Blocks

This repository provides a sample application using the **HPC/Exascale Centre of Excellence in Personalised Medicine** (
[PerMedCoE](https://permedcoe.eu/)) **Building Blocks (BBs)**.

This application can be executed in a HPC with **PyCOMPSs**, **NextFlow** and **Snakemake**.

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Sample Application using Building Blocks](#sample-application-using-building-blocks)
  - [Table of Contents](#table-of-contents)
  - [Application package structure](#application-package-structure)
  - [Usage](#usage)
    - [Requirements](#requirements)
    - [Execution](#execution)
  - [Best practices](#best-practices)
  - [License](#license)
  - [Contact](#contact)

## Application package structure

The suggested structure for an application is:

```text
├── config
│   ├── ...
│   └── conf.yaml
├── dataset
│   ├── ...
│   └── ...
├── LICENSE
├── NextFlow
│   ├── NextFlow.nf
│   └── launch.sh
├── PyCOMPSs
│   ├── app.py
│   └── launch.sh
├── README.md
└── SnakeMake
    ├── Snakefile
    └── launch.sh
```

Firstly, the application must contain a `LICENSE` file and a `README.md` file with the application description in the main folder.

A `config` folder with the configuration files used in the application (e.g. `conf.yaml`).

[Optional] A `dataset` folder containing the input dataset. This is only reasonable for very small datasets. Alternatively, the dataset path can be defined in the application for a different folder (e.g. big dataset in shared folder).

The application:

- Using PyCOMPSs:
  - Provide a Python script that import the required BBs and invokes them using their Python interface (`app.py`).
  - Include a launch script (`launch.sh`)

- Using NextFlow:
  - Provide a NextFlow script (`NextFlow.nf`)
  - Include a launch script (`launch.sh`)

- Using SnakeMake:
  - Provide a Snakefile script (`Snakefile`)
  - Include a launch script (`launch.sh`)

> **NOTE:** Please note that it is not mandatory to provide the application for the three workflow managers.
>
> **NOTE:** This sample application contains the same example with PyCOMPSs, NextFlow and SnakeMake.

## Usage

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- A workflow framework:
  - [PyCOMPSs](https://pycompss.readthedocs.io/en/latest/Sections/00_Quickstart.html)
  - [NextFlow](https://www.nextflow.io/docs/latest/getstarted.html)
  - [SnakeMake](https://snakemake.readthedocs.io/en/stable/getting_started/installation.html)
- Install `sample_BB`.

### Execution

The application can be launched using any of the workflow managers through the `launch.sh` script.

## Best practices

There are a set of best practices suggested to BB developers:

- Use a code style:
  - [pep8](https://www.python.org/dev/peps/pep-0008/)
  - [black](https://github.com/psf/black)

- Document your application.

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
