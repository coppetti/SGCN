import argparse

def parameter_parser():
    """
    A method to parse up command line parameters. By default it gives an embedding of the Bitcoin OTC dataset.
    The default hyperparameters give a good quality representation without grid search.
    Representations are sorted by node ID.
    """

    parser = argparse.ArgumentParser(description = "Run SGCN.")


    parser.add_argument('--edge-path',
                        nargs = '?',
                        default = './input/bitcoin_otc.csv',
	                help = 'Edge list csv.')

    parser.add_argument('--embedding-path',
                        nargs = '?',
                        default = './output/embedding/bitcoin_otc_sgcn.csv',
	                help = 'Target embedding csv.')

    parser.add_argument('--regression-weights-path',
                        nargs = '?',
                        default = './output/weights/bitcoin_otc_sgcn.csv',
	                help = 'Regression weights csv.')

    parser.add_argument('--log-path',
                        nargs = '?',
                        default = './logs/bitcoin_otc_logs.json',
	                help = 'Log json.')

    parser.add_argument('--epochs',
                        type = int,
                        default = 50,
	                help = 'Number of training epochs. Default is 50.')

    parser.add_argument('--reduction-iterations',
                        type = int,
                        default = 30,
	                help = 'Number of SVD iterations. Default is 30.')

    parser.add_argument('--reduction-dimensions',
                        type = int,
                        default = 128,
	                help = 'Number of SVD feature extraction dimensions. Default is 128.')

    parser.add_argument('--seed',
                        type = int,
                        default = 42,
	                help = 'Random seed for sklearn pre-training. Default is 42.')

    parser.add_argument('--lamb',
                        type = float,
                        default = 1.0,
	                help = 'Embedding regularization parameter. Default is 1.0.')

    parser.add_argument('--gamma',
                        type = float,
                        default = 0.001,
	                help = 'Weight regularization parameter. Default is 0.001.')

    parser.add_argument('--test-size',
                        type = float,
                        default = 0.2,
	                help = 'Test dataset size. Default is 0.2.')

    parser.add_argument('--learning-rate',
                        type = float,
                        default = 0.01,
	                help = 'Learning rate. Default is 0.01.')

    parser.add_argument('--weight-decay',
                        type = float,
                        default = 10**-5,
	                help = 'Learning rate. Default is 10^-5.')

    parser.add_argument('--layers',
                        nargs='+',
                        type=int,
                        help = 'Layer dimensions separated by space. E.g. 128 64 32.')
	
    parser.set_defaults(layers=[64, 32])
    
    return parser.parse_args()