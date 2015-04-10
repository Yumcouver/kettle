import yaml
import os
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(PROJECT_PATH, 'config.yaml')) as config_fp:
    application_config = yaml.load(config_fp)

    SPHINX_HMM = os.path.join(PROJECT_PATH, application_config['sphinx.hmm'])
    SPHINX_LM = os.path.join(PROJECT_PATH, application_config['sphinx.lm'])
    SPHINX_DICT = os.path.join(PROJECT_PATH, application_config['sphinx.dict'])
