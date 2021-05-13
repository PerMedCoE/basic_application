# HPC/Exascale Centre of Excellence in Personalised Medicine

## Sample Building Block

This package provides a **Building Block (BB)** example using the **HPC/Exascale Centre of Excellence in Personalised Medicine** (
[PerMedCoE](https://permedcoe.eu/)) base Building Block ([permedcoe](https://github.com/PerMedCoE/permedcoe)).

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Sample Building Block](#sample-building-block)
  - [Table of Contents](#table-of-contents)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [Developer instructions](#developer-instructions)
    - [Building block](#building-block)
    - [Best practices](#best-practices)
  - [License](#license)
  - [Contact](#contact)

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)

### Installation

There are two ways to install this package (from Pypi and manually):

- From Pypi:

  This package is **NOT YET** publicly available in Pypi:

  ```shell
  pip install sample_BB
  ```

  or more specifically:

  ```shell
  python3 -m pip install sample_BB
  ```

- From source code:

  This package provides an automatic installation script, but it is necessary to install the `permedcoe` package before the `sample_BB` package since it is required by `sample_BB`.

  ```shell
  # Install permedcoe package
  cd ../PerMedCoE
  ./install.sh
  # Download sample_BB source
  cd ../sample_BB
  ./install.sh
  ```

  This script creates a file `installation_files.txt` to keep track of the installed files. It is used with the `uninstall.sh` script to clean up the system.

### Usage

The `sample_BB` package provides a clear interface that allows it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and Snakemake).

- Command line interface:

  Once installed the `sample_BB` package, it provides the `sample_BB`
  command, that can be used from the command line. For example:

  ```text
  $ sample_BB -h
  usage: sample_BB [-h] [-i INPUT [INPUT ...]] [-o OUTPUT [OUTPUT ...]] [-c CONFIG] [-d]
                  [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR] [--processes PROCESSES]
                  [--gpus GPUS] [--memory MEMORY] [--mount_points MOUNT_POINTS]

  optional arguments:
    -h, --help            show this help message and exit
    -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                          Input file/s or directory path/s
    -o OUTPUT [OUTPUT ...], --output OUTPUT [OUTPUT ...]
                          Output file/s or directory path/s
    -c CONFIG, --config CONFIG
                          Configuration file path
    -d, --debug           Enable Building Block debug mode. Overrides log_level
    -l {debug,info,warning,error,critical}, --log_level {debug,info,warning,error,critical}
                          Set logging level
    --tmpdir TMPDIR       Temp directory to be mounted in the container
    --processes PROCESSES
                          Number of processes for MPI executions
    --gpus GPUS           Requirements for GPU jobs
    --memory MEMORY       Memory requirement
    --mount_points MOUNT_POINTS
                          Comma separated alias:folder to be mounted in the container
  ```

  This interface can be used within any workflow manager that requires binaries (e.g. NextFlow and Snakemake).

  In addition, it can be used with PyCOMPSs by importing the decorated function or any other specific for PyCOMPSs.

  ```python
  from sample_BB.sample import personalize_model_task

  personalize_model_task(suffix=suffix,
                         model=model,
                         mutations_dataset=input,
                         output=output)
  ```

- Extension for PyCOMPSs:

  Moreover, a BB can also implement a Python function not limited to the input (file/s or directory/ies), output (file/s or directory/ies) and config (yaml file) signature. This enables application developers to use the BB with PyCOMPSs using Python objects instead of files among BBs.

  ```python
  from sample_BB.sample import personalize_model_bb_extended

  personalize_model_bb_extended(*args, **kwargs)  # specific interface
  ```

### Uninstall

Uninstall can be done as usual `pip` packages:

There are two ways to uninstall this package, that depends on the way that it was installed (from Pypi or using `install.sh`):

- From Pypi:

  ```shell
  pip uninstall sample_BB
  ```

  or more specifically:

  ```shell
  python3 -m pip uninstall sample_BB
  ```

- From manual installation (using `install.sh`):

  ```shell
  ./uninstall.sh
  ```

  And then the folder can be cleaned as well using the `clean.sh` script.

  ```shell
  ./clean.sh
  ```

## Developer instructions

### Building block

There are a set of rules to implement a PerMedCoE compliant Building Block:

- Provide a executable Python script with the following structure:

  ```Python
  from permedcoe import container
  from permedcoe import binary
  from permedcoe import task
  from permedcoe import FILE_IN
  from permedcoe import FILE_OUT
  from permedcoe import DIRECTORY_IN
  from permedcoe import DIRECTORY_OUT

  CONTAINER = "/path/to/container.sif"

  def sample_bb_extended(...):
      # Python code calling to tasks (see PyCOMPSs)
      ...

  @container(engine="SINGULARITY", image=CONTAINER)
  @binary(binary="/path/to/binary")
  @task(dataset=FILE_IN, output=FILE_OUT)
  def sample_bb_task(dataset_flag="-d", dataset=None,
                      output_flag="-o", output, ...):
      # Equivalent to:
      # /path/to/binary -d dataset -o output
      ...

  def invoke(input, output, config):
      # Process config parameters dictionary to
      # prepare the call to 'sample_bb_task'
      dataset = input
      sample_bb_task(dataset=dataset,
                     output=output)
      ...
  ```

- Use a single container per Building Block (`CONTAINER`).

- Use the decorators provided by `permedcoe` package. They provide the capability to use the BB in various workflow managers transparently. In other words, the BB developer does not have to deal with the peculiarities of the workflow managers.

- A BB can be a single executable, but it can be a more complex code if the `sample_bb_extended` function is implemented and used with PyCOMPSs.

- It is necessary to have function (`invoke`) with a specific signature: `(input, output, config)`.

- The BB `binary` must be defined with the `@task`, `@binary` and `@container` decorators (`sample_bb_task`). This function needs to declare the binary flags, and it is invoked from the `invoke` function.

- The `@task` decorator must declare the type of the file or directories for the binary invocation. In particular, using the parameter name and `FILE_IN`/`FILE_OUT`/`DIRECTORY_IN`/`DIRECTORY_OUT` to define if the parameter is a file or a directory and if the binary is consuming the file/directory or it is producing it.

### Best practices

There are a set of best practices suggested to BB developers:

- Use a code style:
  - [pep8](https://www.python.org/dev/peps/pep-0008/)
  - [black](https://github.com/psf/black)

- Document your BB.

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
