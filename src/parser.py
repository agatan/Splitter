import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it trains on the Cora dataset.
    The default hyperparameters give a good quality representation without grid search.
    """

    parser = argparse.ArgumentParser(description = "Run Splitter.")

    parser.add_argument("--edge-path",
                        nargs = "?",
                        default = "./input/cora_edges.csv",
	                help = "Edge list csv.")

    parser.add_argument("--embedding-output-path",
                        nargs = "?",
                        default = "./output/cora_embedding.csv",
	                help = "Target classes csv.")

    parser.add_argument("--persona-output-path",
                        nargs = "?",
                        default = "./input/cora_personas.json",
	                help = "Target classes csv.")

    parser.add_argument("--epochs",
                        type = int,
                        default = 1,
	                help = "Number of training epochs. Default is 200.")

    parser.add_argument("--number-of-walks",
                        type = int,
                        default = 10,
	                help = "Number of training epochs. Default is 200.")

    parser.add_argument("--window-size",
                        type = int,
                        default = 5,
	                help = "Number of training epochs. Default is 200.")

    parser.add_argument("--negative-samples",
                        type = int,
                        default = 5,
	                help = "Number of training epochs. Default is 200.")

    parser.add_argument("--walk-length",
                        type = int,
                        default = 40,
	                help = "Number of training epochs. Default is 200.")

    parser.add_argument("--seed",
                        type = int,
                        default = 42,
	                help = "Random seed for train-test split. Default is 42.")

    parser.add_argument("--early-stopping",
                        type = int,
                        default = 5,
	                help = "Number of early stopping rounds. Default is 5.")

    parser.add_argument("--start-learning-rate",
                        type = float,
                        default = 0.01,
	                help = "Learning rate. Default is 0.01.")

    parser.add_argument("--lambd",
                        type = float,
                        default = 0.1,
	                help = "Learning rate. Default is 0.01.")

    parser.add_argument("--minimal-learning-rate",
                        type = float,
                        default = 0.001,
	                help = "Learning rate. Default is 0.01.")

    parser.add_argument("--dimensions",
                        type = int,
                        default = 32,
	                help = "Learning rate. Default is 0.01.")

    parser.add_argument('--workers',
                        type = int,
                        default = 4,
	                help = 'Number of parallel workers. Default is 4.')

    return parser.parse_args()