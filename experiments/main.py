from experiment_suite.experiment_utils import hyperparams, storage, manager
import time
import numpy as np


def run_experiment(
        run_dir: str,
        run_idx: int,
        param_a: int,
        param_b: int
):
    mm = manager.Manager(run_dir)
    time.sleep(20)
    mm.mark_as_spun_up()
    mm.log('value', param_a * param_b)

if __name__ == '__main__':
    parser = hyperparams.build_parser_for_experiment(run_experiment)
    args = parser.parse_args()
    run_experiment(**args.__dict__)
