#!/usr/bin/python3
import os

from permedcoe import Container        # To define container related needs
from permedcoe import Binary           # To define binary to execute related needs
from permedcoe import Task             # To define task related needs

from permedcoe import FILE_IN          # To define file type and direction
from permedcoe import FILE_OUT         # To define file type and direction
from permedcoe import DIRECTORY_IN     # To define directory type and direction
from permedcoe import DIRECTORY_OUT    # To define directory type and direction

from permedcoe import get_environment  # Get variables from invocation


# Single and global container definition for this building block
# CAUTION: This path will depend on how we agree to work for the building blocks.
#          For instance: if we want different repositories for each building block,
#          then we should think that the container definition has also to be provided
#          by the package.
#          Alternative: we could agree a common path where the definitions have to be
#          placed, and use an environment variable.
SAMPLE_CONTAINER = str(os.environ["HOME"]) + "/github/projects/PerMedCoE/basic_application/sample_BB/image/PerMedCoE-Pilot.sif"


########################################################
# SPECIFIC FOR PyCOMPSs                                #
# Allows a user defined python function as entry point #
########################################################

def personalize_model_bb_extended(*args, **kwargs):
    """ Extended python interface:
    To be used only with PyCOMPSs - Enables to define a workflow within the building block.
    Requirement: all tasks should be executed in a container (with the same container definition)
                 to ensure that they all have the same requirements.
    """
    print("Hello super world!")
    # Pure python code calling to PyCOMPSs tasks (that can be defined in this file or in another).


####################################
# COMMON FOR ALL WORKFLOW MANAGERS #
####################################

@Container(engine="SINGULARITY", image=SAMPLE_CONTAINER)
@Binary(binary="/usr/local/bin/PROFILE_personalize.py")
@Task(mutations_dataset=FILE_IN, output=DIRECTORY_OUT)
def personalize_model_task(system_flag="-sy", system="Linux",
                           suffix_flag="-s", suffix="META_mutations_CNA_asMutant",
                           mutations_dataset_flag="-m", mutations_dataset=None,
                           output_flag="-O", output=None,
                           model="Fumia2013"):
    # Empty since it represents a binary execution.
    # /usr/local/bin/PROFILE_personalize.py -sy Linux -s META_mutations_CNA_asMutant ...
    pass


def invoke(input, output, config):
    """ Common interface.
    Invoked from command line or from PyCOMPSs application.

    Translates the input, output and config parameters into the real
    function call. Avoids to force BB developers to implement this
    internally on their sources.

    Args:
        input (str): Input file path.
        output (str): Output directory path.
        config (dict): Configuration dictionary.
    Returns:
        None
    """
    # Declare how to run the task specification
    # Convert config into bb_name_task_call
    suffix = config["suffix"]
    model = config["model"]
    # env_vars = get_environment()  # NOSONAR - Retrieves the extra flags.
    personalize_model_task(suffix=suffix,
                           model=model,
                           mutations_dataset=input,
                           output=output)
