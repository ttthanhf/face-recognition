
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='command')

    test = subparser.add_parser('test')
    test.add_argument('run')

    server = subparser.add_parser('server')
    server.add_argument('start')

    scan = subparser.add_parser('scan')
    scan.add_argument('run')

    setup = subparser.add_parser('setup')

    args = parser.parse_args()

    if(args.command == 'test'):
        if(args.run):
            from test import test_zone
            test_zone()

    if(args.command == 'server'):
        if(args.start):
            import server.server 
            server.start()
        
    if(args.command == 'scan'):
        if(args.run):
            import scan.scan
            scan.Scan()

    if(args.command == 'setup'):
        print('scetup')

