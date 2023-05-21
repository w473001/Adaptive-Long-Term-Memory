from src.backtest.parallel_backtest import run_parallel_backtest


def main():
    config_name = 'tuned_config_multi'
    run_parallel_backtest(from_config=config_name, base_seed=12345)


if __name__ == '__main__':
    from datetime import datetime
    start = datetime.now()
    main()
    end = datetime.now()
    print(f"started {start}. finished {end}")
