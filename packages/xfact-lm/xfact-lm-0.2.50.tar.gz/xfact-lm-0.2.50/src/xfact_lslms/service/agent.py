import logging
import argparse

from xfact_lslms.log_helper import setup_logging
from xfact_lslms.service.amq_communications import CommunicationLayer
from models import LanguageModelAgent

logger = logging.getLogger(__name__)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='t5-base', help='Model name')
    parser.add_argument('--cache_dir', default=None)
    parser.add_argument('--fp16', action='store_true')
    parser.add_argument('--bf16', action='store_true')
    parser.add_argument('--multi_gpu', action='store_true')
    parser.add_argument('--auto_map', action='store_true')
    parser.add_argument('--gpu0', action='store', type=int, default=10, help='Max memory in GiB to be used by GPU_0 to load the model')

    return parser.parse_args()


if __name__ == "__main__":
    setup_logging()
    args = get_args()

    lm = LanguageModelAgent(args)
    model_queue = args.model.split('/')[-1].lower()

    generate = lambda message: lm.infer(**message)
    forward = lambda message: lm.forward(**message)

    comms = CommunicationLayer(model_queue, generate, forward)
    comms.listen()
