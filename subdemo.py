import sys
import argparse

from utils import read_config, error_exit
import local    # Beam flow with local batch processing
import gcloud   # Beam flow with stream processing using GC features

# --------------------------------------------------------------------
# Testing Beam...

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Running the selected demo beam pipeline')
    parser.add_argument('--cfgfile', default='config.json', help='Config file name with path')
    parser.add_argument('--pipeline', help='Pipeline to run: local | gcp')
    args = parser.parse_args()

    cfg = read_config(args.cfgfile)

    if args.pipeline == 'local':
        local.run_pipeline(cfg)
    elif args.pipeline == 'gcp':
        gcloud.run_pipeline(cfg)
    else:
        error_exit('Invalid option for argument --pipeline.\nValid options: local | gcp')

    print('\nNormal program termination.\n')