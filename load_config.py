import yaml

with open('config.yaml') as config_fp:
    application_config = yaml.load(config_fp)

    SPHINX_HMM = application_config['sphinx.hmm']
    SPHINX_LM = application_config['sphinx.lm']
    SPHINX_DICT = application_config['sphinx.dict']
