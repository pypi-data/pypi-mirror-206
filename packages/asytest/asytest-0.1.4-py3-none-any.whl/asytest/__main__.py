from .asytest import parse_args, run_tests


if __name__ == "__main__":
    args = parse_args()
    run_tests(args.resource, args.max_concurrent)