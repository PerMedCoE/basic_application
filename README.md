# HPC/Exascale Centre of Excellence in Personalised Medicine

## Sample application

This repository contains a sample application using a single Building Block (BB) within the **HPC/Exascale Centre of Excellence in Personalised Medicine**
([PerMedCoE](https://permedcoe.eu/)) project.

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Sample application](#sample-application)
  - [Table of Contents](#table-of-contents)
  - [Repository contents](#repository-contents)
  - [Usage](#usage)
    - [1<sup>st</sup> - Install `permedcoe` package](#1supstsup---install-permedcoe-package)
    - [2<sup>nd</sup> - Install the `sample_BB` package](#2supndsup---install-the-sample_bb-package)
    - [3<sup>rd</sup> - Execute one of the sample applications](#3suprdsup---execute-one-of-the-sample-applications)
  - [License](#license)
  - [Contact](#contact)

## Repository contents

- **sample_BB:** Sample building block (uses the `permedcoe` package provided by PerMedCoE).
- **sample_app:** Sample application using `sample_BB`.

## Usage

### 1<sup>st</sup> - Install `permedcoe` package

  ```shell
  git clone https://github.com/PerMedCoE/permedcoe.git
  cd permedcoe
  ./install.sh
  cd ..
  ```

### 2<sup>nd</sup> - Install the `sample_BB` package

  ```shell
  git clone https://github.com/PerMedCoE/basic_application.git
  cd basic_application/sample_BB
  ./install.sh
  cd ../..
  ```

### 3<sup>rd</sup> - Execute one of the sample applications

- **PyCOMPSs** sample application:

  > NOTE: Requires PyCOMPSs installed in the machine.

  ```shell
  cd basic_application/sample_app/PyCOMPSs
  ./launch.sh
  cd ../..
  ```

- **Nextflow** sample application:

  > NOTE: Requires Nextflow installed in the machine.

  ```shell
  cd basic_application/sample_app/Nextflow
  ./launch.sh
  cd ../..
  ```

- **Snakemake** sample application:

  > NOTE: Requires Snakemake installed in the machine.

  ```shell
  cd basic_application/sample_app/Snakemake
  ./launch.sh
  cd ../..
  ```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
