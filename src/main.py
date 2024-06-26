from utils import tab_printer
from model import Trainer
from param_parser import parameter_parser

def main():
    """
    Parsing command line parameters, reading data.
    Fitting and scoring a SimGNN model.
    """
    args = parameter_parser()
    tab_printer(args)
    trainer = Trainer(args)
    if args.load_path:
        trainer.load()
    else:
        trainer.fit()
    trainer.score()
    if args.save_path:
        trainer.save()

if __name__ == "__main__":
    main()
