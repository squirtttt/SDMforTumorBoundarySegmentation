import os, glob, json
import numpy as np

from utils.mypath import Path

class Saver(object):

    def __init__(self, args):
        self.args = args
        self.dir = os.path.join(Path.pathology_root_dir(), self.args.model)
        self.runs = sorted(glob.glob(os.path.join(self.dir, 'experiment_*')))
        
        indices = []
        for tmp in self.runs:
            tmp_num = tmp.split("/")[-1]
            tmp_num = int(tmp_num.split("_")[-1])
            indices.append(tmp_num)

        if len(indices) == 0:
            run_id = str(0)
        else:
            run_id = np.max(indices) + 1

        self.experiment_dir = os.path.join(self.dir, f'experiment_{str(run_id)}')

        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

        if not os.path.exists(self.experiment_dir):
            os.makedirs(self.experiment_dir)

    def save_experiment_config(self, args):
        self.save_args = args.__dict__.copy()
        if 'cuda' in self.save_args:
            del(self.save_args['cuda'])

        with open(os.path.join(self.experiment_dir, 'arg_parser.txt'), 'w') as f:
            json.dump(self.save_args, f, indent=2)
        
        f.close()