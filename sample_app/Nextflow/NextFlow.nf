
params.input="../dataset/Fumia_META_mutCNA.csv"
params.config="../config/conf.yaml"

input_ch = Channel.fromPath(params.input)
conf_ch = Channel.fromPath(params.config)

process personalize {
    input:
    file csv from input_ch
    file conf from conf_ch

    output:
    file "output" into res_ch

    """
    permedcoe execute building_block bb $csv output $conf
    """
}
