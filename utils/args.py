import argparse

def Segmentation_argparser():
    parser = argparse.ArgumentParser(description='PyTorch Semantic Segmentation Training')
    parser.add_argument('--loss-type', type=str, default='CE',
                        choices=['CE'],
                        help='loss func type (default: ce)')
    parser.add_argument('--batch-norm', type=bool, default=True,
                        choices=[True, False],
                        help='Whether the UNet has or not')
    
    parser.add_argument('--num-classes', type=int, default=3)
    parser.add_argument('--use-balanced-weights', type=bool, default=True)

    # training hyperparameters
    parser.add_argument('--epochs', type=int, default=20, metavar='N',
                        help='number of epochs to train (default: auto)')
    parser.add_argument('--batch-size', type=int, default=8,
                        metavar='N', help='input batch size for training (default: auto)')
    parser.add_argument('--test-batch-size', type=int, default=2,
                        metavar='N', help='input batch size for training (default: auto)')


    # optimizer parameters
    parser.add_argument('--lr', type=float, default=1e-3, metavar='LR',
                        help='learning rate (default: auto)')

    # choose model
    parser.add_argument('--model', type=str, default='UNet',
                        choices=['UNet'],
                        help='Choose segmentation models')

    return parser