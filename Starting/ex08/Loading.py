import sys

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, v in enumerate(lst, start=1):
        n = round((v + 1) / total * 100)
        process = f'=' * n
        space = f' ' * (100 - n)
        string = f' {n}%|[{process}>{space}]| {v + 1}/{total}'
        # if 100%  removes characters beginning
        if n == 100:
            string = string.strip()
        print(string, file=sys.stderr, end='\r')
        yield i
