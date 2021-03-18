#!/usr/bin/python3

# To set global building block debug mode
from permedcoe import set_debug
# Import building block entry points
from sample_BB import invoke
from sample_BB import personalize_model_bb_extended


def main():
    set_debug(True)
    print("Sample python application using sample BB")
    conf = {"suffix": "META_mutations_CNA_asMutant",
            "model": "Fumia2013"}
    invoke("../dataset/Fumia_META_mutCNA.csv",
           "output",
           conf)


if __name__ == "__main__":
    main()
